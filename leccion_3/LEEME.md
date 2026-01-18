# Objetivos

Al final de esta lección, entendrás:

1) Modelos de datos y por qué son importantes
2) Clases y objetos y la relación entre los dos
3) Los patrones de diseño

# Modelos de Datos Internos

[Pensamientos por AWS](https://aws.amazon.com/es/what-is/data-modeling/)

La computación es la practica de usar datos para hacer algo.
Por eso, la estructura del dato en nos aplicaciones define cómo funciona
la aplicación. Lo más importante es nos modelo de datos.

Hay una practica en ingeniería de datos que se llama ETL (extract, transform, load).
Hoy, nos centramos en los modelos de transformación.  Pero, tengamos que conjeturar
sobre cuál tipos de datos vamos a extraer y cuál tipos de datos queremos terminar con
a saber cuáles transfomaciónes son necesarios.

# Pydantic

[Pydantic](https://docs.pydantic.dev/latest/concepts/models/) es un paquete que contiene
un módulo que se llama `BaseModel`.  Eso es un tipo de clase que automáticamente crear validadores
a los tipos de datos en el modelo.  

Nosotros hablámos sobre algunos tipos en Python como `string`, `dict`, `list` en la última clase.
Pero, si había un error de tipo, no lo sabíamos hasta que ejecutábamos la función.

# Clases y Objetos

Python es una lengua de Programación Orientada a Objetos (POO).  Una clase es una especificación
para un objeto.  Para crear un objeto desde una clase se llama a la función __new__.  Después de
crearlo, Python se llama __init__ que instanciar el objeto.  Normalmente solo escribimos una nueva __init__ y usamos
la configuración predeterminada para __new__.  `BaseModel` ya define __init__ especial.  Puedes verlo [aquí](https://docs.pydantic.dev/latest/api/base_model/).

Cuando nosotros creamos una clase como eso

`class SpanishSentence(BaseModel)`

decimos Python a crea nos clase como una clase hija de `BaseModel` y por eso nos clase usa
las funciones declaradas en `BaseModel`.  Eso se llama herencia, y la es muy importante de POO.

Todos los "pilares" de POO: inheritance, encapsulation, polymorphism, y abstraction. Pero, empecemos
con herencia.

# Patrones de Diseño

Nadie me dijo sobre los patrones de diseńo cuando yo estaba enseńado POO.  Es un concepto
muy "avanzado" pero, pienso que nunca es demasiado temprano para empezar a pensar en ellos.

Patrones de diseńo definen cómo hablan los objetos.

Pydantic usa patrones, como [método plantilla](https://refactoring.guru/es/design-patterns/template-method).

[Lo mejor recurso de patrones.](https://refactoring.guru/es/design-patterns)
