
from langchain_core.prompts import ChatPromptTemplate
from src.models import AgenteState, ListaTareas
from src.groq_config import llm

def nodo_analizador(state: AgenteState):
    print(f"--- (GROQ) AGENTE 1: ANALIZADOR ---")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente experto en extracción de datos. "
                   "Analiza el texto y extrae una lista de tareas estructurada. "
                   "Si no se menciona duración, asume 1 hora. "
                   "Responde SOLO con el JSON."),
        ("user", "{input}")
    ])
    
    estructurador = prompt | llm.with_structured_output(ListaTareas)
    
    resultado = estructurador.invoke({"input": state["input_usuario"]})
    return {"tareas_estructuradas": resultado.tareas, "revisiones": 0}

#El pipeline lo que hace en el fondo es :
"""
prompt_value = prompt.invoke({
    "input": state["input_usuario"]
})

respuesta_llm = llm.invoke(prompt_value)

resultado = parser.invoke(respuesta_llm)

el estructurador es la combinacion de estos tres pasos, cuando se ejecuta invoke, se ejecutan los tres pasos de forma secuencial, pasando el resultado de cada paso al siguiente. Esto simplifica mucho el código y hace que sea más fácil de leer y mantener.

suponiendo que todos los pasos son funciones, esto seria bsicamente lo que hace el pipeline:

pipeline = [paso1, paso2, paso3]

entrada = "Estudiar Python 2 horas"
output = entrada

for step in pipeline:
    output = step(output)

print(output.tareas)
"""