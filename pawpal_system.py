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
        pass

    def is_recurring(self):
        """Check if this task repeats (daily or weekly)."""
        pass


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
        pass

    def get_tasks(self):
        """Return all tasks for this pet."""
        pass

    def get_pending_tasks(self):
        """Return only tasks that are not yet completed."""
        pass

    def remove_task(self, description):
        """Remove a task by its description. Returns True if found."""
        pass


# ──────────────────────────────────────────────
# Owner — manages one or more pets
# ──────────────────────────────────────────────
@dataclass
class Owner:
    name: str                   # owner's name
    pets: list = field(default_factory=list)  # list of Pet objects

    def add_pet(self, pet):
        """Add a pet to the owner's list."""
        pass

    def get_pet(self, name):
        """Find and return a pet by name."""
        pass

    def get_all_tasks(self):
        """Gather all tasks from every pet into one list."""
        pass


# ──────────────────────────────────────────────
# Scheduler — the "brain" that organizes tasks
# ──────────────────────────────────────────────
class Scheduler:
    def __init__(self, owner):
        """Create a scheduler linked to an owner."""
        self.owner = owner      # the Owner whose pets we manage

    def get_daily_schedule(self, target_date):
        """Get all tasks for a specific date, sorted by time."""
        pass

    def sort_by_time(self, tasks):
        """Sort a list of tasks by their due_time (earliest first)."""
        pass

    def sort_by_priority(self, tasks):
        """Sort tasks by priority (high -> medium -> low)."""
        pass

    def filter_by_status(self, tasks, completed):
        """Filter tasks by completion status (True or False)."""
        pass

    def filter_by_pet(self, tasks, pet_name):
        """Filter tasks to only show ones for a specific pet."""
        pass

    def detect_conflicts(self, tasks):
        """Find tasks that overlap in time and return warning messages."""
        pass

    def handle_recurrence(self, task):
        """If a task is recurring, create the next occurrence."""
        pass

    def find_next_available_slot(self, tasks, duration, target_date):
        """Find the next open time slot of a given duration."""
        pass
