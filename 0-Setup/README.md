# 0 - Setting Up  

  

Queremos darte la bienvenida a nuestro del lenguaje del programación Python.

  


  

En esta primera guía nos dedicaremos a a descargar y configurar (en muchos lados en vez de configurar verás la palabra *setear*) nuestro entorno de trabajo.

  
  

Pero antes hablemos un poco de los **sistemas operativos (OS).**

  

---

  

# Sistemas Operativos

Un sistema operativo es la base sobre la cuál instalamos los programas/aplicaciones y su trabajo es de servir de intermediario entre el *hardware* y las aplicaciones que usamos.

  

Vamos a verlo como los planos de un edificio.

  

El *Hardware* es como un edificio sin acabados, tiene las conexiones de luz, agua, tienes el piso pero en concreto puro, no hay llaves de agua, no hay interruptores, tampoco luces, etc, es decir, no es habitable.

  

El *OS* es el mismo edificio pero con todos los acabados, tiene sus pisos, sus interruptores, sus luces etc. ¡Pero está vacío!

¿Para hacerlo habitable que podría faltar?

Necesita un amoblado que le de funcionaldiad y propósito al edificio, en nuestro caso aquí entran las *aplicaciones*.

  
  

Existen tres sistemas operativos dominantes en el mundo, y estos poseen detalles que pueden modificar la forma en que tendemos a programar, *casi nunca radicalmente*, pero hay detalles de los que debemos estar pendientes y que aprenderemos poco a poco.

  

Estos son:

  

- Windows

- MasOS

- Y Linux

  
  

## Windows

Este sistema no necesita presentación, domina el mercado mundial de computadores personales, y si te gusta el gaming estas prácticamente obligado a tener Windows en tu computadora (aunque Steam ya pone esta dominancia en duda).

  

Ya que este **SO** está dirigido a un público general, no deja muy a la mano las herramientas de programación y su flexibilidad es poca, aunque su soporte es grande y la mayoría de las instalaciones están automatizadas.

  

## MacOs

El sistema operativo por excelencia de las computadoras de Apple, está inspirado en una familia de SO que se denominan **Unix**, una de la caracteristicas de la que hablaremos más adelante es de su poderosa terminal, con la cuál se instalan muchos programas.

  

Por su arquitectura y diseño el desempeño de las Macs es excelente y da mucha flexibilidad a los programadores.

  

## Linux

En realidad, Linux es lo que se denomina un *Kernel*, por lo cuál es en realidad una familia de SO (inspirados en Unix), está familia destaca por ser gratuita (casi siempre) y altamente personalizable. En el pasado se consideraba que solo los programadores más avanzados podía usar un SO Linux (¡y no sin razón!), pero hoy en día con distribuciones como Ubuntu, Pop_Os o Manjaro, entre muchos otros, usar un SO Linux está sencillo como usar Windows o MacOs.

  

Además, casi todos ya tienen preinstalado Python además de la terminal tan característica de estos sistemas.

  

---

