# Objectives

By the end of this lesson, you will understand:

1) Data models and why they are important
2) Classes and objects and the relationship between the two
3) Design patterns

# Internal Data Models

[Thoughts by AWS](https://aws.amazon.com/what-is/data-modeling/)

Computing is the practice of using data to do something.
Therefore, the structure of data in our applications defines how the
application works. The most important thing is our data models.

There is a practice in data engineering called ETL (extract, transform, load).
Today, we focus on transformation models. But, we need to conjecture
about what types of data we will extract and what types of data we want to end up with
to know which transformations are necessary.

# Pydantic

[Pydantic](https://docs.pydantic.dev/latest/concepts/models/) is a package that contains
a module called `BaseModel`. This is a type of class that automatically creates validators
for the data types in the model.

We talked about some types in Python like `string`, `dict`, `list` in the last class.
But, if there was a type error, we didn't know until we executed the function.

# Classes and Objects

Python is an Object-Oriented Programming (OOP) language. A class is a specification
for an object. To create an object from a class, the __new__ function is called. After
creating it, Python calls __init__ which instantiates the object. Normally we only write a new __init__ and use
the default configuration for __new__. `BaseModel` already defines a special __init__. You can see it [here](https://docs.pydantic.dev/latest/api/base_model/).

When we create a class like this

`class SpanishSentence(BaseModel)`

we tell Python to create our class as a child class of `BaseModel` and therefore our class uses
the functions declared in `BaseModel`. This is called inheritance, and it is very important in OOP.

All the "pillars" of OOP: inheritance, encapsulation, polymorphism, and abstraction. But, let's start
with inheritance.

# Design Patterns

Nobody told me about design patterns when I was learning OOP. It's a very
"advanced" concept but, I think it's never too early to start thinking about them.

Design patterns define how objects communicate.

Pydantic uses patterns, like [template method](https://refactoring.guru/design-patterns/template-method).

[The best resource for patterns.](https://refactoring.guru/design-patterns)
