# Software Principles

Software principles establish the foundations we rely on to make our code more readable, understandable, and writable. These principles serve as the cornerstone for enhancing the clarity and quality of our written code.

These principles are as follows:

## Seperation of Concerns (SoC)

Different components should be positioned separately from each other. For example, the login process, comment model, and product structures should be positioned independently. This way, when developing our application or modifying an existing module, we can advance the development process without disrupting or touching other structures, ensuring that we maintain code integrity. By minimizing dependency structures, we can focus on the task at hand and elevate code quality to a high level.

Here I have shown an example made without following my principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/SoC/BadCode/bad_example.py).

Here, too, I have shown how we get better results when we follow the principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/SoC/GoodCode/good_example.py).

## Don't Repeat Yourself (DRY)

The repetition of code not only makes it difficult to read but also complicates it. To prevent this, we should avoid code duplication. By applying this principle, we enhance the maintainability, readability, and testability of our code. This principle also nods to the single-responsibility principle.

Here I have shown an example made without following my principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/DRY/BadCode/bad_example.py).

Here, too, I have shown how we get better results when we follow the principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/DRY/GoodCode/good_example.py).

## Keep It Simple Stupid (KISS)

KISS, a principle emphasizing the pursuit of simplicity. It suggests that a system works well when it is simple, and simplicity is more effective than complexity. When writing code, it's essential to steer clear of complex structures and aim for 'smart,' meaning simplicity. I summarize this principle as follows: 'If you can explain what you're doing to a 5-year-old, you truly understand the task at hand.

Here I have shown an example made without following my principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/KISS/BadCode/bad_example.py).

Here, too, I have shown how we get better results when we follow the principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/KISS/GoodCode/good_example.py).

# SOLID Principles

SOLID is a set of principles initiated by Robert C. Martin and further developed by Michael Feathers. It aims to facilitate the development of software in a maintainable, sustainable, understandable, and flexible manner. This principle assists us in reducing complexity as the project grows. It complements and works in harmony with Object-Oriented Programming (OOP), enhancing each other's capabilities for cohesive functionality.

The following five concepts make up our SOLID principles:

## Single Responsibility Principle (SRP)

It advocates that a component should have only one responsibility, aiming for a single reason to change when the component needs modification. If a function serves multiple purposes (has multiple responsibilities), it violates this principle. Failure to adhere to this principle means that when there are parts of the code that need modification, we would have to change multiple places in the functions we wrote. This not only extends the coding and maintenance processes but also increases costs. In short, a function should have one responsibility. Decreasing responsibility also means easier adaptation to change.

Here I have shown an example made without following my principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/SOLID_Examples/1.SRP/BadCode/bad_example.py).

Here, too, I have shown how we get better results when we follow the principle. [GitHub Pages](https://github.com/ulasgulhan/Software_Principles/blob/main/Principles_Examples/SOLID_Examples/1.SRP/GoodCode/good_example.py).

## Open/Closed Principle (OCP)

A class or function should be open for extension but closed for modification. It should preserve existing features while allowing for the addition of new ones. When adding something new to the project, we should extend our functions with minimal (simple) modifications, without altering their existing features. By adhering to this principle, as your project grows, you can easily keep track of and understand the functions without extensive changes to their core functionalities.

## Liskov Substitution Principle (LSP)

The Liskov Substitution Principle (LSP) is a key concept in object-oriented programming, emphasizing that derived classes should be substitutable for their base classes. In practical terms, if a program uses a base class, it should seamlessly work with any derived class without causing issues. This means that the behavior of the derived class should align with the expected behavior of the base class, ensuring that substituting one for the other does not compromise the correctness of the program. The principle emphasizes behavioral compatibility, avoiding the strengthening of preconditions and weakening of postconditions in derived classes compared to their base classes.

## Interface Segregation Principle (ISP)

Instead of using a single interface for all purposes, it is recommended to use multiple interfaces based on usage scenarios. This principle suggests using a separate interface for each responsibility, allowing users to choose a specific interface for a particular purpose. This principle operates on a logic similar to the Single Responsibility Principle (SRP), with the difference that the Interface Segregation Principle (ISP) focuses on interfaces, while SRP addresses classes and functions.

## Dependency Inversion Principle (DIP)

This principle aims to minimize the dependencies of classes that use a class when its properties change. It advocates that the superclass should not be dependent on the subclass. When there is a change in the superclass, the subclass should adapt to this change. However, when a change is made in the subclass, it should not affect the superclass. To prevent this, an abstraction concept is usually introduced between the higher-level and lower-level classes.

