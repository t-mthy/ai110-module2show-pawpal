"""
PawPal+ System — Core Logic Layer
Classes: Task, Pet, Owner, Scheduler
"""

from dataclasses import dataclass, field
from datetime import date, timedelta


# ──────────────────────────────────────────────
# Task — represents a single pet care activity
# ──────────────────────────────────────────────
@dataclass
class Task:
    description: str            # what the task is (e.g. "Morning walk")
    due_date: str               # date string in "YYYY-MM-DD" format
    due_time: str               # time string in "HH:MM" format
    duration_minutes: int       # how long the task takes
    priority: str               # "low", "medium", or "high"
    frequency: str = "once"     # "once", "daily", or "weekly"
    completed: bool = False     # whether the task is done
    pet_name: str = ""          # which pet this task belongs to

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def is_recurring(self):
        """Check if this task repeats (daily or weekly)."""
        return self.frequency in ("daily", "weekly")

    def __repr__(self):
        """Show a short, readable summary of this task."""
        # Build a status tag like "[x]" for done or "[ ]" for pending
        status = "[x]" if self.completed else "[ ]"
        return (
            f"{status} {self.due_time} | {self.description} "
            f"({self.pet_name}, {self.priority}, {self.duration_minutes}min)"
        )


# ──────────────────────────────────────────────
# Pet — stores pet info and its list of tasks
# ──────────────────────────────────────────────
@dataclass
class Pet:
    name: str                   # pet's name
    species: str                # "dog", "cat", etc.
    age: int                    # pet's age in years
    tasks: list = field(default_factory=list)  # list of Task objects

    def add_task(self, task):
        """Add a new task to this pet's task list."""
        # Stamp the task with this pet's name so we know who it belongs to
        task.pet_name = self.name
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return list(self.tasks)

    def get_pending_tasks(self):
        """Return only tasks that are not yet completed."""
        return [task for task in self.tasks if not task.completed]

    def remove_task(self, description):
        """Remove a task by its description. Returns True if found."""
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                return True
        return False


# ──────────────────────────────────────────────
# Owner — manages one or more pets
# ──────────────────────────────────────────────
@dataclass
class Owner:
    name: str                   # owner's name
    pets: list = field(default_factory=list)  # list of Pet objects

    def add_pet(self, pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_pet(self, name):
        """Find and return a pet by name, or None if not found."""
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def get_all_tasks(self):
        """Gather all tasks from every pet into one list."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


# ──────────────────────────────────────────────
# Scheduler — the "brain" that organizes tasks
# ──────────────────────────────────────────────
class Scheduler:
    def __init__(self, owner):
        """Create a scheduler linked to an owner."""
        self.owner = owner      # the Owner whose pets we manage

    def get_daily_schedule(self, target_date):
        """Get all tasks for a specific date, sorted by time."""
        # Grab every task across all pets
        all_tasks = self.owner.get_all_tasks()
        # Keep only tasks that match the target date
        daily = [t for t in all_tasks if t.due_date == target_date]
        # Return them sorted earliest-first
        return self.sort_by_time(daily)

    def sort_by_time(self, tasks):
        """Sort a list of tasks by their due_time (earliest first)."""
        # "HH:MM" strings sort correctly in alphabetical order
        return sorted(tasks, key=lambda t: t.due_time)

    def sort_by_priority(self, tasks):
        """Sort tasks by priority (high -> medium -> low)."""
        # Map each priority level to a number so "high" comes first
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(tasks, key=lambda t: priority_order.get(t.priority, 3))

    def filter_by_status(self, tasks, completed):
        """Filter tasks by completion status (True or False)."""
        return [t for t in tasks if t.completed == completed]

    def filter_by_pet(self, tasks, pet_name):
        """Filter tasks to only show ones for a specific pet."""
        return [t for t in tasks if t.pet_name == pet_name]

    def detect_conflicts(self, tasks):
        """Find tasks that overlap in time and return warning messages."""
        # Placeholder — full logic coming in Phase 3 (Algorithmic Layer)
        warnings = []
        return warnings

    def handle_recurrence(self, task):
        """If a task is recurring, create the next occurrence."""
        # Placeholder — full logic coming in Phase 3 (Algorithmic Layer)
        return None

    def find_next_available_slot(self, tasks, duration, target_date):
        """Find the next open time slot of a given duration."""
        # Placeholder — full logic coming in Phase 7 (Advanced)
        return None
