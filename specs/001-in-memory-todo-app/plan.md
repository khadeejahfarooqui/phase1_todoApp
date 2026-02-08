# Phase I – In-Memory Console Todo App - Technical Plan

## 1. Scope and Dependencies
- **In Scope**:
    - Generation of a Python console-based Todo application.
    - Implementation of Add, View, Update, Delete, and Toggle Complete/Incomplete Todo functionalities.
    - In-memory storage for Todo items.
    - Menu-driven user interface.
    - Input validation and error handling for menu options and Todo IDs.
    - Auto-incrementing ID for Todo items.
- **Out of Scope**:
    - Persistence of data (e.g., file system, database).
    - External libraries.
    - Network calls.
    - Advanced UI features (e.g., sorting, filtering).
- **External Dependencies**: None, as per Constitution and Spec.

## 2. Key Decisions and Rationale
- **Menu-driven CLI vs direct commands**:
    - **Decision**: Menu-driven CLI.
    - **Rationale**: Provides a clear and intuitive user experience for a beginner-friendly console application, as outlined in the objective.
- **In-memory storage vs database/file system**:
    - **Decision**: In-memory storage.
    - **Rationale**: Explicitly stated in the "Technology Constraints" of the Spec and "Implementation Rules" of the Constitution for Phase I.
- **Procedural functions vs classes**:
    - **Decision**: Procedural functions.
    - **Rationale**: Aligns with the "Architecture: Simple procedural or function-based design" constraint in the Constitution and promotes beginner-friendly readability.
- **Single script structure**:
    - **Decision**: Single Python script (`src/main.py`).
    - **Rationale**: Simplifies project structure for a console-based application and adheres to the "Single runnable Python application" output requirement.

## 3. Interfaces and API Contracts
- **Internal API (Functions)**:
    - `add_todo()`:
        - **Inputs**: User input for title (string) and description (string).
        - **Outputs**: None (modifies in-memory list), displays confirmation message.
        - **Errors**: Handles empty title/description.
    - `view_todos()`:
        - **Inputs**: None.
        - **Outputs**: Prints formatted list of todos to console.
        - **Errors**: Displays "No todos" message if list is empty.
    - `update_todo()`:
        - **Inputs**: User input for Todo ID (integer), new title (string), new description (string).
        - **Outputs**: None (modifies in-memory list), displays confirmation message.
        - **Errors**: Handles invalid Todo ID, empty title/description.
    - `delete_todo()`:
        - **Inputs**: User input for Todo ID (integer).
        - **Outputs**: None (modifies in-memory list), displays confirmation message.
        - **Errors**: Handles invalid Todo ID.
    - `toggle_complete()`:
        - **Inputs**: User input for Todo ID (integer).
        - **Outputs**: None (modifies in-memory list), displays confirmation message.
        - **Errors**: Handles invalid Todo ID.
    - `main_menu()`:
        - **Inputs**: User input for menu choice (integer).
        - **Outputs**: Calls corresponding function or exits.
        - **Errors**: Handles invalid menu choice.

## 4. Non-Functional Requirements (NFRs) and Budgets
- **Performance**:
    - Minimal latency for console interactions (user perception).
    - Efficient in-memory operations for small to medium Todo lists (due to in-memory constraint).
- **Reliability**:
    - Application must not crash on invalid input (menu, Todo ID).
    - Consistent behavior across all functional requirements.
- **Security**: N/A for Phase I (no sensitive data, no external access).
- **Cost**: N/A (local console application).

## 5. Data Management and Migration
- **Source of Truth**: The in-memory Python list of Todo dictionaries/objects.
- **Schema Evolution**: N/A for Phase I (no persistence, schema is fixed in memory for runtime).
- **Migration and Rollback**: N/A (no persistence).
- **Data Retention**: Data exists only for the duration of the application's runtime. Upon exit, all data is lost.

## 6. Operational Readiness
- **Observability**: Console output will serve as the primary observability mechanism, displaying current Todo list state and error messages.
- **Alerting**: N/A (local console application).
- **Runbooks**: N/A (simple console application).
- **Deployment and Rollback strategies**: N/A (single Python script, no deployment infrastructure).
- **Feature Flags and compatibility**: N/A.

## 7. Risk Analysis and Mitigation
- **Top 3 Risks**:
    1.  **Incorrect ID management**: If Todo IDs are not unique or properly managed, it could lead to data corruption or incorrect operations.
        -   **Mitigation**: Implement a simple auto-incrementing counter for IDs and ensure checks for existing IDs before use/modification.
    2.  **Graceful error handling**: Failure to handle invalid user input (e.g., non-integer input for ID, out-of-range menu options) could lead to application crashes.
        -   **Mitigation**: Implement `try-except` blocks for input conversions and explicit checks for valid ranges/existence.
    3.  **Code complexity/readability**: As more features are added, maintaining beginner-friendly readability in a single script can become challenging.
        -   **Mitigation**: Adhere to clear function separation, consistent naming conventions, and concise code as per Constitution. Refactoring can be considered in later phases if necessary.

## 8. Evaluation and Validation
- **Definition of Done (tests, scans)**:
    - All functional requirements from `specs/001-in-memory-todo-app/spec.md` are met.
    - All acceptance criteria pass during manual console testing.
    - Application runs without errors and handles invalid input gracefully.
    - Code adheres to Python 3.13 syntax and best practices for readability.
- **Output Validation**:
    - Console output for viewing todos is clear, well-formatted, and accurately reflects the in-memory state.
    - Error messages are user-friendly and informative.
