
from langchain_core.prompts import ChatPromptTemplate
from src.models import AgenteState, ListaTareas
from src.groq_config import llm

def nodo_analizador(state: AgenteState):
    print(f"--- ⚡ (GROQ) AGENTE 1: ANALIZADOR ---")
    
    # Truco Pro: A veces Llama 3 necesita ejemplos más explícitos en el system prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente experto en extracción de datos. "
                   "Analiza el texto y extrae una lista de tareas estructurada. "
                   "Si no se menciona duración, asume 1 hora. "
                   "Responde SOLO con el JSON."),
        ("user", "{input}")
    ])
    
    # Groq soporta 'with_structured_output' nativamente con Llama 3
    estructurador = prompt | llm.with_structured_output(ListaTareas)
    resultado = estructurador.invoke({"input": state["input_usuario"]})
    return {"tareas_estructuradas": resultado.tareas, "revisiones": 0}