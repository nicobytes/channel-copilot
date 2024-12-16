Hoy quiero hablarles sobre una nueva primitiva que trae Angular en su versión 19, llamada Linking Signal. Esta herramienta es una mejora para manejar señales computadas de manera más organizada y completa. A menudo surge la confusión sobre cuándo utilizar un Computer Signal y cuándo un Linking Signal. En este video, presento un ejemplo práctico para aclarar estas dudas.

Imaginemos un componente sencillo, como un Dropdown Component, que tiene un Signal llamado Options, que es un array de strings. Inicialmente, configuramos opciones por defecto como "Opción 1", "Opción 2" y "Opción 3", y las renderizamos en el HTML. Luego, exploramos cómo manejar la selección de opciones y almacenar su estado usando un Signal llamado selectedOption.

El desafío viene cuando queremos introducir reactividad, como cambiar el conjunto de opciones de manera dinámica. Aquí es donde Linking Signal cobra sentido, ya que permite definir fuentes o señales de las que depende, similar a un computed, pero con la capacidad adicional de ser reescribible. Antes de su introducción, una alternativa era usar un effect, que no es la práctica más recomendada por el equipo de Angular.

El LinkedIn Signal facilita la manipulación reactiva de señales, evitando efectos innecesarios y mejorando la legibilidad del código. Aunque aún está en fase de vista previa y podrían surgir errores de tipado, ofrece una solución más pura y nativa para manejar estados reactivos en Angular.

Con este LinkedIn Signal, podemos establecer lógica de negocios reactiva, como seleccionar automáticamente una opción por defecto cuando hay datos, o manejar adecuadamente un array vacío. Esto nos permite programar de manera más eficiente y evitar malas prácticas con effects.

Espero que esta explicación haya sido útil y los invito a suscribirse al canal para más actualizaciones y noticias sobre Angular.