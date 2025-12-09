# Objectives

By the end of this lesson you should be able to:

1. Understand how to clone and contribute to this repo.
2. Understand how python code runs.
3. Understand what a package is.
4. Install a package!
5. Run a Python program!

# Installation

OPTION ONE:

  $ xcode-select --install

OPTION TWO:

  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  $ brew install python git


# Clone Me

- Create an account on [GitHub.com](https://github.com) if you don't already have one.
- Generate an SSH key: [Documentación](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).  
- Put the public part of the key (*.pub) under 'Settings'>'SSH and GPG Keys'.
- The private part of the key lives under `~/.ssh`.  You can use `~/.ssh/config` to choose which key you want to use for the Github server.  If you only have one key, this is not necessary

```
Host github.com
  IdentityFile ~/.ssh/id_ed25519
```

- Run `git clone git@github.com:ksell8/all-aboard-python.git`.  This will create an all-aboard-python folder in your current working directory (CWD).

# Using Python

You have chosen Python as your fighter.  Good choice friend.

An important thing about python.  It's slow.  But that doesn't matter.

What is important is that you understand why it is slow.  Knowing your fighter's weaknesses is how you understand how to most effectively use them.  We will explore why this is the case in our upcoming lessons, but the general idea is that faster fighters work with the machine directly by translating to machine code, and Python works through a virtual machine, which then tells the computer what to run.  There are different implementations of the Python virutal machine.  The most common implementation is CPython.  The implementation known to be the fastest (under certain conditions) is PyPy.

Let's see which implementation you are running:

    $ import platform

    $ print(platform.python_implementation())

The best part about Python is that lots of people use it.  And these people have created lots of useful tools and shared them with the world to use.  These tools are shared in the form of packages.  Most computing languages have a concept similar to python packages, and they all have a centralized place these packages are stored.  [PyPi](https://pypi.org/) is the most common place for Python packages.  You will also need a way to download these packages, these tools are called package managers.  The most common and simple package manager for Python is called PIP which stands for 'Pip installs packages'.  My favorite is [Poetry](https://python-poetry.org/), but we will start with PIP.

PIP is installed with both installation options above.  And is either under pip or pip3.  You can type the command to check out everything that is possible with it.

By default PIP installs packages globally, but you can't install multiple versions of the same package globally.  This makes it difficult to manage multiple projects with multiple versions on one machine.  But not to worry, it for this reason that virtual environments exist!  A virtual environment is a digital sandbox that allows you to install whatever packages you need and run programs without worrying about messing up your global environment.

To create a virtual environment run: 

    $ python3 -m venv venv

    $ source venv/bin/activate
    
> [!WARNING]
> The virtual environment library is typically installed with python, but you may need to install it globally with pip.
>
> Using: pip install virtualenv
>
> This is the ONLY package you should ever install globally.

To exit:

    $ deactivate

# You Try It

There is a sample project under sample.  

To install the dependencies of the sample in the virtualenv run:

  $ pip install -r requirements.txt

To run the sample program:

  $ python data_processor.py