from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from documentos import cargar_documento,dividir_en_fragmentos,guardar_en_chromadb
from chat import responder,procesar_documento

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MensajeRequest(BaseModel):
    mensaje:str

class RutaRequest(BaseModel):
    ruta:str

@app.post("/cargar")
def cargar_archivo(request: RutaRequest):
    try: 
        procesar_documento(request.ruta)
    except ValueError:
        raise HTTPException(status_code=500, detail="Error al procesar el documento")
    return {"mensaje" : "Documento cargado correctamente"}

@app.post("/preguntar")
def recibir_pregunta(request: MensajeRequest):
    try:
        resp = responder(request.mensaje)
    except ValueError:
        raise HTTPException(status_code=500, detail="Error al procesar la respuesta de claude")
    return resp