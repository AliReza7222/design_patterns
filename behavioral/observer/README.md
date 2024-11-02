# Observer Pattern

The Observer Pattern is a behavioral design pattern that establishes a one-to-many dependency between objects. It allows a single object, known as the *subject*, to maintain a list of *observers* that are automatically notified whenever the subject’s state changes. This keeps observers synchronized with the subject without requiring them to actively query it.

![Observer-Pattern](img1.png)

This pattern is ideal for scenarios where multiple components need to be updated automatically in response to changes in a single, central object, making it useful for designing reactive and modular systems.


## 📘 Definition
The Observer Pattern allows an object (the *subject*) to notify multiple dependent objects (the *observers*) about state changes. By creating this one-to-many dependency, observers can automatically stay up-to-date with the subject’s state.

## ✨ Key Features

- **One-to-Many Relationship**: This pattern supports a one-to-many relationship where a single subject can have multiple observers. Any change in the subject’s state triggers an update to all observers, who can then respond accordingly.

- **Loose Coupling**: Observers and the subject are loosely coupled, meaning the subject doesn’t need to know specifics about the observers. Observers subscribe to the subject for updates, and each can process updates independently.

- **Automatic Updates**: When the subject's state changes, all registered observers are automatically notified, allowing them to stay in sync without constant monitoring.

- **Open for Extension, Closed for Modification**: This pattern enables adding or removing observers dynamically without altering the subject’s code. This supports the "open/closed" principle, allowing new observers to be added without modifying core logic.

## 🎯 Benefits

- **Consistency Across Dependents**: Observers receive updates in real time, ensuring all dependent objects have the latest information upon any change in the subject's state.

- **Modularity and Scalability**: The pattern enables easy addition or removal of observers without modifying the subject’s core logic, supporting system growth as more observers subscribe when needed.

- **Separation of Concerns**: Observers handle their own updates, allowing the subject to focus solely on managing its state. This separation enhances code clarity and reduces error risks.

- **Reduced Maintenance Costs**: Thanks to loose coupling, changes in the subject or an observer don’t directly impact each other, making the codebase easier to maintain and extend.

---

## ➡️ Push and Pull in the Observer Pattern

The Observer Pattern can support *push* and *pull* models, adding flexibility to how data is shared with observers:

- **Push Model**: In the push model, the subject sends data directly to observers when it notifies them. This approach is more proactive, as the subject determines what information observers need and sends it with each notification. It's efficient when observers need specific data immediately.

- **Pull Model**: In the pull model, the subject only notifies observers of a change, but it’s up to each observer to retrieve the necessary data from the subject. This approach allows observers to pull the exact data they need, but it may introduce a slight delay as observers query the subject.

Combining both models is also possible, enabling observers to choose whether they want data directly pushed to them or to pull it as needed. This dual approach provides flexibility based on observer requirements and system design.

## 🔄 Similarity to the Publish/Subscribe Pattern

The Observer Pattern is often compared to the *Publish/Subscribe* (or *Pub/Sub*) pattern, as both facilitate communication between objects. Here are some key similarities and differences:

![Pub/Sub](img2.png)

- **Similarities**: Both patterns allow multiple components to receive updates based on events. In both patterns, components register their interest to be notified of specific changes.

- **Differences**:
  - In the Observer Pattern, observers are directly linked to the subject. This direct connection makes it suitable for scenarios where the subject needs to notify specific observers directly.

  - In contrast, the Publish/Subscribe pattern introduces a messaging broker or event bus. This addition further decouples publishers and subscribers, allowing for greater flexibility.

  - The Observer Pattern is typically implemented synchronously. This means that when an event occurs, the subject directly calls the appropriate method of all its observers.

  - On the other hand, the Publish/Subscribe pattern is often implemented asynchronously, often using a message queue. This allows subscribers to receive updates independently from the publisher.

  - As a result, the Publish/Subscribe pattern is more scalable and is ideal for distributed systems. In contrast, the Observer Pattern is generally used within a single application.
