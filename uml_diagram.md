# PawPal+ UML Class Diagram

```mermaid
classDiagram
    direction LR

    class Owner {
        +str name
        +list~Pet~ pets
        +add_pet(pet: Pet) None
        +get_pet(name: str) Pet
        +get_all_tasks() list~Task~
    }

    class Pet {
        +str name
        +str species
        +int age
        +list~Task~ tasks
        +add_task(task: Task) None
        +get_tasks() list~Task~
        +get_pending_tasks() list~Task~
        +remove_task(description: str) bool
    }

    class Task {
        +str description
        +str due_date
        +str due_time
        +int duration_minutes
        +str priority
        +str frequency
        +bool completed
        +str pet_name
        +mark_complete() None
        +is_recurring() bool
    }

    class Scheduler {
        +Owner owner
        +get_daily_schedule(date: str) list~Task~
        +sort_by_time(tasks: list) list~Task~
        +sort_by_priority(tasks: list) list~Task~
        +filter_by_status(tasks, completed) list~Task~
        +filter_by_pet(tasks, pet_name) list~Task~
        +detect_conflicts(tasks: list) list~str~
        +handle_recurrence(task: Task) Task
        +mark_task_complete(task: Task) Task
        +find_next_available_slot(tasks, duration, date) str
        -_time_to_minutes(time_str: str) int
        -_minutes_to_time(total_minutes: int) str
    }

    Owner "1" --> "*" Pet : owns
    Pet "1" --> "*" Task : has
    Scheduler "1" --> "1" Owner : manages
```

## Relationships
- **Owner** owns one or more **Pets** (one-to-many)
- **Pet** has zero or more **Tasks** (one-to-many)
- **Scheduler** manages one **Owner** and operates across all their pets' tasks

## Changes from Initial Design
- Added `mark_task_complete()` to Scheduler — a convenience method that marks a task done and automatically handles recurrence in one step.
- Added private helper methods `_time_to_minutes()` and `_minutes_to_time()` to Scheduler — used internally by conflict detection and the upcoming next-available-slot feature.
