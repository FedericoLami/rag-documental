# RAG Documental con IA

Sistema de consulta inteligente sobre documentos propios usando Retrieval Augmented Generation (RAG). Cargás un archivo PDF o TXT, y el sistema lo indexa semánticamente en una base de datos vectorial. A partir de ahí podés hacerle preguntas en lenguaje natural y Claude responde basándose exclusivamente en el contenido del documento, no en su conocimiento general.

Pensado para automatizar la consulta de documentación interna en entornos empresariales: manuales técnicos, reglamentos, contratos, informes, bases de conocimiento, y cualquier documento sobre el que se necesite respuesta rápida y precisa sin intervención humana.

---

## Demo

![Demo del sistema RAG](demo.gif)

---

## Tecnologías utilizadas

| Capa | Tecnología |
|------|-----------|
| Modelo de lenguaje | Claude Haiku (Anthropic API) |
| Base de datos vectorial | ChromaDB |
| Extracción de PDF | PyMuPDF (fitz) |
| Backend / API REST | FastAPI + Uvicorn |
| Frontend | HTML · CSS · JavaScript vanilla |
| Configuración | python-dotenv |
| Entorno | Python 3.11 + venv |

---

## Arquitectura del proyecto

```
rag-documental/
├── documentos.py     # Carga, fragmentación e indexación de documentos
├── buscador.py       # Búsqueda semántica en ChromaDB
├── chat.py           # Lógica de respuesta con Claude
├── main.py           # API REST con FastAPI (endpoints)
├── index.html        # Interfaz web
├── .env              # Variables de entorno (no se sube a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

Cada archivo tiene una única responsabilidad:

- `documentos.py` lee el archivo, lo divide en fragmentos con solapamiento y los indexa en ChromaDB.
- `buscador.py` convierte la pregunta del usuario en una consulta semántica y recupera los fragmentos más relevantes.
- `chat.py` arma el prompt con el contexto recuperado y obtiene la respuesta de Claude.
- `main.py` expone dos endpoints REST y coordina las capas anteriores.

---

## ¿Qué es RAG?

RAG (Retrieval Augmented Generation) es un patrón arquitectónico que combina búsqueda semántica con generación de lenguaje natural.

En lugar de enviar el documento completo al modelo (costoso e ineficiente), el sistema:

1. Divide el documento en fragmentos con solapamiento
2. Los indexa en una base de datos vectorial
3. Cuando llega una pregunta, recupera solo los fragmentos relevantes
4. Le pasa esos fragmentos a Claude como contexto para que responda

Esto permite trabajar con documentos de cualquier tamaño y garantiza que las respuestas estén ancladas en el contenido real del documento.

---

## Endpoints de la API

### `POST /cargar`

Recibe la ruta de un documento, lo procesa y lo indexa en ChromaDB.

**Request:**
```json
{
  "ruta": "C:/documentos/manual_tecnico.pdf"
}
```

**Response:**
```json
{
  "mensaje": "Documento cargado correctamente"
}
```

### `POST /preguntar`

Recibe una pregunta en lenguaje natural y devuelve la respuesta de Claude basada en el documento.

**Request:**
```json
{
  "mensaje": "¿Cuáles son los pasos para administrar el test?"
}
```

**Response:**
```
"Según el documento, los pasos son..."
```

---

## Instalación y uso

### Requisitos previos

- Python 3.11
- API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com))

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/rag-documental.git
cd rag-documental

# 2. Crear y activar entorno virtual
py -3.11 -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crear archivo .env en la raíz del proyecto:
ANTHROPIC_API_KEY=tu-api-key-aquí

# 5. Iniciar el servidor
uvicorn main:app --reload
```

### Interfaz web

Con el servidor corriendo, abrí `index.html` directamente en el navegador. Ingresá la ruta completa de tu documento PDF o TXT y comenzá a hacer preguntas.

### Documentación interactiva de la API

```
http://127.0.0.1:8000/docs
```

FastAPI genera automáticamente una interfaz para probar todos los endpoints.

---

## Casos de uso empresariales

- **Recursos Humanos:** consultas sobre reglamentos internos, políticas de la empresa o convenios colectivos sin necesidad de buscar manualmente.
- **Legal:** análisis rápido de contratos o documentos legales extensos, localizando cláusulas específicas en segundos.
- **Soporte técnico:** base de conocimiento inteligente sobre manuales de productos o guías de troubleshooting.
- **Salud:** consulta de protocolos clínicos o guías de práctica médica para profesionales de la salud.
- **Educación:** sistema de preguntas y respuestas sobre material de estudio o documentación académica.

---

## Autor

**Federico Lami**
[LinkedIn](https://www.linkedin.com/in/federicolami/)