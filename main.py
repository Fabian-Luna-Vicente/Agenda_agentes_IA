from src.graph import app

if __name__ == "__main__":
    prompt_usuario = """
    Hola IA, necesito organizar mi semana.
    1. Preparar el Q3 report (Prioridad Alta, Energía Alta). No sé cuánto dura, calcúlalo tú.
    2. Ir al dentista el martes por la tarde (2 horas, energía media, personal).
    3. Estudiar Rust (Energía alta, quiero dedicarle 10 horas en total en la semana).
    4. Pasear al perro (Todos los días, 30 min, energía baja).
    """

    print("🚀 INICIANDO SISTEMA DE AGENTES (Powered by Groq)...")
    

    resultado = app.invoke({"input_usuario": prompt_usuario, "revisiones": 0})
    
    print("\n" + "="*50)
    print(f"📂 RESULTADO FINAL GENERADO: {resultado['archivo_generado']}")
    print("="*50)
    
    # Imprimimos un resumen en consola para verificar
    plan = resultado["plan_semanal"]
    if plan:
        for dia in plan.plan:
            tareas_nombres = [t for t in dia.tareas_asignadas]
            print(f"\n📅 {dia.dia}:")
            print(f"   Tareas: {', '.join(tareas_nombres)}")
            print(f"   📝 Razón: {dia.razonamiento}")
    else:
        print("❌ Error: No se generó un plan válido.")