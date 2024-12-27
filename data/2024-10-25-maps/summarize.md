Hoy quiero compartir algo fascinante que he aprendido: cómo integrar Google Maps en una aplicación Angular de una manera poco convencional. Aunque existen librerías increíbles en la comunidad para hacer esto, he decidido usar la librería creada por el equipo de Google, diseñada específicamente para Angular. Me inspiré en la implementación de Starbucks, donde vemos un mapa interactivo que muestra sus ubicaciones. Quise replicar ese efecto de interactividad, donde al hacer hover o clic en un punto del mapa, nos lleva a la ubicación específica.

Para lograrlo, trabajé en un proyecto de e-commerce que usé como ejemplo, creando una página llamada "Locations" para integrar Google Maps. En esta página, enfoqué mi atención en la integración más que en el diseño o la responsividad, utilizando Tailwind para el layout. Comencé estableciendo una lista de ubicaciones con atributos como nombre, descripción, latitud y longitud. Luego, implementé un servicio en Angular para manejar las ubicaciones y conectarme a una API que creé, la cual genera ubicaciones aleatorias cerca de un punto específico.

La clave para integrar Google Maps fue generar una API Key a través de Google Cloud Console y habilitar la API de Maps JavaScript. Después, incluí un script en el archivo index.html para cargar la API de Google Maps de manera dinámica. Utilicé un componente de Google Maps para Angular, importando el módulo necesario y configurando el centro del mapa y el nivel de zoom usando Signals, una nueva característica de Angular.

La parte emocionante fue agregar marcadores al mapa, utilizando el componente MapAdvancedMarker para cada ubicación y generando un Map ID necesario para los marcadores avanzados. Esto permitió que los puntos en el mapa se renderizaran correctamente. También implementé interacción entre la lista de ubicaciones y el mapa: al hacer clic en un marcador, se abre un InfoWindow con información detallada de la ubicación, y al hacer clic en la lista, el mapa centra el marcador correspondiente.

Aunque la documentación de este componente no es muy visible, es una herramienta poderosa y mantenida por el equipo de Angular, proporcionando una integración fluida y eficiente. Espero que esta guía te haya sido útil. Si te interesa profundizar más en esta integración, no dudes en explorar la documentación y experimentar con el código. ¡Recuerda suscribirte, dejar un like y compartir con tus amigos interesados en Angular!