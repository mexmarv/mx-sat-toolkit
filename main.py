# Marvin Nahmias. Todos los derechos reservados. (2021)
# Puedes usar este código libremente, solo referencíame con link a GitHub.
# SAT MX TOOLKIT
# Se utiliza FastAPI como framework, uvicorn, pyfiscal, Suds-py3 como SOAP client
# y JSON para serializar

import json, ssl
from datetime import date
from typing import Union
from fastapi import FastAPI, Response, HTTPException
from suds.client import Client
from pyfiscal.generate import GenerateRFC, GenerateCURP

# Funcion para convertir SUDS a DICT/Tuple
def fastest_object_to_dict(obj):
    if not hasattr(obj, '__keylist__'):
        return obj
    data = {}
    fields = obj.__keylist__
    for field in fields:
        val = getattr(obj, field)
        if isinstance(val, list):  # tuple not used
            data[field] = []
            for item in val:
                data[field].append(fastest_object_to_dict(item))
        else:
            data[field] = fastest_object_to_dict(val)
    return data

#Entidades SAT
entities = { 
			'': '',
			'AGUASCALIENTES': 'AS',
			'BAJA CALIFORNIA': 'BC',
			'BAJA CALIFORNIA SUR': 'BS',
			'CAMPECHE': 'CC',
			'CHIAPAS': 'CS',
			'CHIHUAHUA': 'CH',
			'COAHUILA': 'CL',
			'COLIMA': 'CM',
			'DISTRITO FEDERAL': 'DF',
			'DURANGO': 'DG',
			'GUANAJUATO': 'GT',
			'GUERRERO': 'GR',
			'HIDALGO': 'HG',
			'JALISCO': 'JC',
			'MEXICO': 'MC',
			'MICHOACAN': 'MN',
			'MORELOS': 'MS',
			'NAYARIT': 'NT',
			'NUEVO LEON':'NL',
			'OAXACA': 'OC',
			'PUEBLA': 'PL', 
			'QUERETARO': 'QT',
			'QUINTANA ROO': 'QR',
			'SAN LUIS POTOSI': 'SP',
			'SINALOA': 'SL',
			'SONORA': 'SR',
			'TABASCO': 'TC',
			'TAMAULIPAS': 'TS',
			'TLAXCALA': 'TL',
			'VERACRUZ': 'VZ',
			'YUCATÁN': 'YN',
			'ZACATECAS': 'ZS',
			'NACIDO EXTRANJERO': 'NE'
		}

# Tags API Fields
tags = [
     {
        "name": "/",
        "description": "SAT MX Toolkit. Consulta /docs para mas información de los APIs.",
    },
    {
        "name": "RFC",
        "description": "Calculo de RFC PF con Homoclave. La **fecha** es formato *yyyy-mm-dd*.",
    },
    {
        "name": "CURP",
        "description": "Calculo de CURP. La **fecha** es formato *yyyy-mm-dd*.",
    },
    {
        "name": "CFDI",
        "description": "Validacion de Factura o Recibo de Nomina. El **monto** es *sin comas y con dos decimales*.",
    },
]
#Ignora errores SSL certificados 
ssl._create_default_https_context = ssl._create_unverified_context

#Inicializa FastAPI
app = FastAPI(title="SAT-MX Toolkit de APIs",
    description="Toolkit de APIs de servicios con el SAT. Revisar CFDIs y Calculo de RFC con Homoclave.",
    version="1.2",
    contact={
        "name": "Marvin Nahmias",
        "url": "http://about.me/mexmarv",
        "email": "mexmarv@gmail.com",
    },
    license_info={
        "name": "Creative Commons Zero 1.0",
        "url": "https://github.com/mexmarv/mx-sat-toolkit/blob/main/LICENSE",
    },
    openapi_tags=tags
    )

#en el root
@app.get("/", tags=["/"])
async def root():
    return {"Bienvenid@ al toolkit del SAT!": "Consulta /docs para mas información de los APIs."}

@app.get("/sat-rfc", tags=["RFC"])
async def rfc(nombre: str, apellido1: str, apellido2: str, fecha: Union[date, None]):      
    if (nombre != "") or (apellido1 != "") or (apellido2 != ""):
        kwargs = {
            "complete_name": nombre,
            "last_name": apellido1,
            "mother_last_name": apellido2,
            "birth_date": fecha.strftime("%d-%m-%Y")
        }

        rfc = GenerateRFC(**kwargs)
        results = {"RFC": rfc.data}
    return results

@app.get("/sat-curp", tags=["CURP"])
async def sat_curp(nombre: str, apellido1: str, apellido2: str, fecha: Union[date, None], genero: str, codigo_edo: str ): 
        
        if codigo_edo.upper() not in entities.values():
            raise HTTPException(status_code=404, detail= codigo_edo + " no existe. Los Validos son: " + json.dumps(entities))
        else:
            ciudad = list(entities.keys())[list(entities.values()).index(codigo_edo.upper())] 

            kwargs2 = {
                "complete_name": nombre,
                "last_name": apellido1,
                "mother_last_name": apellido2,
                "birth_date": fecha.strftime("%d-%m-%Y"),
                "gender": genero.upper(),
                "city": ciudad,
                "state_code": codigo_edo
            }
            curp = GenerateCURP(**kwargs2)
            results = {"CURP": curp.data}  
        return results

@app.get("/sat-cfdi", tags=["CFDI"])
async def cfdi(rfce: str, rfcr: str, monto: str, folio: str):     
    obj_cfdi = {"rfce": rfce, "rfcr": rfcr, "monto": monto, "folio": folio}   
    
    if (rfce != "") or (rfcr != "") or (monto != "") or (folio != ""):
        sat_query = "re=" + rfce + "&rr=" + rfcr + "&tt=" + monto + "&id=" + folio
        client = Client('https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc?WDSL')
        result = client.service.Consulta(sat_query)
        ParsedResponse = fastest_object_to_dict(result)

    return Response(content=json.dumps(ParsedResponse),media_type="application/json")

