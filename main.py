"""
PawPal+ CLI Demo Script
────────────────────────
This script is a "playground" that creates sample data and
prints a readable daily schedule to the terminal.
It verifies that our backend logic works before we touch the UI.
"""

from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date


def main():
    # ── Today's date as a string (used for all tasks below) ──
    today = date.today().isoformat()  # e.g. "2026-03-27"

    # ──────────────────────────────────────────
    # Step 1: Create an Owner
    # ──────────────────────────────────────────
    owner = Owner(name="Jordan")
    print(f"Owner created: {owner.name}\n")

    # ──────────────────────────────────────────
    # Step 2: Create two Pets and register them
    # ──────────────────────────────────────────
    mochi = Pet(name="Mochi", species="dog", age=3)
    whiskers = Pet(name="Whiskers", species="cat", age=5)

    owner.add_pet(mochi)
    owner.add_pet(whiskers)
    print(f"Pets registered: {mochi.name} ({mochi.species}), "
          f"{whiskers.name} ({whiskers.species})\n")

    # ──────────────────────────────────────────
    # Step 3: Add Tasks (intentionally out of order)
    # ──────────────────────────────────────────
    # Mochi's tasks
    mochi.add_task(Task(
        description="Evening walk",
        due_date=today, due_time="17:30",
        duration_minutes=30, priority="medium"
    ))
    mochi.add_task(Task(
        description="Morning walk",
        due_date=today, due_time="07:00",
        duration_minutes=30, priority="high", frequency="daily"
    ))
    mochi.add_task(Task(
        description="Flea medication",
        due_date=today, due_time="09:00",
        duration_minutes=5, priority="high"
    ))

    # Whiskers' tasks
    whiskers.add_task(Task(
        description="Breakfast feeding",
        due_date=today, due_time="07:30",
        duration_minutes=10, priority="high", frequency="daily"
    ))
    whiskers.add_task(Task(
        description="Litter box cleaning",
        due_date=today, due_time="12:00",
        duration_minutes=10, priority="medium"
    ))

    # ──────────────────────────────────────────
    # Step 4: Build and display the daily schedule
    # ──────────────────────────────────────────
    scheduler = Scheduler(owner)
    schedule = scheduler.get_daily_schedule(today)

    # Print a nicely formatted schedule
    print("=" * 55)
    print(f"  PawPal+ Daily Schedule — {today}")
    print("=" * 55)
    print(f"  {'Time':<8} {'Task':<22} {'Pet':<10} {'Priority':<8}")
    print("-" * 55)

    for task in schedule:
        print(f"  {task.due_time:<8} {task.description:<22} "
              f"{task.pet_name:<10} {task.priority:<8}")

    print("=" * 55)
    print(f"  Total tasks: {len(schedule)}")
    print()

    # ──────────────────────────────────────────
    # Step 5: Test mark_complete on a task
    # ──────────────────────────────────────────
    first_task = schedule[0]
    print(f"Completing task: \"{first_task.description}\" ... ", end="")
    first_task.mark_complete()
    print(f"Done! (completed = {first_task.completed})")

    # Show remaining pending tasks
    pending = scheduler.filter_by_status(
        scheduler.get_daily_schedule(today), completed=False
    )
    print(f"Pending tasks remaining: {len(pending)}\n")

    # ──────────────────────────────────────────
    # Step 6: Filter tasks by pet
    # ──────────────────────────────────────────
    all_tasks = owner.get_all_tasks()
    mochi_tasks = scheduler.filter_by_pet(all_tasks, "Mochi")
    whiskers_tasks = scheduler.filter_by_pet(all_tasks, "Whiskers")
    print(f"Mochi's tasks:    {len(mochi_tasks)}")
    print(f"Whiskers' tasks:  {len(whiskers_tasks)}")


if __name__ == "__main__":
    main()
