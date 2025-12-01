¿Estás eligiendo tu framework de agentes de IA por moda… o porque entiendes los patrones de arquitectura que hay detrás?

En mi nuevo video cuento cómo, después de trabajar con LangGraph, Cloudflare Agents, Vercel AI SDK, Microsoft Agent Framework, Trigger, Mastra y más, llegué a la conclusión de que las herramientas cambian, pero los **patrones** se repiten. Por eso me enfoqué menos en “¿qué uso?” y más en “¿qué debo entender para poder construir buenos agentes en cualquier stack?”, apoyándome en el blogpost de Anthropic sobre agentes efectivos.

En el video recorro los patrones clave que aparecen una y otra vez al construir agentes y workflows:
- **Chaining**: dividir tareas complejas en pasos encadenados entre nodos/LLMs.  
- **Routing**: un router que deriva cada request al agente correcto (booking, FAQs, conversación general, etc.).  
- **Paralelización**: varios agentes especializados ejecutándose al mismo tiempo (por ejemplo, distintos reviewers de código) y luego un aggregator que unifica resultados.  
- **Orchestrator**: un “project manager” de agentes que decide dinámicamente qué combinación usar según la tarea.  
- **Evaluator/Optimizer**: loops donde un modelo evalúa y mejora la salida de otro hasta cumplir ciertos criterios.

También conecto estos patrones con arquitecturas tipo **ReAct (Reasoning + Acting)** y cierro con algo que como devs solemos olvidar: no siempre necesitas un grafo hipercomplejo; muchas veces un solo modelo bien diseñado, con algunas tools y un loop sencillo, es la solución más simple, barata y mantenible.

Si estás construyendo agentes, plataformas internas o centros de soporte inteligentes, este video es un mapa mental para que puedas:
- Reconocer estos patrones en cualquier framework  
- Decidir cuándo vale la pena orquestar algo complejo y cuándo no  
- Evitar la sobreingeniería y enfocarte en llevar cosas a producción

Aquí está el video completo: https://youtu.be/oR0GqQ8wMfk  

Me interesa mucho saber: ¿qué patrón estás usando hoy en tus agentes y cuál te gustaría profundizar más?