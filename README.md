```markdown
# 📅 Asistente Inteligente de Planificación Semanal (IA Multi-Agente)

Este proyecto implementa un sistema de **Agentes de IA** orquestados con **LangGraph** y potenciados por **Llama 3 (vía Groq)**. El objetivo es transformar listas de tareas desordenadas en una planificación semanal optimizada, respetando restricciones de tiempo y energía.

## 🚀 Funcionalidad Principal

El sistema utiliza una arquitectura de grafo donde múltiples agentes colaboran:
1.  **Analizer Agent:** Interpreta el lenguaje natural, extrae tareas y estima atributos faltantes (prioridad, duración).
2.  **Planifier Agent:** Distribuye las tareas en la semana (Lunes-Viernes) optimizando la carga cognitiva.
3.  **Evaluator Agent:** Revisa el plan generado buscando errores lógicos o sobrecargas (>8h/día) y solicita correcciones si es necesario (Bucle de Auto-Reflexión).
4.  **Persistence:** Guarda el resultado final en un archivo JSON local.

## 📂 Estructura del Proyecto

La arquitectura está modularizada siguiendo principios de separación de responsabilidades:

```text
.
├── src/
│   ├── nodes/                 # Lógica individual de cada agente
│   │   ├── analizer_node.py   # Agente de análisis y extracción
│   │   ├── planifier_node.py  # Agente de planificación y calendario
│   │   ├── evaluator_node.py  # Agente crítico (Quality Assurance)
│   │   └── persistence_node.py # Manejo de I/O (guardado de archivos)
│   ├── routers/
│   │   └── evaluator_router.py # Lógica condicional (Circuit Breaker)
│   ├── graph.py               # Definición y ensamblaje del StateGraph
│   ├── groq_config.py         # Configuración del cliente ChatGroq
│   ├── models.py              # Esquemas de datos Pydantic
│   └── state.py               # Definición del estado compartido (TypedDict)
├── main.py                    # Punto de entrada (Ejecución por consola)
├── langgraph.json             # Configuración para LangGraph Studio
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Variables de entorno (No incluido en git)
└── .gitignore                 # Archivos excluidos del control de versiones

```

## 🛠️ Requisitos Previos

* Python 3.10+
* Cuenta en [Groq Cloud](https://console.groq.com) (para inferencia LLM rápida).
* Cuenta en [LangSmith](https://smith.langchain.com/) (Recomendado para visualización de trazas).
* Docker Desktop (Solo necesario si vas a usar la interfaz visual de LangGraph Studio).

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_CARPETA>

```


2. **Crear y activar entorno virtual:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```


3. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


4. **Configurar Variables de Entorno:**
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```ini
# Motor de IA (Obligatorio)
GROQ_API_KEY=gsk_tu_clave_secreta_aqui

# Visualización y Trazas (Recomendado para LangGraph Studio)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT="agenda-asistente"
LANGCHAIN_API_KEY=lsv2_tu_clave_langsmith_aqui

```



## ▶️ Ejecución

### Opción A: Vía Consola (CLI)

Para ejecutar el flujo completo y generar el archivo de planificación directamente:

```bash
python main.py

```

El resultado se guardará como `plan_semanal_final.json` en el directorio raíz.

### Opción B: LangGraph Studio (Visualización Interactiva)

Este proyecto incluye configuración para **LangGraph Studio**, lo que permite ver el flujo de los agentes en tiempo real.

1. Abre **Docker Desktop**.
2. Abre la aplicación **LangGraph Studio**.
3. Selecciona la carpeta de este proyecto.
4. Interactúa con el agente desde el panel derecho y observa cómo se iluminan los nodos en el grafo.

## 🧠 Stack Tecnológico

* **Orquestación:** LangGraph (StateGraph, Conditional Edges).
* **LLM:** Llama 3.3 70B Versatile (vía Groq API) para inferencia de baja latencia.
* **Validación:** Pydantic (Strict Schemas para Output Parsing).
* **Observabilidad:** LangSmith (Tracing).

---

*Desarrollado como Prueba Técnica de Implementación de Agentes.*

```

```