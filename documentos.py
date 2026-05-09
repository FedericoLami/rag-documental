import chromadb
from sentence_transformers import SentenceTransformer
pip install pymupdf

def cargar_documento(ruta):
    with open(ruta, "r", encoding = "utf-8") as text:
        contenido = text.read()
    return contenido

def dividir_en_fragmentos(texto, size = 500, solapamiento = 50):
    i = 0
    listaTexto = []
    while (i < len(texto)):
        listaTexto.append(texto[i: i + size])
        i += size - solapamiento
    return listaTexto

def guardar_en_chromadb(fragmentos,nombre_coleccion):
    cliente = chromadb.Client()
    
    modelo = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = modelo.encode(fragmentos)

    coleccion = cliente.get_or_create_collection(nombre_coleccion)
    ids = []
    for i in range(len(fragmentos)):
        ids.append(f"fragmento_{i}")
    coleccion.add(
        documents = fragmentos,
        embeddings = embeddings,
        ids = ids
    )
    