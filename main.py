# Marvin Nahmias. Todos los derechos reservados. (2021)
# Puedes usar este código libremente, solo referencíame con link a GitHub.
# Revisar CFDIs validos ante SAT con 4 argumentos:
# RFC Emisor, RFC Receptor, Monto del CFDI Neto, Folio
# Se utiliza FastAPI como framework, Suds-py3 como SOAP client
# y JSON para serializar

import json, ssl
from fastapi import FastAPI, Response
from suds.client import Client

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
app = FastAPI(title="SAT México APIs - Toolkit (Marvin Nahmias)",
    description="Aquí encontraras una manera de verificar si una factura o recibo de nómina en México son validos, via un REST API como puente al SAT, sin ´throttling´.",
    version="0.0.1",
    terms_of_service="http://about.me/mexmarv")

#en el root
@app.get("/")
async def root():
    return {"Bienvenid@!": "Consulta /docs para mas información de los APIs."}

@app.get("/sat")
async def sat(rfce: str, rfcr: str, monto: str, uuid: str):     
    obj_sat = {"rfce": rfce, "rfcr": rfcr, "monto": monto, "uuid": uuid}   
    
    if (rfce != "") or (rfcr != "") or (monto != "") or (uuid != ""):
        sat_query = "re=" + rfce + "&rr=" + rfcr + "&tt=" + monto + "&id=" + uuid
        client = Client('https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc?WDSL')
        result = client.service.Consulta(sat_query)
        ParsedResponse = fastest_object_to_dict(result)

    return Response(content=json.dumps(ParsedResponse),media_type="application/json")

