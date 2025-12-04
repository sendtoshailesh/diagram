# Mermaid Diagram Examples

Mermaid renders in GitHub, GitLab, Notion, and many markdown viewers.

## Flowchart
```mermaid
graph TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> B
    C --> E[End]
```

## Sequence Diagram
```mermaid
sequenceDiagram
    participant User
    participant API
    participant Database
    
    User->>API: Request data
    API->>Database: Query
    Database-->>API: Results
    API-->>User: Response
```

## Class Diagram
```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +String breed
        +bark()
    }
    class Cat {
        +meow()
    }
    Animal <|-- Dog
    Animal <|-- Cat
```

## Gantt Chart
```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Planning
    Requirements    :a1, 2024-01-01, 7d
    Design         :a2, after a1, 5d
    section Development
    Backend        :a3, after a2, 10d
    Frontend       :a4, after a2, 12d
    section Testing
    QA Testing     :a5, after a4, 5d
```

## To render as image:
Use Mermaid CLI: `mmdc -i diagram.mmd -o diagram.png`
Or use online editor: https://mermaid.live
