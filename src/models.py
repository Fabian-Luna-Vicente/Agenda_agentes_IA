from typing import List, Literal, Optional, TypedDict
from pydantic import BaseModel, Field

class Tarea(BaseModel):
    nombre: str = Field(description="Nombre de la tarea")
    duracion_horas: float = Field(description="Duración estimada en horas")
    prioridad: Literal["alta", "media", "baja"]
    energia_requerida: Literal["alta", "media", "baja"]
    tipo: Literal["trabajo", "estudio", "personal"]

class ListaTareas(BaseModel):
    tareas: List[Tarea]

class PlanDiario(BaseModel):
    dia: str
    tareas_asignadas: List[str]
    razonamiento: str

class PlanSemanal(BaseModel):
    plan: List[PlanDiario]

class Evaluacion(BaseModel):
    status: Literal["APROBADO", "RECHAZADO"]
    comentarios: str

class AgenteState(TypedDict):
    input_usuario: str
    tareas_estructuradas: List[Tarea]
    plan_semanal: Optional[PlanSemanal]
    feedback: Optional[str]
    revisiones: int
    archivo_generado: str