![enter image description here](https://www.python.org/static/img/python-logo.png)

# Python v3

Te hablamos de los *SO* porque estos van a definir como vas a instalar Python (entre otros detalles a futuro), ya que en cada sistemas es distinto.

  

Primero que nada debes dirigirte a esta dirección: https://www.python.org/downloads/

  

Y seguir los pasos segun tu sistema operativo.

  
 En Windows basta con bajar el instalador y ejecutarlo como cualquier otro programa que puedes descargar. Es posible que te pida que ejecutes como administrador.

MacOs a veces viene con Python preisntalado, asi que primero:
-  Abre una terminal (En el Finder, abre la carpeta /Aplicaciones/Utilidades y, a continuación, haz doble clic en Terminal).

- Dentro de la terminal escribe: `python3 --version` (minúscula todo el comando)

- Si aparece algo como: `Python 3.xx.xx` (las **x** son números que pueden variar) significa que ya tienes el software .

- Si no aprece nada o aparece `Python 2.xx.xx`, deberás bajar la aplicación desde la página oficial e instalarla.

- Cuando termien la instalación ingresa otra vez: `python3 --version` para asegurarte de que todo esté bien.

  

En Linux debes arbir una terminal con `Ctrl + t` y escribir `python3 --version`, y si aparece `Python 3.xx.xx`(las **x** son números que pueden variar) significa que ya tienes el software .

- De no aparecer el mensaje ingresa en la terminal: `sudo apt update`

- Una vez terminado ingresa: `sudo apt install python3`

- Cuando termien la instalación ingresa otra vez: `python3 --version` para asegurarte de que todo esté bien.

  
  
  

### Paso extra para usuarios de Windows

  

Si lo sé, es un poco fastidioso que tengas un paso extra, pero como dijimos más arriba, Windows no está pensado en programadores.

  

- En el buscador escribe "PowerShell", este emula (imita) las terminales Unix de MacOs/Linux (puede aparecer como Windows PowerShell).

- Si no lo tienes dirigete aquí y sigue los pasos: https://learn.microsoft.com/es-es/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3#winget

  

## Usemos Python

  

**Nota:** De ahora en más, cuando hablemos de "Terminal", los ususarios de Windows deben abrir el (Windows)PowerShell.

  

Abre una terminal e ingresa: `py` si eres usuario Windows o `python3` si eres usuario Unix.

  

Deberias tener un mensaje aprecido a este:

  

```
Python 3.11.1 (main, Jan 6 2023, 00:00:00)

[GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] on linux

Type "help", "copyright", "credits" or "license" for more information.

>>>
```




¿Ves esas tres flechas?

`>>>`

  

Eso es un **prompt**, especificamente un prompt de Python, y simplemente indica que:

  

1. Estás es un espacio vitual de Python, es decir, todo lo que escribas de ahí en más debe ser bajo las reglas de este lenguaje (ya las iremos viendo poco a poco).

2. Está esperando algun tipo de comando de parte del usuario (es decir, espera a que tú le des una instrucción).

  

Ahora escribe en el promt: `print("hello world")` y presiona Enter.

Deberias verlo asi:

  

>>> print("hello world")

hello world

  
  
  

No parece muy útil ¿verdad?

  

Que tal ahora:

  

>>> 472 * 195

¿Cuál fue el resultado?

  

Mejor, pero tampoco particularmente útil, es más fácil usar la calculadora de tu celular.

  

En la realidad, casi nunca usamos el entorno de Python de esta manera, pero nos sirve para hacer pequeños juegos que nos ayudan a concoer mejor este lenguaje, pero para programar de verdad necesitaremos editores de código.

  

-----

# Editores de Código

  

En realidad, son como los block de notas de Windows, y es que de hecho, podemos escribir código de cualquier lenguaje con block de notas, basta con cambiar la terminacion del archivo de .txt a .py (en el caso de python, en un lenguaje como JavaScript debe termianr en .js y en C# en .cs) para que se pueda ejecutar.

  

Sin embargo un editor moderno como VSCode y Sublime nos va a facilitar el trabajo al momento de escribir y debuggear nuestro código.

  

En general ambos son muy buenos y modernos, particularmente preferimos VSCode por ser más moldeable y tiene muchas extensiones que aumentan su funcionaldiad, pero eso viene con el coste de hacer este software más pesado.

Si tu computadora es muy vieja o está muy lenta te recomendamos que uses Sublime.

  

Finalmente no hay nada de malo con que experimentes con ambos editores y decidas cuál es mejor para ti.

  

Aquí te dejamos una conversación entre Lex Fridman y Guido Van Rossum (el creador de Python) sobre editores de código para Python: https://www.youtube.com/watch?v=G5mtQhWNezQ&ab_channel=LexClips

  

## VSCode

  

Este es un editor creado por Microsoft, increiblement popular y ligero. Su nombre es *Visual Studio Code* pero se abrevia como *VSCode* normalmente.

No lo llames Visual Studio, ese es un IDE, un editor altamente especializado, tambien de Microsoft, pero dedicado a un número particular de herramientas y puedes generar confusión.

  

VScode

![enter image description here](https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/getstarted_page.png)

  

Para instalar, primero ve a https://code.visualstudio.com/

  

Descarga la app, y la instalas como instalaste Python si estas en Windows o en Mac.

  

En Linux, las versiones más reciente tienden a funcionar tal cual Mac y Windows, pero puede ser que no dependiendo de tu distro. En dado caso descargas la app y en la carpeta de descargas con click derecho le das a *abirir en terminal/open in terminal* y ejecutas

  

```

sudo apt install code_1.xx.xx.deb

```

**Nota:** escribe el comando hasta la letra "c" de modo que quede coomo: `sudo apt install c` y presiona la tecla `tab` de este modo se autcompleta el nombre del archivo.

  

### Configurando VSCode

Primero abre el VSCode y a la izquierda verás unos cuanto iconos, busca el que dice *extensiones/extensions* y te dará una barra de busqueda.

  

En esa barra escribe *python*, verás una extension del mismo nombre, abajo tendrá como una *estrella o lazo azul* que dice Microsoft y le das a instalar.

  

![enter image description here](https://www.mytecbits.com/wp-content/uploads/Visual-Studio-Code-For-Python-01-776x401.jpg)

  

Esta lo que hará será el indicarnos errores de código.

  

Luego busca e instala "indent-rainbow" y "Path Intellisense" para ayudas extras.

  

---

  

Ahora vamos a *Archivos/Files*-> *Preferencias/Preferences* -> *Configuración/Settings*.

  

En el buscador ingresa: "word wrap". Y en la primera opción que aparece "Editor: Word Wrap" la colocas en "on".

  

![enter image description here](https://www.kindacode.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-11-at-16.58.57.jpg)

  

Ahora ingesa "bracket pair colorization" en el buscador, y en la opción del mismo nombre asegurate que esté marcada.

  

Con esto estamos listos con VSCode.

  

## Sublime Text

  

Es quizas el otro gran editor de los que hay en el mercado, un poco menos potente que VSCode pero por lo mismo más rápido y ligero.

  

![enter image description here](https://www.sublimetext.com/screenshots/3.0/linux@2x.png)

  

Primero ve a su página oficial: https://www.sublimetext.com/

  

Descarga la app, y la instalas como instalaste Python si estas en Windows o en Mac.

  

En Linux debrás hacer varios pasos:

  

1. Abrir una terminal.

2. Ingresar `wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null`.

3. Luego ingresas `echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list`.

4. Después: `sudo apt update`

5. Finalmente: `sudo apt install sublime-text`

  

**Nota:** pregunta en la clase el significado de cada comando.

  

### Configurando Sublime Text

Abre Sublime Text y presiona en *Ver/View* y busca la casilla "Word Wrap" casi al final y asegurate que esté seleccionada.

  

Ahora en *Tools/Herramientas* -> *Command Palette/Paleta de Comandos*, haces click en la opcion en ingresas "python" y aparecerá *"set sintax: Python"*, elige la opción.

  

¡Todo listo!

  

---

  

# !La Terminal!

  

Las Terminales Unix o Shell Unix son herraminetas poderosas que permite que tú, el usuario, pueda comunicarse de una manera muy directa con la computadora haciendo uso de pocos recursos de procesador y realizando las acciones rápidamente.

  

Las terminales tienen su propio Scripting (su propio lenguaje de programación) que se llama **bash**, aunque no lo vamos a aprender, si debemos concoer algunos comandos que nos van a ayudar un montón.

  

1. Crea una carpeta en cualquier lado de tu escritorio, ponle el nombre que quieras, pero este *no debe contener espacios*.

  

2. Entra en la carpeta y ya adentro abre una Terminal.

3. Vamos a crear una nueva carpeta que se llame "esta_es_una_carpeta", pero la crearemos con la terminal usando el comando **mkdir**. `mkdir esta_es_una_carpeta` y presionas "enter".

3.1. **mkdir** viene de make directory (crear/hacer directorio)

4. Deberias ver la carpeta nueva creada, para verla en la terminal usa el comando **ls**.

4.1. **ls** proviene de listing (listado)

5. Vamos a crear un archivo de texto con el comando **touch**. Ingresa `touch mi_texto.txt`. Ahora usa el comando **ls**, ¿lo ves?.

6. Ahora vamor a ir dentro de "esta_es_una_carpeta", usando el comando **cd**, en Unix ingresa `cd /esta_es_una_carpeta` en Windows `cd \esta_es_una_carpeta`.

6. 1 **cd** viene de change directory (cambiar directorio)

6. 2 En Windows las direcciones de los directorios o carpetas se indican con " \ " mientras que en Unix se hace con " / ".

7. Vamos a crear un archivo nuevo usando **touch**, `touch hello.py`. ¡¡¡Has creado tu primer archivo de Python!!!!

8. Vamos a subir un niverl, usando `cd ..`  **OJO**, no uses `cd`, asi sin los dos "." (puntos), ya que esto te llevará a la raíz de todo tu sistema. Si eso pasa, puedes abrir una nueva terminal donde quedamos.

9. Vamos a eliminar el archivo "mi_texto.txt" usando el comando **rm**. Dejaré que deduscas lo que debes hacer.

9.1. **rm** es por remove (remover)

  

10. En este punto tu terminal debe verse algo desastrosa, vamos a limpiarla con el comando **clear**, así eliminamos toda esa info de la pantalla.

10.1 **clear** significa limpiar.

11. Para terminar puedes abrir todo el contenido usando VSCode con el comando `code .` (incluye el punto) o con Sublime usando `subl .` (también con el punto).

  

Las terminales Unix tienen muchisimos más comando y se pueden crear comandos propios para casi todo, pero de momento con los que tenemos más que suficiente.

  

-  **mkdir**

-  **ls**

-  **cd**

-  **touch**

-  **rm**

-  **clear**

-  **code/subl .**

  

##### (En esta seccion puedes ver un poco de historia de las primreas terminales de computadora que existieron: https://www.youtube.com/watch?v=47NRaBVxgVM&t=11623s&ab_channel=freeCodeCamp.org)

  
  ---
  
# Control de Versiones

  
  
  

¿Has visto a alguien haciendo una Tesis?

  

Siempre hay como 10 archivos que se llaman "Tesis Final"

![enter image description here](https://pbs.twimg.com/media/Bx1ZBdHCUAAqPpr.jpg)

  

Y los programadores tuvieron este problema por mucho tiempo hasta que Linus Torval (padre del Linux Kernel) creo Git.

  

Git lo que hace es tomar como una foto de los cambios que vas realizando, y puedes tener distintas versiones en un mismo archivo sin que afecte el rendimiento del programa o la organización.

  

Es un poco abstracto mentalmente hablando pero será más facil de entender con la práctica.

  

## Instalando Git

  

Para Windows ve a esta dirección: https://git-scm.com/download/win

Y baja la versión de 64-bits.

  

Para Linux y MacOs primero abre una terminal e ingresa:

```bash

git  --version

```

Si obtienes:

````bash

git  version  2.39.1 (puede ser  este  número  o  superior)

````

Ya está intalado en tú máquina.

  

Si no:

  

Linux:

```bash

sudo  apt  update

```

luego:

```bash

sudo  apt  install  git

```

  

En el caso de MacOs se puede complicar un poco ve a esta página y sigue las instrucciones: https://www.atlassian.com/git/tutorials/install-git

  
  

### Para todos!!!

No olviden checar su version de Git con:

  

```bash

git  --version

```

  
  



## Configurando Git

Vamos a configurarlo rápidamente con estos comandos.

Vamos a añadir tu usuario y tu email:

```bash

git  config  --global  user.name  "ActionCoders"

git  config  --global  user.email  "acoders@ac.com"

```

  

Ahora copia el siguiente:

`````bash

git  config  --global  init.defaultBranch  main

`````

El anterior es apra evitar conflictos con github.

  

Vamos a darle algo de color a git:

  

```bash

git  config  --global  color.ui  auto

```

Y para terminar:

```bash

git  config  --global  pull.rebase  false

```

  

Vamos a chequear tu usuario y tu email:

```bash

git  config  --get  user.name

git  config  --get  user.email

```

  

### !MacOs Alerta!

Usen un paso extra:

```bash

echo  .DS_Store >> ~/.gitignore_global

git  config  --global  core.excludesfile  ~/.gitignore_global

```

Esto evitara que se guarden y suban unos archivos de seguimieento que solo sirven en y para MacOs.

  
  

  

## GitHub

  

Si Git es la herramienta con la que haces videos, GitHub sería el Tiktok a donde los subes.

  

Es una especie de red social y almacén de proyectos, la idea no es subir programas completos, sino los scripts de los proyectos. Darle vida y movimiento a tu GitHub es de suma importancia, los desarrolladores profesionales son medidos en buena medida por sus aportes dentro de esta comunidad.

  

Primero que nada ve a https://github.com/ y abre una cuenta con el mismo correo que asociaste a Git.

  

Ahora vamos a asociar la cuenta de GitHub a Git.

  

En GitHub, busca el icono a la derecha, has click, y ve a *Settings*, ahora a la izquierda busca *SSH and GPG keys* y has click, ahora has click en *New SSH Key*.

  

Aquí va la clave que vamos a crear:

![enter image description here](https://syntaxbytetutorials.com/wp-content/uploads/2019/07/githubssh-1024x530.png)

  
  
  

Vamos a crear una clave **ssh**, es una clave criptográfica que usa algoritmos complejos para proteger tu cuenta y tus archivos. Abre una terminal e ingresa:

```bash

ssh-keygen  -t  ed25519  -C <youremail>

```

Ahora usa este comando:

```bash

cat  ~/.ssh/id_ed25519.pub

```

Deberia salir algo (reemplazamos una clave real por puras 'A' pero para ti serán como un montón de letras aleatorias seguido de tu correo):

```bash

ssh-aa55555  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAA

actioncoders@actioncoders.com

  

```

Vamos a probar la conexión:

Ingresa:

```bash

ssh  -T  git@github.com

```

  

Deberías obtener:

  

```bash

> The authenticity of host 'github.com (IP ADDRESS)' can't be established.

> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.

> Are you sure you want to continue connecting (yes/no)?

```

Responde *yes* y debería decir ahora:

```bash

> Hi (Tú  nombre  se  usuario)! You've successfully authenticated, but GitHub does not

> provide shell access.

```

  

Si te da un mensaje de error, descansa media hora y repite los pasos, si aún así persiste el problema contacta con tu profesor.

  
  

# Usemos Git

  

Primero que nada ve a tu GitHub, crea un nuevo repositorio, ve al ícono de tu perfil, *Your repositories*, y presiona en *New*. Siguiendo la tradición, vamos a llamarlo *Hello_World*.

  

Ahora Vamos a copiar la clave **ssh** que no da ese repo asi:

![enter image description here](https://cdn.statically.io/gh/TheOdinProject/curriculum/b54d14c5dcee1c6fac61aee02fca7e9ef7ba1510/foundations/git_basics/project_practicing_git_basics/imgs/02.png)

  

Crea una carpeta para nuestros proyectos. Dale el nombre que más te guste, y dentro de esa carpeta abre una terminal y vamos a usar el comando *git clone*.

```bash

git  clone  {aquí  copias  la  clave  ssh  de  GitHub}

```

Ahora crea un archivo *Hello_World.txt* (con la consola)

  

Vamos a ver cuál es el estado con el comando

```bash

git  commit  status"

```

  

![enter image description here](https://cdn.statically.io/gh/TheOdinProject/curriculum/b54d14c5dcee1c6fac61aee02fca7e9ef7ba1510/foundations/git_basics/project_practicing_git_basics/imgs/07.png)

  
  

Está en rojo porque no hemos iniciado el seguimiento del archivo, para eso debemos usar el comando:

```bash

git  add  .

```

Esto añade el archivo al seguimiento de Git.

Ahora usa el comando para darle una descripción:

```bash

git  commit  -m  "{aquí debes escribir un mensaje pequeño}"

```

  

Si usas `git status` una vez más debería estar en verde.

  

Ahora subelo a GitHub con:

```bash

git  push

```

¡¡¡Mira tú GitHub y ve que hay en el repo!!!

Estó será suficiente por ahora, demomento no debemos bajar ni configurar más nada pero puedes consultar esta guía tantas veces necesites.

  



**Ahora todo esta listo para comenzar.**

  
  

