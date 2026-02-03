# 📚 LexiCard: An Intelligent Vocabulary Learning System

LexiCard is a lightweight modular, extensible vocabulary learning application designed to enhance
active recall, retention, and habit-based learning. The system follows solid software engineering principles (SOLID, Clean Architecture) and is built with scalability, testability, and maintainability as first-class concerns. This project serves both as a practical learning tool and a reference implementation for academic and professional software design practices.

Vocabulary acquisition is a critical component of language proficiency, yet traditional memorization techniques lack adaptability and feedback mechanisms. LexiCard addresses this gap by providing an interactive, logic-driven vocabulary learning system that separates concerns between data handling, business logic, and presentation.

---

## 🎓 Purpose

- 🧠 Improve **vocabulary retention** through active recall
- 📖 Separate **word exposure** from **meaning reveal**
- 🧪 Ensure **testability** through isolated components  
- 🔮 Enable **future extensions** without modifying core logic
- 🛠️ Apply **SOLID principles** and Clean Architecture

---
## 🧩 Design Principles & Patterns

### 1️⃣Single Responsibility Principle (SRP)
- <i> A class should have one, and only one, reason to change. </i>

Each class in the system has a single, clearly defined responsibility:

| Component           | Responsibility                                       |
| ------------------- | ---------------------------------------------------- |
| `WordManager`       | Vocabulary logic (selection, known/unknown tracking) |
| `LexicalController` | Application flow & coordination                      |
| `UiManager`         | UI state updates only                                |
| `UI Builders`         | UI construction only                                 |
| `Orchestrators`       | Event wiring only                                    |
| `Data Retrievers`     | Data loading only                                    |
| `Data Savers`         | Persistence only                                     |
| `AudioService`      | Audio playback only                                  |


### 2️⃣ Open/Closed Principle (OCP)
- <i> Software entities should be open for extension, but closed for modification. </i>

Example in LexiCard:
 - To add a new data source (e.g., Database or API), implement a new DataRetriever without changing existing components.


### 3️⃣ Liskov Substitution Principle (LSP)
- <i> Objects of a superclass should be replaceable with objects of a subclass without altering correctness. </i>

Example in LexiCard:
 - Any class implementing <code>IDataRetriever</code> (e.g., CSVDataRetriever, JsonDataRetriever, DatabaseDataRetriever) can be used interchangeably 
without breaking the system, as long as the interface contract is honored.


### 4️⃣ Interface Segregation Principle (ISP)
- <i> Clients should not be forced to depend on interfaces they do not use. </i>

Example in LexiCard:

- Instead of a single large data interface, LexiCard defines small, 
purpose-specific abstractions.
- A read-only retriever does not need to implement save or delete behavior.

| Interface       | Purpose              |
| --------------- | -------------------- |
| `DataRetriever` | Load vocabulary      |
| `DataSaver`     | Persist updates      |
| `DataRemover`   | Remove learned words |


### 5️⃣ Dependency Inversion Principle (DIP)
- <i> High-level modules should not depend on low-level modules. Both should depend on abstractions.</i>

Example in LexiCard:
- <b>High-level modules</b> - LexicalController, WordManager
- <b>Low-level modules</b> - CSV loaders, File writers


- High-level modules depend on interfaces and factories
- Concrete implementations are injected at runtime
  - All concrete dependencies are created in <code>main.py</code>
  - Controllers receive abstractions

### ☑️ Design Pattern Usage in LexiCard

| Pattern                   | Example Classes                                            | Purpose                                                                                        |
| ------------------------- | ---------------------------------------------------------- |------------------------------------------------------------------------------------------------|
| Singleton                 | ResourceLoader                                             | Single instance for resource management.                                                       |
| Factory | DataRetrieverFactory, DataSaverFactory, DataRemoverFactory | Creates and controls the creation of data access objects (retriever, saver, remover) separately. |
| Builder + Director        | DesktopLexiUiBuilder, DesktopUiDirector                    | Construct complex UI in steps, decoupled from controller.                                      |
| Orchestrator              | UiOrchestrator                                             | Connects UI events to controller actions and decouples presentation from logic.              |


---
## ✨ Key Features

- 📚 Vocabulary Flashcards — One word at a time, distraction-free
- 🖥️ Platform-Aware UI Construction - Different operating systems handle different UI
- ⏱️ Timed Meaning Reveal — Meaning appears after a controlled delay
- 🔁 Next Word Navigation — Independent of known/unknown state
- 🧠 Learning State Tracking — Known vs unknown words
- 🧩 Extensible Architecture — Add spaced repetition, analytics, or APIs

---
## 📸 LexiCard App Output (UI Preview)

<img width="254" height="384" alt="image" src="" />

---
## 📌 How It Works

1. Application initializes required services 
2. A **random word** is selected 
3. User attempts recall 
4. ⏳ Meaning is revealed **after a delay**
5. User marks the word as:
   - ✅ Known 
   - ❓ Unknown 
6. System updates learning state and moves forward

---
## 🔧 Core Functionalities

### ✅ WordManager
- Acts as the central business logic unit.
- Decides how vocabulary should be presented and updated during learning sessions.

### ✅ LexicalController
- Coordinates between WordManager, UIManager, and AudioService.
- Decides what should happen when a user interacts with the app.

### ✅ Orchestrator
- Connects UI components with the controller actions.
- Takes actual UI events (button clicks, key presses) and calls the correct LexicalController methods.

### ✅ UI Manager
- Acts as an adapter between controller and UI.
- Decides how UI components reflect the current application state.

### ✅ UI
- Responsible only for rendering visual elements.
- Decides how visual elements are presented to the user.

### ✅ Data Access Layer
- Handles all persistence-related operations.
- Decides how learning progress is stored and updated.

### ✅ AudioService
- Provides audio-related functionality.
- Decide when audio should be played based on instructions.

---
##  🧪 Testing Strategy

- WordManager → business logic tests
- LexicalController → coordination / integration tests


- 🧩 Unit tests for WordManager to validate core business logic.
- 🔗 Unit tests for Controller focus on coordination between components.
- 🔄 Mocked data retrievers, data saver and data remover
- 🛝 Ensure UI-independent logic and event handling are fully tested.

---
##  🔁 CI/CD Pipeline

#### The CI pipeline includes:
 - Dependency installation 
 - Static analysis & linting 
 - Unit test execution 
 - Security scanning 
 - Python package build

Trigger Rules:

- 🔀 All branches → validation & tests 
- 🚀 Main branch → release-ready builds

---

## 📦 Future Enhancements

- 🎨 Modern UI & Language Selection — Allows users to choose which language they want to learn.

- 🔔 Custom Alerts — Notify users about events such as data saving or errors.

- 👤 User Profiles & Progress Tracking — Track individual learning progress over time.

- 📈 Learning Analytics & Reports — Provide insights into user performance and vocabulary mastery.

---

## 🔀 Git Flow Workflow

The project follows a Git Flow–inspired workflow:

- 🌿 master — Stable, production-ready releases
- 🌱 develop — Active development
- ✨ feature/* — New features

---
## 💡 Inspiration

>LexiCard is inspired by active recall and spaced learning techniques widely used in cognitive science.
The project also serves as a demonstration of how clean architecture and SOLID principles can be applied to educational software.