from langchain_core.prompts import ChatPromptTemplate
from src.models import AgenteState, PlanSemanal
from src.groq_config import llm

def nodo_planificador(state: AgenteState):
    print(f"--- ⚡ (GROQ) AGENTE 2: PLANIFICADOR ---")
    
    tareas_txt = "\n".join([f"- {t.nombre} ({t.duracion_horas}h, E:{t.energia_requerida})" for t in state["tareas_estructuradas"]])
    feedback = state.get("feedback", "Ninguno")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto en planificación. Crea un horario semanal (Lunes-Viernes). "
                   "Reglas: Max 8h/día. Tareas 'alta energía' por la mañana. "
                   "Si hay feedback previo, CORRIGE el plan según lo indicado."),
        ("user", f"Tareas: {tareas_txt}\nFeedback anterior: {feedback}")
    ])
    
    planificador = prompt | llm.with_structured_output(PlanSemanal)
    resultado = planificador.invoke({})
    
    return {"plan_semanal": resultado}