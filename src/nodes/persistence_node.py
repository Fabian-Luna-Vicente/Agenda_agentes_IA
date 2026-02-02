import json
import os

from src.models import AgenteState


def nodo_guardar_archivo(state: AgenteState):
    print("--- 💾 NODAL FINAL: GUARDANDO ARCHIVO ---")
    
    # Extraemos el plan del estado. Como es un objeto Pydantic, usamos .model_dump()
    plan_data = state["plan_semanal"].model_dump()
    
    # Definimos el nombre del archivo (podría ser dinámico basado en fecha)
    filename = "plan_semanal_final.json"
    
    # Escribimos en disco. 
    # 'ensure_ascii=False' es CRÍTICO para que las tildes y ñ se lean bien.
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(plan_data, f, indent=4, ensure_ascii=False)
        
    return {"archivo_generado": os.path.abspath(filename)}