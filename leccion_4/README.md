# What to do?

Trace the call stack of the examples using [Pila de Frames](https://trippyhippies.org/homework/call_stack_simulator.html).

## Important Terms

- Stack: Theoretical concept in computer science.  A traditional stack is LIFO, last in first out.  This is the opposite of a line, which is FIFO, first in first out which is called a queue (like the Brits call it).  Real life examples of a stack are a stack of dishes.  Typically folks pull from the top.
- Call Stack: The call stack is a stack that the python interpreter uses to manage the control flow of functions.
- Entrypoint: An entrypoint is another program starts a python program.  It is the first function that goes on the call stack.  All other calls come from this. The simplest entrypoint looks like this:
    

    __name__ == "main":
            print("this is an entrypoint")
    