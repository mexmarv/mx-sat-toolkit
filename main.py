# Marvin Nahmias. Todos los derechos reservados. (2021)
# Puedes usar este código libremente, solo referencíame con link a GitHub.
# Revisar CFDIs validos ante SAT con 4 argumentos:
# RFC Emisor, RFC Receptor, Monto del CFDI Neto, Folio
# Se utiliza FastAPI como framework, Suds-py3 como SOAP client
# y JSON para serializar

import json, ssl
from fastapi import FastAPI, Response
from suds.client import Client
from pyfiscal.generate import GenerateRFC

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
    }
    )

#en el root
@app.get("/")
async def root():
    return {"Bienvenid@ al toolkit del SAT!": "Consulta /docs para mas información de los APIs."}

@app.get("/sat-cdfi")
async def cdfi(rfce: str, rfcr: str, monto: str, folio: str):     
    obj_cfdi = {"rfce": rfce, "rfcr": rfcr, "monto": monto, "folio": folio}   
    
    if (rfce != "") or (rfcr != "") or (monto != "") or (folio != ""):
        sat_query = "re=" + rfce + "&rr=" + rfcr + "&tt=" + monto + "&id=" + folio
        client = Client('https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc?WDSL')
        result = client.service.Consulta(sat_query)
        ParsedResponse = fastest_object_to_dict(result)

    return Response(content=json.dumps(ParsedResponse),media_type="application/json")

@app.get("/sat-rfc")
async def rfc(nombre: str, apellido1: str, apellido2: str, fecha: str):      
    if (nombre != "") or (apellido1 != "") or (apellido2 != "") or (fecha != ""):
        kwargs = {
            "complete_name": nombre,
            "last_name": apellido1,
            "mother_last_name": apellido2,
            "birth_date": fecha
        }

        rfc = GenerateRFC(**kwargs)
        results = {"RFC": rfc.data}
    return results

