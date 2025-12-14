# Objetivos

Al final de esta lección, tú vas a:

1. Clonar y contribuir a este repositorio.
2. Entender cómo se ejecuta Python.
3. Entender el paquete.
4. ¡Instalar un paquete!
5. ¡Ejecutar un programa de Python!

# Instalación

Opción Uno:

  $ xcode-select --install

Opción Dos:

  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  $ brew install python git

# Cloname

- Crea una cuenta en [GitHub.com](https://github.com) si no tienes todavía.
- Genera una clave SSH: [Documentación](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).  
- Pon la parte PUBLICA (*.pub) de esa clave en 'Settings'>'SSH and GPG Keys'.
- La parte privada queda en tu computadora en `~/.ssh`.  Tú puedes usar `~/.ssh/config` para eligir cuál clave estás usando a para comunicarte con GitHub.  Si hay solo una, no es necessario.

```
Host github.com
  IdentityFile ~/.ssh/id_ed25519
```

-  Corre `git clone git@github.com:ksell8/all-aboard-python.git`


# Usando Python

Tú has eligido Python como tu luchador.  Bien eligido amigo.

Una cosa importante.  Python es muy lento.  Pero, no importa.  

Sin embargo, es importante que entiendas porque es la verdad para que comprendes los debilidades de tu luchador.  Sin ese conocimiento no puedes usar Python con éxito.  Nosotros vamos a indagar en estas lecciones, pero los luchadores más rapidos trabajan con la maquina directamente, mientras Python trabaja a traves de una maquina virtual que se llama `the Python Virtual Machine`.  Hay muchss implementaciones de PVM.  La más común es CPython, escrito en C.  PyPy es concocida por ser un poco más rapido, pero depende del trabajo. 

Veamos cuál estás usando:

```
import platform

print(platform.python_implementation())
```

Lo mejor de Python es que mucha gente lo usa.  Y ellos han creado muchos útiles.  Tú puedes usar su trabajo en vez de crearlo tú mismo otra vez.

Cuando gente crea código reutilizable lo comparte en un archivo que se llama el paquete.  Casi cada lenguaje de computación tiene una forma de paquete, y también tiene un lugar que almacena los paquetes.  El lugar más común de almacenamiento de paquetes se llama [PyPi](https://pypi.org/) que significa 'Python Package Index'.  También, necesitas una manera de descargarlos.  Lo más común y sencilla es usar PIP.  PIP significa 'Pip installs Packages'.  Mi preferencia es [Poetry](https://python-poetry.org/), pero vamos a empezar con PIP.  Ahora, [UV](https://docs.astral.sh/uv/) es lo mejor.  Todo cambia muy rápidamente en la ciencia de computación.

Por defecto, PIP instala los paquetes globalmente.  No puedes tener más de una versión del mismo paquete globalmente.  Pero hay situaciónes en las que necesita una versión para un proyecto y una versión diferente para un otro. Y, por eso, hay entornos virtuales!  Entornos virtuales son un espacio aislado donde puedes instalar paquetes y ejecutar programas.

Para crear un entorno virtual corre:

  $ python3 -m venv venv

  $ source venv/bin/activate

> [!WARNING]
> Típicamente el paquete virtualenv está instalado con python, pero si no, instala globalmente
>
> Usando: pip install virtualenv
>
> Nunca instales paquetes en la forma global excepto virtualenv

Para salir:

  $ deactivate

# Pruébalo

Para instalar las dependencias de la muestra en el virtualenv:

  $ pip install -r requirements.txt

Para ejectuar la programa:

  $ python data_processor.py