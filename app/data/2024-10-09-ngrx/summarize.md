Hoy quiero compartir cómo manejar el estado global o local de los componentes en Angular usando un paquete ligero llamado ngRx Signals. Esta herramienta aprovecha la nueva reactividad en Angular y ofrece una solución más simple y declarativa en comparación con Redux, evitando el exceso de boilerplate.

El manejo del estado en aplicaciones web suele presentar desafíos, especialmente cuando se trata de comunicación entre componentes anidados, un problema conocido como Prop Drilling. NgRx Signals aborda este problema permitiendo que los componentes se suscriban a partes del estado de interés y reaccionen de forma automática a los cambios sin recorrer todo el árbol de componentes.

NgRx Signals es parte de la familia de paquetes ngRx, pero se destaca por su simplicidad. A diferencia de ngRx Store, que requiere múltiples archivos y configuraciones, este paquete permite definir el estado, los estados derivados y los métodos de modificación en un solo lugar, haciendo que el mantenimiento sea más sencillo.

Para comenzar, instalamos ngRx Signals en nuestro proyecto Angular. Luego, definimos un archivo de store para manejar el estado local o global del componente. Este archivo actúa como un servicio inyectable que maneja el estado inicial, los estados derivados mediante `withComputed`, y los métodos de modificación del estado con `withMethods`.

Además, podemos integrar servicios que manejan datos externos, como APIs, directamente en los métodos del store. Esto nos permite estructurar nuestra aplicación de manera que los componentes se centren en la representación visual y el store en el manejo del estado y la lógica de negocio.

NgRx Signals también permite tener múltiples stores, rompiendo el patrón tradicional de un único store en Redux. Esto ofrece flexibilidad para manejar estados locales de componentes individuales o estados globales para toda la aplicación, según las necesidades.

En resumen, ngRx Signals simplifica el manejo del estado en Angular, ofreciendo una solución ligera y efectiva que aprovecha el modelo de reactividad de Signals. Es especialmente útil para quienes buscan reducir el boilerplate y mejorar la organización del código en aplicaciones complejas. Si estás interesado en mejorar el manejo del estado en tus proyectos Angular, te recomiendo probar ngRx Signals.