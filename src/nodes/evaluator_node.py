from langchain_core.prompts import ChatPromptTemplate
from src.models import AgenteState, Evaluacion
from src.groq_config import llm

def nodo_evaluador(state: AgenteState):
    print(f"--- ⚡ (GROQ) AGENTE 3: EVALUADOR ---")
    
    plan_json = state["plan_semanal"].model_dump_json()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Revisa el plan semanal. "
                   "Si un día tiene >8 horas o lógica ilógica, RECHAZA y explica por qué. "
                   "Si es viable, APRUEBA."),
        ("user", "Plan a revisar: {plan_para_evaluar}") 
    ])
    evaluador = prompt | llm.with_structured_output(Evaluacion)
    decision = evaluador.invoke({"plan_para_evaluar": plan_json})
    
    if decision.status == "APROBADO":
        return {"feedback": None}
    else:
        return {"feedback": decision.comentarios, "revisiones": state["revisiones"] + 1}