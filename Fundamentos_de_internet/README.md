# Fundamentos de Internet 

## 1. Del Cliente al Servidor

1.1 Qué hace el cliente (navegador).
Cuando el usuario escribe www.youtube.com y presiona Enter, el navegador interpreta la dirección, busca la dirección IP del servidor mediante el DNS y establece una conexión para solicitar la página web. Después, recibe la información del servidor, la procesa y muestra el contenido en pantalla. Cuando el usuario selecciona un video, el navegador solicita los datos necesarios para reproducirlo.

1.2 Qué papel cumple el DNS.
El DNS interpreta los nombres de dominio ejemplo: www.youtube.com y lo que devuelve es una direccion IP de 32 bits. En otras palabras traduce el dominio a direccion IP.

1.3 Qué ocurre con la dirección IP.
El DNS devuelve una dirección IP correspondiente a un servidor de YouTube. Con esta dirección, el navegador puede localizar el servidor al que debe conectarse.

1.4 Qué hace el servidor.
El servidor recibe la solicitud, procesa la petición y envía los recursos necesarios para mostrar la página, como textos, imágenes y videos.

1.5 Cómo entra en juego el protocolo HTTP/HTTPS.
El navegador utiliza el protocolo HTTPS para comunicarse de forma segura con YouTube. Este protocolo cifra la información que se intercambia entre el cliente y el servidor, protegiéndola durante la transmisión.

ver imagen
![Imagen proceso del cliente al servidor](https://github.com/JavierFallas6/Ejercicios_Lyfter/pull/10)

## 2. Frontend y Backend en acción

2.1 Indique qué parte del sistema correspondería al frontend y cuál al backend.
Frontend: Es la parte visual de sistema con la que interactúa el usuario. En una app donde se permite registrarse, consultar horarios disponibles, seleccionar un médico y reservar una cita.
Backend: Es la parte que funciona detrás del sistema. Se encarga de procesar las solicitudes, verificar la disponibilidad de los médicos, guardar las citas en una base de datos y validar la información ingresada.

2.2 Mencione tres tecnologías posibles para cada uno.
Frontend: HTML, CSS, Javascript
Backend: Python, java, Node.js

2.3 Explique brevemente cómo el frontend se comunicaría con el backend (mencione los conceptos de API, HTTP y request/response).
Request: el frontend envía al backend los datos de la cita, como el nombre del médico, la fecha y la hora, mediante una petición HTTP a través de una API.
Procesamiento: el backend verifica que el horario esté disponible y guarda la cita en la base de datos.
Response: el backend devuelve una respuesta al frontend indicando si la cita se reservó correctamente o si ocurrió algún error.
Resultado: el frontend muestra un mensaje al usuario confirmando la cita o informándole que debe seleccionar otro horario.


## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|-----------------------|------------------------------|----------------------------------|
| REST        |        Json            |      Alta             |Baja                          |Alta                              |
| SOAP        |        XML             |      Baja             |Alta                          |Media                             |
| GraphQL     |       Json             |   Muy Alta            |Media-alta                    |Alta                              |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
De lo que he leido veo mas apropiado REST por que utiliza un formato de datos que es usado regularmente o se tiene mas conocimient (Json), ademas de que es facil de implentar y que su uso actual es Alto, lo cual se traduce a que debe tener mas documentacion sobre como hacerle un uso apropiado.

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:**
Pokedexes

- **Descripción:**
ofrece una encyclopedia de pokemones donde se registra informacion como: nombre del pokemon, si el pokemon pertenece a la seria de video juegos originales o no, un catalogo de regiones de los pokemones (no era tan fanatico de pokemones entonces no estoy familiarizado a que se refere con la region). tambien una descripcion en diferentes lenguajes. ademas de la version del juego al que pertenece el pokemon.

### 4.2 Configuración en Postman
- **Nombre de la colección:**
PokeApi - Contest Types.postman_collection

- **Solicitudes agregadas:**
  - GET - GET - Contest Types
  - POST - This is a consumption-only API — only the HTTP GET method is available on resources.
  - PUT/PATCH/DELETE - This is a consumption-only API — only the HTTP GET method is available on resources.

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint | Código de estado | Notas |
|-----------|--------|----------|------------------|-------|
|           |get     |  Contest Types              |200 OK |    Muestra la informacion del pokemon contest type   |
|           |get     |  Super Contest effect       |200 ok |    Son el tipo de efecto que se usan durante competencia   |
|           |get     |  Contest effect             |200 ok |    Se refiere a los movimiento durante el efecto   |

### 4.4 Explicación técnica
Yo seleccione la de Contest, la cual analiza el peso de cada pokemon para asignarlo en las batallas. los tipos de efectos que se usan y los movimientos. 
#### [PokeApi - Contest]
- **Método HTTP:**
get
- **Endpoint:**
Contest Types (endpoint), Contest Effects (endpoint), Super Contest Effects (endpoint)
- **Parámetros / body:**
https://pokeapi.co/api/v2/contest-type/1/, https://pokeapi.co/api/v2/contest-effect/3/, https://pokeapi.co/api/v2/super-contest-effect/4/
- **Descripción de la respuesta:**
No me queda muy claro que debo de poner en esta seccion.
**¿Qué aprendiste del proceso?**
Me parece super vacilon el proceso es basicamente un query tipo SQL para traer y enviar datos (en estos casos no se pudo el envio porque no deja pero entiendo el concepto)
### 4.5 Reflexión final
Aprendi que sirve como una forma de send/receive datos, que postman es una excelente forma de hacer pruebas antes de pasarlo a "Live". me gusto, entiende el concepto de para que es que se utiliza el get, push, put, delete

Sobre post me ayudo a entender mejor como es que funciona el request/receive de la informacion.