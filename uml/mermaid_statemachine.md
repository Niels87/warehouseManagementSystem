::: mermaid


stateDiagram
    [*] --> MainMenu
    MainMenu --> SearchState : Search
    MainMenu --> AddState : Add
    MainMenu --> ExitState : Exit
    SearchState --> MainMenu : Return
    AddState --> MainMenu : Return
    ExitState : Exit

    state MainMenu {
        [*] --> "Display main menu options" #55A3B2
    }
    state SearchState {
        [*] --> "Perform search operation" #87B79E
    }
    state AddState {
        [*] --> "Perform add operation" #C6948E
    }

:::