**Version mejorada**

Si trabajas con RAG, agentes o knowledge bases, la calidad del Markdown de entrada importa más de lo que parece.

En este video comparé dos opciones para convertir PDF a Markdown: la solución de Cloudflare, que yo venía usando, y PDF Inspector, una alternativa open source de Firecrawl. Probé ambos con PDFs densos, documentos simples, CVs y archivos con muchas tablas.

Mi conclusión: en documentos básicos los dos cumplen, pero PDF Inspector entrega un Markdown más limpio, mejor organizado y mucho más útil en la práctica. La diferencia más clara apareció en las tablas, donde Cloudflare suele fallar o perder estructura, mientras que PDF Inspector las recupera bastante mejor. Si el Markdown sale bien desde el inicio, luego hace falta menos postproceso para usarlo en sistemas de AI.

Además, PDF Inspector es gratis, open source y fácil de integrar con Python, Node, Rust o incluso WebAssembly. Si ya estás en Cloudflare, su opción sigue siendo cómoda. Pero si tu foco es extraer PDF a Markdown con buena calidad, yo le daría una oportunidad seria a PDF Inspector.

¿Has probado otras herramientas para este flujo?

**Hashtags**
#AIEngineering #RAG #LLM #OpenSource #DeveloperTools

**Opcional - Variante alternativa**
Convertir PDF a Markdown parece un detalle menor, hasta que quieres usar ese contenido en RAG o una knowledge base.

En este video puse a prueba Cloudflare y PDF Inspector de Firecrawl con varios tipos de PDFs: documentos simples, archivos densos, currículums y tablas. En lo básico, ambos funcionan. Pero en calidad de salida, PDF Inspector me dejó mejor impresión: Markdown más limpio, mejor estructura y una vista previa más clara.

El punto decisivo fueron las tablas. Ahí Cloudflare pierde bastante contexto o formato, mientras que PDF Inspector logra una extracción mucho más útil. Y eso, para pipelines de AI, importa mucho: cuanto mejor entra el contenido, menos trabajo hay después.

Además, PDF Inspector suma otro punto fuerte: es gratis, open source y fácil de integrar en distintos stacks. Si ya usas Cloudflare, su alternativa sigue siendo práctica. Pero para este caso de uso puntual, PDF Inspector me parece más conveniente.

**Hashtags**
#RAG #Markdown #AIEngineering #Firecrawl #PDFProcessing