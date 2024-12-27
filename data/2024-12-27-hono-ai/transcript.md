 Bien, en este video vamos a conectar HonoJS a uno de esos modelos, a un LAR Language Model que tiene Cloudflare en su red de cómputo. Ya que al final, una vez tengamos como nuestro servicio en HonoJS, una de esas habilidades es conectarnos a uno de esos modelos que están disponibles. Y se hace súper sencillo porque casi que es como llamar a una librería. No hay que hacer mucha configuración, de por sí no hay que hacer casi ninguna configuración, un par de movimientos en nuestra aplicación. Y ya con eso podemos tener a disposición grandes modelos muy buenos que son Open Source. Entonces te estarías ahorrando costos. Por ejemplo, está LAMA, la serie LAMA 3, 3.1, 3.2, 3.3, en el cual tienen un performance muy similar a algunos a GPT-4 o GPT-3, 3.5 Turbo. Así que imagínate ya conectarte a uno de estos modelos que son Open Source y ya no tener que pagar por las inferencias de OpenAI, por ejemplo. Ese sería. Sin embargo, también hay otros modelos disponibles. En esta red, como por ejemplo Whisper para hacer transcripciones o por ejemplo Stable Diffusion para generar imágenes. Entonces podrías crear servicios en los cuales se utilicen estos modelos que realmente no tienes que configurar mucho. Y precisamente de eso se va a tratar este video. De cómo configurarlo en la red de computador Cloudflare en un ejemplo súper sencillo que es nuestro Hello World en Hono. Así que empecemos. Y vamos a conectarnos a AI. Vamos a ver si logramos conectarnos a alguno de los servicios de AI de Cloudflare, al menos en este primer GET. ¿Vale? Entonces, aquí vamos a utilizar. Vamos a ver Cloudflare. Workers. AI. Y acá está. Acá está la documentación. Básicamente lo que tengo que hacer es. Bueno, primero habilitar esto para que mi servicio tenga AI. Y luego vamos a ver algunas guías. Acá literalmente tienen varios modelos. Y hay varias cosas de IA que tiene Cloudflare. Lo más normal es que ya tiene una base de datos llamada Bitcoin. Y aquí tenemos el código de la base de datos de Cloudflare. Y aquí tenemos el código de la base de datos de Cloudflare. Y aquí tenemos el código de la base de datos de Cloudflare. Esa es la rigidez. El códigoMs era. El código Microsoft tenía el código Microsoft ha sido el que tenía la base de datos. La China acaba de salir del mercado. Como todas las preguntas de Cloudflare. Cómoмерca va viendo. No veo la<|fi|> Pues esto es todo. Monter Machado. acá acá me dan una de suma acá ya me dan una guía de modelos que están dentro de la red de cloudflare entonces vamos a decir test generation que básicamente son estos la language model y miremos acá está yema yema que es open source falcon que es open source pero yo quiero los de lama que son como los más potentes en este momento vamos a buscar lama lama acá yo quiero el ama 3.3 que fue el que lanzaron hace poquito en teoría es este este es esta el ama 3.3 y acá nos dice como nosotros lo podemos configurar en nuestro work es básicamente fíjense que acá vamos a hacer inferencia en pues en el caso literalmente yo podría instalar la enche en que es un framework para hacer como más fácil esta conexión con modelos de la language model pero ahorita creo que voy a intentar hacerlo como lo más plano posible va entonces acá hay algo que nos que si de pronto nos va a costar en cloudflare y es que cualquier configuración como variables de entorno como servicios como una base de datos como el r2 para subir archivos como este de ella todos van a venir en el contextoじゃあ acá tengo un contexto y por ejemplo acá pues voy a empezar a habilitarlo no tengo algo como un profesor punto algo punto end sino que todas商 variables de ambientes contexto y servicios vienen por el contexto no esto podría ser un poquito difícil de manejar cuando uno está acostumbrando a programación orienta objetos porque al final a que hay como muchas funciones chiquitas fuentes en otras secciones que aún no sé muy bien los lugares se enflica ahora con este wifi que van a ir Castle me parlo mas через donde pasa verdad que en donde tengo que estar pasando ese contexto bien lo primero que voy a utilizar es el baile necesito habilitar el baile y como no recuerdo muy bien pues como habilitado al baile pues me voy a guiar en en como lo hice por acá y por acá debo tener en cdc y el baile ya básicamente los baile son una forma de tipar eso en donde yo en donde se van a ir habilitando los servicios que normalmente tienen un scope y como aquí descargamos los typings de cloudflare él le va a poner como el typing adecuado al servicio bien pero básicamente él dentro de ese contexto va a recibir como una forma de distancia en donde yo pueda empezar a usar pero tengo que hacerle un typing correspondiente de por sí creo que el de ai no tiene que ser un typing correspondiente pero si yo quiero que te diga que yo voy a utilizar el de ai no tiene que ser un typing correspondiente pero si yo quiero que tenga una base de datos fíjense en este de b1 este de dónde salió de dónde salió este typing esto es de literalmente si yo voy miro es de la librería de typing que se descargó como de esto si yo declaro dentro de mis bailes una base de datos le pongo un nombre y le digo que esto es de tipo debe una base de datos de de uno pues yo pues a esto al debe uno store pues empezarle a tiene binding como tiene operaciones funciones o sea le va a tener contexto a esa base de datos bien o si tengo un jota secret excedentes toca empezar a habilitarlo de esa manera como vamos a habilitar el de ella y que por si este y commerce no tiene ella pero déjenme este de las entrevistas en mi aplicación de entrevistas si tiene habilitado y hay y creo que hay hasta donde lo vimos no tenía typing entonces eso sí toca literalmente ponerle un n ni a menos que ya haya algo aunque parece que sí que ya hay typing a ver este viene a mira que si ya tiene antes ya no entonces acá tener el ron tiene tiene varias cosas que ya que ya podríamos usar fíjense que ya ha cambiado antes no tenía typing normalmente estos type in span aumentando entonces ahora literalmente el servidor ya tiene el servidor ya está con el software ya que esta El servicio de AI ya tiene typing y por ende me va a ayudar un montón a desarrollar, que es como la forma de habilitar el servicio. Entonces, ¿qué hay que hacer ahí? Pues básicamente algo que tengo que hacer es habilitar ese binding con contexto. Entonces, aquí básicamente lo que vamos a hacer es utilizar los bindings. Entonces, déjenme ver. Ah, sí, este app binding. Tenemos que crear, normalmente yo creo un archivo llamado types. Types.typescript. Y le digo app. Normalmente ahí pueden haber variables o el binding. Entonces, aquí todavía no tengo variables. Entonces, simplemente voy a poner el binding. Y el binding lo importo, pues, del archivo bindings. Y el binding.typescript. Listo. Entonces, ahí ya está. Este creo que debería ser .com. Listo. Ahora, esa aplicación, ahora sí yo construyo la aplicación con base a esa, pues, como para que esté typeado de esa forma. Entonces, básicamente lo que yo le digo aquí es que esta app tiene un typing específico. ¿Cuál va a ser? Pues la de app. Y esa app ¿de dónde viene? De types. Bien. Entonces, ahora solo componerle este app. Ahora, en teoría, esto debería tener ahora sí contexto de ese servicio. Entonces, si yo le digo. Déjame ver qué tal. Vamos a ver si sí lo toma. Aquí como que el cursor me dice eso debería estar en .get, pero parece que no. Si no, no tuviéramos error de typing. Pero déjenme ver. Aquí cómo fue que yo hice esa. Ah, ya. Creo que fue. Así. New AI. Y esa AI ¿viene de dónde? Creo que viene de Cloudflare. Creo que ese New AI viene de Cloudflare. Déjame ver la documentación. Aquí. Aquí. ¿Dónde está? Aquí. Ese m.ai. Acá fíjense que es donde sale el m.ai y ahí corre en ese run. Eso es lo que quiero empezar a hacer. Pero acá corre del contexto. A ver, vamos a ver. Ay. Ok. C.emp. Debería estar ahí. Ah, mira, creo que este es el punto. Sí, ahí está. .run. Ese es. Ahí tenía ese error. Simplemente ya está dentro del contexto .run y ahí debería empezar a funcionar, en teoría. Si no, lo que me toca hacer es crear la estancia, pero no hay problema. Listo. Entonces ahora nos dicen cómo es la forma en que yo tengo que llamar. Entonces tengo que decirle. Ok. El modelo al que tengo que llamar. Entonces acá run. Y luego me dice, pues como cualquier lar language model, me dice que tengo que tener pues un mensajes y ese tipo de cosas. No. No, creo que el cursor me está autocompletando mal. No quiero que me autocomplete así. Ya, exacto. Parampán. Acá run. Esto es un await, sí. Entonces esto lo ponemos de forma síncrona. Y sí, podríamos tener el respuesta y acá el test response. Lo que no sé es por qué acá me dice que este modelo me dice que no existe. Run. Acá es el modelo. Como que no lo toma, como que este modelo pareciera que no. A ver si así lo copié bien. Normalmente uno puede entrar aquí. Hasta donde yo vi y ver qué modelos están. Mira, acá está el de Q. Ya está el de Q. Eso es interesante que esté un modelo como Q aquí en la red de Cloudflare. Está interesante. Déjenme ver. BSI. Creo que no está el 3.3. Qué raro. A ver, entonces voy a escoger este. El de meta 3.1. Está Lama. Mistral. El de Google de Yema. Bueno, al parecer creo que todavía no está el 3. Entonces. Ah, mira, sí creo que es error de typing. Voy a escoger ese, Lama 3.1. Ok. Y veamos el response. Acá vamos a ver los mensajes. Mensajes de sistema, mensajes de rol. Rol. User content. Acá está Hello World. Él debería contestarme. Y el response creo que es directo. Creo que es. Déjenme ver esto que me devuelve. Punto. Ah, claro, esto debería ser un JSON, creo. Ya. Vamos a responder ese JSON directo. Aunque me da curiosidad que tiene este. Que devuelve esto. Esto es una promise. Ok. Con response. Qué raro que. No creo que es el texto directo. A ver, prueba, prueba. Entonces. Ya. Entonces, bueno, aquí literalmente lo que voy a decir es que cada vez que yo le haga un impunt aquí. Pues le diga como que me haga un chiste. Te doy un media joke. Basado en el modelo de Lama 3.1. Y de nuevo, acá tienen varios modelos. Creo que aquí lo que habría que hacer para que me acepte. Eh. Pues modelos más actualizados. Creo que hay que configurar. Qué versión de los workers hay. Vamos a ver si este se descargó una. Podríamos actualizarlo porque a veces es solo el typing. O sea, no es que realmente el modelo no esté, sino que no está en la versión de typing que se es que uno selecciona. Entonces uno podría decir a ver esto, por ejemplo, fue publicado hace seis días. Entonces yo podría decir que quiero esta versión en específico. Me tocaría reinstalar dependencias. En el PMI. Para que restale esa dependencia. Bueno, entonces a ver. Creo que la actualizó. Entonces en el PMI. Este. Y le digo esa versión en específico. Con. No hay. O sea que me descargue esa versión en específico. Ya y vamos a ver si ahora sí encuentra. Si ya. Hay otros modelos. A ver. Lama no. No, no, todavía no. Miren que puedo acceder a Whisper para hacer traducciones. Bueno, qué raro que no esté aquí el de Lama. Bueno, el de Lama 3.3. Luego vamos a mirar por qué o si toca activar alguna cosa más. Pero veamos si funciona apenas este. Dice que este debería ser System. Bueno, no, User está bien. User, pongámoslo bien. Y ahora cuando yo haga un Get, pues debería contarme un chiste. Vamos a hacer un primer one def. Primero lo va a probar aquí en local. A ver si todo funciona. Bueno, acá me sale un warning. Y es que cuando yo estoy utilizando Workers de AI, pues al final. Dónde se está, o sea, en local no está el modelo de Lama. Entonces ellos le tocan conectarse, pues a. Pues al modelo y a su Edge. Entonces yo tengo que decirle la forma de conectarse. Creo que hay que darle Remote para que se pueda conectar. Veamos si. Acá sale algún error. Sí, probablemente aquí salga un error. Y me diga. Ah, no, mira, acá me salió todo bien. Mira, aquí tengo un. Un chiste. A ver, le voy a decir que sea en español. En Spanish. Listo. Entonces acá lo cambio. Esto es Load. Recargo. Vamos a ver si ya recarga. Demora un poquito más porque me imagino que se está conectando a la red de Edge de Cloudflare. A ver. Acá dice, claro, un hombre entra. Bueno, en fin, a una barbería. Le dice al barbero. Un poquito menos. A ver. Un hombre entra a la barbería. Le dice al barbero. Hazme su truco. ¿Qué? Manteniendo en mi viaje de negocios. El barbero dice. Tres chill party. Bueno, no sé. Está raro ese chiste porque es divertido. Puedo explicar. Bueno, acá está raro ese chiste. Pero lo importante es que tenemos una respuesta de un LAR Language Model y también sabemos. Y que literalmente no nos tocó desplegar un modelo, etcétera. Literalmente ya solo por utilizar uno de ellos como un framework que podemos conectar. Y que lo que tenemos que hacer es correrlo en la red de Cloudflare de Cloudflare Workers. También de Deno. De Dino. Obviamente, si yo ya corro esto en Dino, en el servidor de Fastify, de Vercel, pues esto no tiene sentido. ¿Por qué? De nuevo, esto tiene sentido porque me estoy conectando a la red de Cloudflare donde hay estos modelos. Aunque hay una manera de habilitar que yo pueda en cualquier API de Node o lo que sea con el AI Web Gateway, conectarme a modelos y utilizar simplemente a Cloudflare como inferencia, como un código de referencia. O como hosting, digamos, de modelos en los cuales simplemente le hago una petición y lo devuelvo. Pero aquí, pues ya estando en la red de Cloudflare, pues simplemente lo estoy utilizando. Obviamente, este modelo parece no estar muy bueno. Podríamos probar otro como un Mistral. A ver, veamos qué otros modelos están acá. Meta... Creo que... A ver... En teoría, estos deberían ser muy buenos. Porque son casi la competencia de JTPT4. ¿Por qué? Porque son ya JTPT4. A ver... Y no sabía que estaban ya disponibles en Cloudflare. Veamos, cambiamos el modelo. Y... Intentamos. Entonces, vamos a ver acá. Vamos a hacer un repuesto. Ahí se está demorando. Aquí tiene... Aquí parece que está mejor. ¿Sabes qué? Quisiera devolver esto como text. A ver... Punto response al final es, ¿no? Punto response. Que no está tan bien. ¿Qué pasa? Que no está tan bien. ¿Qué pasa? Que no está tan bien. ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? ¿Qué pasa? Que no está... Que no está... Con el correcto typing. Entonces, por eso me salió un error. Me dice como, hey, yo no conozco... No hay nada que diga response. Entonces, me va a tocar hacer un hat aquí. Como... LLM response. Y decirle que esto sea en. Que es una mala práctica en teoría, pero pues si no me dan el typing, tampoco me dejan mucha opción. Y... Ya. Vamos a ver. Y... ¿Qué pasa? Que no está tan bien. ¿Qué pasa? Que no está tan bien. Que no está tan bien. Debería responderlo en texto. Eso. Hola, aquí tienes una pequeña broma española. ¿Qué hace una abeja en el gimnasio? Zumba. Ya, ya, ya. No, no. Mejor se vea a mí por el chiste. Es el chiste de la language model. Ok. Vamos a hacer el deployment de eso. Entonces, vamos a ir aquí a la terminal. Y... Voy a cerrar. Listo. Y en teoría, hago en la terminal. Y... Voy a cerrar. Y... Listo. Y en teoría, hago en la terminal. Y... Listo. Y... Listo. Y en teoría, hago en la terminal. Y... Listo. Y en teoría, hago en la terminal. Run deploy. Vamos a ver que no se pierda el dominio. Porque creo que tocaba configurarlo. Pero, vamos a ver qué pasa. Entonces, ahí ya lo que hizo fue. ¿Qué hicimos? Bueno, pues obviamente ya estando en la red de computadores de Cloudflare, estamos usando Cloudflare y su red de modelos que ya están puestos en esa red. Por ende, podemos como que llamarlos. Se vuelve casi como una librería, ¿no? Como cuando importas lojas, Shunderscore, etc. Moment.js, State Functions, cualquier librería. Al estar dentro de la red de computadores de Cloudflare, tienes estas habilidades. Aparte de la habilidad genial de Edge Computing, que esa la tiene Versa, Fastify, Boom, etc. Cloudflare tiene una red en donde tiene modelos ya dispuestos para empezarles a hacer cosas. Entonces, ya podría empezar a hacer, obviamente, acá es algo muy, muy chiquito. Es cuéntame un chiste en español. Pero realmente yo podría ya subir un pie. Yo podría ya subir un PDF y que me haga el resumen del PDF o cosas ya avanzadas que en este momento ya hacen los language model. Y normalmente los modelos que están acá son los modelos que son open source. Entonces, vemos los modelos de Whisper, de OpenAI, que OpenAI lanzó esos modelos open source. Los de Lama, hasta donde yo sabía, ya habían puesto el 3.3 de Lama. No sé por qué ahorita no me lo está jalando bien. Luego averiguo por qué. Pero estaban diciendo en el Twitter de Cloudflare que ya podíamos probar. La versión de Lama 3.3. Que un Lama 3.3 es casi comparable a un GPT-4 en cierto punto. Tenemos Mistral. Esto no sé cuáles son. TheBlock. Gema. Gema, el modelo open source de Google, etc. Los de Microsoft. Tenemos bastantes. Bueno, acá en teoría, pues ustedes ya ven toda la... Pues los que hay. En teoría son todos... Estos que hay. Acá me dicen que literalmente ya estaba el 3.3. No nos funcionó. Luego vamos a ver por qué. Pero en fin. Pero literalmente pues tenemos estos modelos y ustedes ya los pueden filtrar. Por quienes hacen buena... Bueno, todas las language model hacen tareas como de extracción, de resumen. Pero, por ejemplo, podríamos tener... Hay modelos de generación de imágenes. Es más, aquí tienen un modelo, un flux open source. Tienen un stable diffusion para... Imagínense, o sea, desplegar un modelo de stable diffusion es complejo. O sea, necesitaríamos un servidor que tenga GPUs. Necesitaríamos, pues, tener unos conocimientos. Normalmente necesitamos que ese modelo simplemente esté para hacer inferencia. Obviamente, servidores como Amazon, modelos como Azure, ya tienen también este tipo de modelos. En los cuales nosotros también podríamos... Si uno va al AI Azure Studio. Y... También ellos ya tienen muchos modelos que casi muy similar. Si desplegas en Azure, pues entonces como que tienes ya acceso a ciertos modelos que están en la nube. Pero por ahora me parece que Cloudflare es como sencillo para desarrolladores. Y en unas pocas líneas de código ya tengo este tipo de acceso. Déjame ver si ya hizo deploy. Acá se hizo deploy. Vamos a ver si yo entro a este dominio. ¿Y cómo es el get? Sería, pues, contar un chiste. Y ahí está. Obviamente cada vez que hagan un refresh va a contar un chiste nuevo. Vamos a ver este. Claro que tienes una vertebroma en español. ¿Qué hace un perro en el gimnasio? Mueve el pato. Ok. Ahora, acá me hacen la explicación del chiste. Si se explica el chiste dicen que es malo. Veamos si todavía funciona en mi dominio. HononicoBytes.com Aunque se demora. La inferencia no debería ser tan larga. Qué raro que se demore. Pero bueno, ahí dice. ¿Qué hace una abeja en el gimnasio? Zumba. Este me lo repitió. A ver, yo quiero que me cuente otro. Aunque Cloudflare es muy buena haciendo caché. Entonces a veces puede que cachee la respuesta. ¿Por qué los perros siempre están contentos en el parque? Porque allí tienen... Perra... No, no entendí el chiste. Pero ok. Ok. En fin. No, en fin. Acá hay modelos interesantes que podemos inferir. Y listo. Pues literalmente fíjense que en unas pequeñas líneas. No solo vimos Hono.js. Vimos un poquito de Cloudflare. Cómo desplegar en Cloudflare. Y utilizar una de esas habilidades que hay en Cloudflare. Que es utilizar sus modelos que están ahí en la misma red. Que ya los puedo llamar directamente desde el código. Con estas pequeñas líneas de código. Básicamente hicimos una aplicación. De código. Una aplicación súper sencilla. Que tiene un get para ello Tuvimos que habilitar el biding. Casi que así se van habilitando los servicios. Para que luego tengan el typing correcto. Y básicamente luego, Creamos el type-app. Y aquí es donde le pusimos esa app. Para que tenga contexto. Normalmente todo eso sale del ZEB.Emb. Y luego ya encuentro el servicio de EAI para que vaya a la inferencia de un modelo como tal. Entonces... Espero te haya gustado este video, que te suscribas a este canal, que me cuentes más si ya sabías acerca de Cloudflare, si sabías acerca de Hono y si quieres aprender mucho más de él. Así que te espero y suscríbete en este canal.