**Resumen en primera persona:**  

¡Hola a todos! En este video, les mostré cómo integrar un modelo de lenguaje como GPT-4 de OpenAI en Landgraf, nuestro sistema de grafos para crear agentes multiagentes. Después de explorar los fundamentos de Landgraf en videos anteriores, como los nodos lineales y los Conditional Edges, era hora de dar el salto a la inteligencia artificial generativa.  

Primero, usé Langchain como puente para conectarnos de manera flexible a modelos como GPT-4, Mistral o LLaMA. Instalamos la librería `langchain-openai` con Poetry, configuramos la API key de OpenAI en un archivo `.env` y verificamos que todo funcionara correctamente. ¡Importante: nunca compartan sus claves en público! Luego, construí un grafo simple con un solo nodo que maneja mensajes, heredando de `MessageState` para gestionar el historial de la conversación.  

Aquí viene lo interesante: añadí un *system prompt* para definir el rol del asistente como experto en Angular, evitando que se desvíe a otros temas. Aprendí que concatenar arrays de mensajes correctamente es clave (¡Python lo hace fácil con el operador `+`!). Después de ajustar errores y probar el sistema, vimos cómo el modelo responde coherentemente, incluso rechazando preguntas sobre React para mantenerse enfocado en Angular.  

Finalmente, demostré cómo Landgraf y Langchain funcionan juntos para crear sistemas escalables, con la posibilidad de agregar más nodos, funciones personalizadas y conexiones a otros modelos en el futuro. Si quieren profundizar en agentes más complejos o *function calls**, ¡suscríbanse para no perderse los próximos tutoriales!  

**¡Los invito a probar este ejemplo y compartir sus resultados en los comentarios!** 🚀 ¿Qué temas les gustaría ver en próximos videos? 👇