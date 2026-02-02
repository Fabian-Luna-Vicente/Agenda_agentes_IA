from src.models import AgenteState


def router_evaluacion(state: AgenteState):
    feedback = state.get("feedback")
    revisiones = state.get("revisiones", 0)

    if feedback and revisiones < 3:
        print(f"   🔄 Bucle detectado: Intento {revisiones + 1}/3. Volviendo a planificar...")
        return "reintentar"
    

    elif feedback and revisiones >= 3:
        print("   ⚠️ Límite de revisiones alcanzado. Guardando mejor esfuerzo.")
        return "finalizar"

    else:
        print("   ✅ Plan aprobado por el evaluador.")
        return "finalizar"