# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial UML design included four classes: Task, Pet, Owner, and Scheduler. Task holds the details of a single care activity (description, time, priority, etc.). Pet stores info about one animal and keeps a list of its tasks. Owner manages a list of pets and can pull all tasks together. Scheduler is the "brain"; it takes the Owner and uses its data to sort, filter, and organize tasks across all pets. The relationships were straightforward: an Owner has many Pets, each Pet has many Tasks, and the Scheduler connects to one Owner.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes. The biggest change was adding a `mark_task_complete()` method to the Scheduler class. Originally, the plan was to just call `task.mark_complete()` directly on the Task. But when recurring tasks were added, I needed something that could mark the task done and automatically create the next occurrence in one step. Putting this in the Scheduler made sense because it already has access to the Owner and all the Pets, so it can find the right pet and add the new task to it. Two private helper methods (`_time_to_minutes` and `_minutes_to_time`) were also added to support the time math needed for conflict detection.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers three main constraints: time (when the task is due), priority (high, medium, or low), and duration (how long the task takes). Time matters most because a pet owner needs to follow a chronological plan throughout the day. You can't feed a pet at 7 AM if you haven't gotten up yet. Priority is used as a secondary sort so the owner can quickly see what's most urgent. Duration is used for conflict detection, knowing how long a task takes tells us whether two tasks actually overlap.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The conflict detection compares consecutive tasks in time order, which means it only catches overlaps between neighbors. Not, say, a really long task that spans three others. This is a tradeoff between simplicity and completeness. It's reasonable here because most pet care tasks are short (5-60 minutes), so the neighbor-comparison approach catches the vast majority of real conflicts. A full "every-pair" comparison would be more thorough but harder to read and slower, and it's overkill for a daily pet care schedule.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

AI (Claude Code) was used as a development partner/copilot throughout the entire project. It helped with brainstorming the class structure, writing the UML diagram in Mermaid.js, scaffolding class skeletons with dataclasses, implementing the full method logic, building the test suite, and wiring up the Streamlit UI. The most helpful approach was working phase-by-phase. It gives clear instructions for what to build in each step, then reviewing the output before moving on. This made it easy to catch issues early instead of fixing a huge pile of code at the end.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When building the project phases, the AI suggested reordering the phases so that all backend logic (core classes + algorithms) was finished and tested before any UI work. The original plan had UI integration (Phase 3) happening before the algorithms (Phase 4), which would have meant revisiting the UI later to add sorting, conflict warnings, and recurrence features. The reordering made sense because it avoids double work on `app.py`, so the suggestion was accepted after thinking through the dependency chain. Every piece of code was also verified by running `python main.py` for the CLI demo and `pytest tests/ -v` for the test suite before moving on.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

The test suite has 16 tests across five areas: core class behavior (task completion, adding tasks, pending filter, cross-pet aggregation), sorting correctness (by time and by priority), recurrence logic (daily +1 day, weekly +7 days, one-time tasks creating nothing), conflict detection (overlapping tasks flagged, non-overlapping tasks clean), and edge cases (empty lists, pets with no tasks). These tests are important because they cover the main "promises" the system makes. If sorting is wrong, the daily schedule is useless. If recurrence is broken, tasks silently disappear. If conflict detection fails, the owner double-books themselves. Additional tests were created for the stretch features to test next available slot functionalities.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

Confidence: 4 out of 5 stars. The core logic is solid and well-tested. If there were more time, the next edge cases to test would be: a task with 0 duration (does conflict detection handle it?), tasks that span midnight, two tasks at the exact same time with the same description, and Streamlit session state behavior (does the Owner actually persist across reruns?).

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The "CLI-first" workflow worked really well. Building and verifying all the backend logic in `main.py` before touching the Streamlit UI meant the UI was just a thin layer on top of already-working code. There was no "it works in the terminal but breaks in the app" moment. The conflict detection and recurring task features also came together cleanly. They feel like real, useful features rather than just checkboxes.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

The conflict detection could be smarter. Right now, it only compares neighboring tasks. So a very long task that overlaps multiple later tasks would only flag the first conflict. Also, the Streamlit UI could benefit from a visual timeline or calendar view instead of just tables. Finally, adding persistent storage (like a simple JSON file or SQLite database) would make the app actually useful between sessions, since right now everything resets when the Streamlit server restarts.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

Designing the system on paper first (the UML diagram) before writing any code saved a lot of time. It forced clear thinking about what each class is responsible for and how they connect. When it came time to code, most of the hard decisions were already made. Working with AI phase-by-phase also helped. Instead of asking for the whole project at once, breaking it into small, reviewable pieces made it much easier to understand what was being built and catch problems early.
