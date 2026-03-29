"""
PawPal+ Test Suite
──────────────────
Basic tests to verify core system behavior.
Run with:  pytest tests/ -v
"""

import sys
import os

# Add the project root to the path so we can import pawpal_system
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Owner, Scheduler


# ──────────────────────────────────────────────
# Test 1: Task completion
# ──────────────────────────────────────────────
def test_task_mark_complete():
    """Calling mark_complete() should set completed to True."""
    task = Task(
        description="Morning walk",
        due_date="2026-03-29", due_time="07:00",
        duration_minutes=30, priority="high"
    )
    # Task starts as not completed
    assert task.completed is False
    # After marking complete, it should be True
    task.mark_complete()
    assert task.completed is True


# ──────────────────────────────────────────────
# Test 2: Adding tasks to a pet
# ──────────────────────────────────────────────
def test_pet_add_task_increases_count():
    """Adding a task to a Pet should increase the pet's task count."""
    pet = Pet(name="Mochi", species="dog", age=3)
    # Pet starts with zero tasks
    assert len(pet.get_tasks()) == 0

    # Add one task — count should become 1
    pet.add_task(Task(
        description="Walk",
        due_date="2026-03-29", due_time="07:00",
        duration_minutes=30, priority="high"
    ))
    assert len(pet.get_tasks()) == 1

    # Add another — count should become 2
    pet.add_task(Task(
        description="Feeding",
        due_date="2026-03-29", due_time="08:00",
        duration_minutes=10, priority="medium"
    ))
    assert len(pet.get_tasks()) == 2
