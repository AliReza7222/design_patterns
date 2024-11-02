# Strategy Pattern

## Definition
The **Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently from the clients that use it, providing flexibility and modularity.
**_Take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don’t._**

## Key Features
- **Encapsulation of Algorithms**: Strategy Pattern enables you to encapsulate a family of algorithms into individual classes, each implementing a particular behavior or algorithm.
- **Interchangeable Behavior**: The encapsulated algorithms are interchangeable, allowing you to modify the behavior at runtime as long as the object being used implements the correct behavior interface.
- **Runtime Flexibility**: By changing the encapsulated algorithm at runtime, clients can dynamically adapt their behavior without modifying their code structure.

## Benefits
1. **Encapsulate What Varies**: Strategy Pattern allows you to isolate the parts of your code that change frequently. This way, the variable parts are managed independently and can be easily altered or extended without impacting the stable parts of the code.
2. **Easier Extension and Maintenance**: Since variable behaviors are separated, extending or modifying these behaviors in the future becomes simpler and doesn’t require altering other parts of the code.
