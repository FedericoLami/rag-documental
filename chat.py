import anthropic
from dotenv import load_dotenv
from buscador import buscar_fragmentos
from documentos import cargar_documento, dividir_en_fragmentos, guardar_en_chromadb

load_dotenv()

client = anthropic.Anthropic()
nombre_coleccion = "mi_documento"

def procesar_documento(ruta):
    contenido = cargar_documento(ruta)
    lista_texto = dividir_en_fragmentos(contenido)
    guardar_en_chromadb(lista_texto,nombre_coleccion)

def responder(pregunta):
    fragmento = buscar_fragmentos(pregunta,nombre_coleccion)
    mensajes = [{"role": "user", "content": pregunta}]
    answer = client.messages.create(
        model = "claude-haiku-4-5",
        max_tokens = 1024,
        system = f"""Basándote únicamente en el siguiente contexto, 
                   respondé la pregunta. Contexto: {fragmento}. Pregunta: {pregunta}
                """,
        messages = mensajes
    )
    return answer.content[0].text

def conversacion_claude():
    fin = False
    encontrado = False
    print("Para finalizar en cualquier momento ingresar el mensaje: fin")
    
    while ((not encontrado) and (not fin)):
        ruta = input("Ingresa la ruta del documento: ")

        if ruta == "fin":
            fin = True
      
        if not fin:
            try:
                procesar_documento(ruta)
                encontrado = True
            except FileNotFoundError:
                print("Documento no encontrado, ingresar nuevamente: ")
    
    while not fin:
        mensaje = input("Ingresa tu consulta o fin para finalizar: ")
        if mensaje == "fin":
            fin = True
        if (not fin):
            print(responder(mensaje))

conversacion_claude()

