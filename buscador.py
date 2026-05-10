from sentence_transformers import SentenceTransformer
import chromadb


def buscar_fragmentos(pregunta, nombre_coleccion, n_resultados=3):
    cliente = chromadb.Client()
    coleccion = cliente.get_or_create_collection(nombre_coleccion)
    modelo = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = modelo.encode(pregunta)
    
    resultados = coleccion.query(
        query_embeddings=[embedding],
        n_results=n_resultados
    )
    
    return resultados["documents"][0]