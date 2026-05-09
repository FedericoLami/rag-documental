import chromadb
from sentence_transformers import SentenceTransformer
import os


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
    return