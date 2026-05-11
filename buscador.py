import chromadb

def buscar_fragmentos(pregunta, nombre_coleccion, n_resultados=3):
    cliente = chromadb.Client()
    coleccion = cliente.get_or_create_collection(nombre_coleccion)
    
    resultados = coleccion.query(
        query_texts=[pregunta],
        n_results=n_resultados
    )
    
    return resultados["documents"][0]