# Objetivos

Al final de esta lección, tú vas:

1. Entender como Python ejecutar.
2. Entender el paquete.
3. ¡Instalar un paquete!
4. ¡Ejecutar una programa de Python!

# Instalación

OPCION UNO:

  $ xcode-select --install

OPCION DOS:

  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  $ brew install python git

# Cloname

- Crea una cuenta en (GitHub.com)[https://github.com] si no ya tienes.
- Genera una clave SSH: (Documentación)[https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key].  
- Pon la parte PUBLICA (*.pub) de esa clave en 'Settings'>'SSH and GPG Keys'.
- La parte privado queda en tu computadora en `~/.ssh`.  Tú puedes usar `~/.ssh/config` a eligir cuál clave está usando a communicar con GitHub.  Si hay solo uno, no lo es necessario.

```
Host github.com
  IdentityFile ~/.ssh/id_ed25519
```

-  Corre `git clone git@github.com:ksell8/all-aboard-python.git`


# Usando Python

Tú has eligido Python como tu luchador.  Buen eligido amigo.

Una cosa importante.  Python es muy lento.  Pero, no importa.  

Sin embargo, es importante que entiendas por que es la verdad para que comprendes los debilidades de tu luchador.  Sin eso conocimiento no pueda usar Python con éxito.  Nosotros vamos a investigar en estas lecciones, pero los luchadores más rapidas trabajan con la maquina directamente, mientras Python trabaja a traves de una maquina virtual que se llama `the Python Virtual Machine`.  Hay muchos implementaciones de PVM.  Lo más común es CPython, escrito en C.  PyPy es concocido por ser un poco más rapido, pero depende del trabajo. 

Veamos cuál estás usando:

```
import platform

print(platform.python_implementation())
```

Lo mejor de Python es que mucha gente lo usa.  Y ellos han creado muchos útiles.  Tú puedes usar su trabajo en vez de crearlo tú mismo otra vez.

Cuando gente crea código reutilizable lo comparte en un archivo que se llama el paquete.  Casi cada lenguaje de computación tiene una forma de paquete, y también tiene un lugar que tiene los paquetes.  El más común lugar de paquetes de Python se llama (PyPi)[https://pypi.org/] que significa 'Python Package Index'.  También, necesitas una manera a descargarlos.  Lo más común y sencilla es usar PIP.  PIP significa 'Pip installs Packages'.  Mi preferencia es (Poetry)[https://python-poetry.org/], pero vamos a empezar con PIP.  

Por defecto, PIP instala los paquetes globalmente.  No puedes tener más de una versión del mismo paquete globalmente.  Pero hay situaciónes en las que necesita una versión para un proyecto y una versión diferente para un otro. Y, por eso, hay virtual environments!  Virtual environments son un espacio aislado donde puedes instalar paquetes y ejecutar programas.

Para crear un virtual environment corre:

  $ python3 -m venv venv

  $ source venv/bin/activate

> [!WARNING]
> Típicamente el paquete de virtual environment está instala con python, pero si no, instala globalmente
> Usando: pip install virtualenv
> Nunca instales paquetes en la forma global excepto virtualenv

Para salir:

  $ deactivate

# Pruébalo

Para instalar las dependencias de la muestra en el virtualenv:

  $ pip install -r requirements.txt

Para ejectuar la programa:

  $ python data_processor.py