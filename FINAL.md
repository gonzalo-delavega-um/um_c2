
## Requisitos examen final

Para poder rendir el examen final es requisito haber regularizado la materia a fin del semestre.

El examen final consistirá en la exposición de un código integrador desarrollado por el alumno, cuyo tema será acordado previamente con el profesor.

Para definir los requisitos y alcances del trabajo, **antes de entrar a codear** será necesario plantear una arquitectura del proyecto, problema que solucionará, tareas que ejecutarían, entidades, herramientas de sincronismo concurrencia, justificaciones. Una vez que el **tema ha sido discutido y aprobado** para su desarrollo, se acordará un repositorio GIT donde se irán cargando los cambios periódicos en su desarrollo.

### Consideraciones del código:
El código debe solucionar un problema haciendo uso de las herramientas vistas en clase. Debe incluir aspectos como:
* Uso de Sockets con conexión de clientes múltiples de manera concurrente.
* Uso de mecanismos de IPC
* Uso de asincronismo de I/O
* Uso de cola de tareas distribuidas

Como aspectos opcionales adicionales puede considerarse:
* Despliegue en contenedores Docker
* Parseo de argumentos por línea de comandos
* Almacenamiento de datos en bases de datos

### Presentación
La aplicación a desarrollar deberá ser **acordada previamente** con el profesor de la cátedra.
Una vez desarrollada, deberá ser presentada al profesor al menos una semana antes de la mesa de examen final, para que éste pueda visarla y dar el visto bueno al alumno.
El código deberá ser presentado en un repositorio GIT (o un subdirectorio del repositorio git del alumno), bien organizado, y con el agregado de los siguientes archivos markdown:
* **INSTALL**: contendrá las instrucciones para clonar e instalar/lanzar la aplicación.
* **README**: contendrá la ayuda y uso básico de la aplicación.
* **README.info**: contendrá un breve informe sobre las decisiones principales de diseño del sistema, y su justificación (ej, por qué un determinado modelo de datos, o tipo de almacenamiento, o uso de multiproceso/multithread, etc).
* **README.todo**: contendrá una lista detallada de mejoras y posibles nuevas características/features del sistema para futuras versiones.

Durante la presentación, el alumno expondrá el funcionamiento de la aplicación, explicará el código fuente y tecnologías utilizadas, y el tribunal de la mesa de examen podrá realizar preguntas teóricas sobre los contenidos prácticos expuestos por el alumno.
El tribunal también podrá solicitar pequeños *fixes* de bugs detectados durante la presentación, y pequeñas modificaciones del código.

### Notas:

* No tiene fecha **límite de presentación** (mientras no se les venza la regularidad de la materia :P ). Pueden presentarlo a lo largo del año. El único requisito es que, una vez que decidan en qué mesa van a rendir, una semana antes deben tener el código completo.

* Antes de ponerse a codear les tengo que aprobar la app que piensan desarrollar. Dentro de sus repositorios git creen un directorio llamado **final**, y ahí dentro, un **FINAL.md** que incluya un *diagrama de la arquitectura* de la app que van a desarrollar (piezas de software, nodos en la red, quién se conecta con quién, cómo, qué funcionalidad tienen cada pieza, etc. Pueden armar el diagrama, y un *texto explicativo* sobre qué hace cada cosa, lo más detallado posible.

* El código deberá ser desarrollado de **manera incremental**, por lo que se valoran cambios progresivos (commits) en el repositorio de software durante todo el proceso de desarrollo. En la medida que vayan desarrollando la app, vayan commiteando seguido, no esperen a tener una versión funcional para commitear, no importa si funciona o no, commiteen igual! Eso les sirve para que podamos charlar dificultades, inconvenientes, para que yo pueda ver la evolución del proyecto, y de paso, a ustedes les queda un backup de todo lo que van haciendo (ya no es excusa el "se me rompió el disco, me robaron la compu y tenía todo ahí, etc... tenemos git, aprovechenlo!).

La idea de ese FINAL.md es que podamos quedar, ustedes y yo, con una idea fina de lo que van a hacer. A mi me sirve para saber que tienen noción de los alcances de sus apps, lo que tienen que armar, y a ustedes les sirve de guía para no *irse por las ramas* y acotarse a eso. Igualmente durante el desarrollo pueden charlarse cambios, pero lo ideal es que quede lo más definido posible de entrada.

