from typing import List, TypedDict,Optional
from src.models import Tarea,PlanSemanal

class AgenteState(TypedDict):
    input_usuario: str 
    
    # Lista estructurada de objetos Tarea (Memoria del Agente 1)
    tareas_estructuradas: List[Tarea] 
    
    # El plan propuesto (Memoria del Agente 2)
    plan_semanal: Optional[PlanSemanal] 
    
    # Feedback del evaluador (Memoria del Agente 3)
    feedback: Optional[str] 
    
    revisiones: int 
    
    archivo_generado: str