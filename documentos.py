import chromadb
import fitz

def cargar_documento(ruta):
    if (ruta.endswith(".pdf")):
        doc = fitz.open(ruta)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()
        contenido = texto
    else:
        with open(ruta, "r", encoding="utf-8") as text:
            contenido = text.read()
    return contenido

def dividir_en_fragmentos(texto, size=500, solapamiento=50):
    i = 0
    listaTexto = []
    while (i < len(texto)):
        listaTexto.append(texto[i: i + size])
        i += size - solapamiento
    return listaTexto

def guardar_en_chromadb(fragmentos, nombre_coleccion):
    cliente = chromadb.Client()
    coleccion = cliente.get_or_create_collection(nombre_coleccion)
    ids = [f"fragmento_{i}" for i in range(len(fragmentos))]
    coleccion.add(
        documents=fragmentos,
        ids=ids
    )