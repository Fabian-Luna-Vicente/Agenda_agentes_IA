from langgraph.graph import StateGraph, END
from src.models import AgenteState
from src.nodes.analizer_node import nodo_analizador
from src.nodes.evaluator_node import nodo_evaluador
from src.nodes.persistence_node import nodo_guardar_archivo
from src.nodes.planifier_node import nodo_planificador
from src.routers.evaluator_router import router_evaluacion


# Construcción del grafo
workflow = StateGraph(AgenteState)

# Añadir nodos
workflow.add_node("analizador", nodo_analizador)
workflow.add_node("planificador", nodo_planificador)
workflow.add_node("evaluador", nodo_evaluador)
workflow.add_node("guardar", nodo_guardar_archivo)

# Definir flujo
workflow.set_entry_point("analizador")
workflow.add_edge("analizador", "planificador")
workflow.add_edge("planificador", "evaluador")

workflow.add_conditional_edges(
    "evaluador",
    router_evaluacion,
    {
        "reintentar": "planificador",
        "finalizar": "guardar"
    }
)

workflow.add_edge("guardar", END)

# Compilar
app = workflow.compile()