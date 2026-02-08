---
id: 1
title: Define AI-driven Python Todo app constitution
stage: constitution
date: 2026-02-08
surface: agent
model: gemini-1.5-pro
feature: none
branch: main
user: user
command: sp.constitution ## Purpose
Define strict rules for AI-driven, spec-based implementation of a Python console Todo application.

## Role
You are an expert Python software engineer practicing Spec-Driven Development.
You generate code strictly from the provided specification.

## Core Principles
- Spec is the single source of truth
- No assumptions beyond the spec
- No feature creep
- Clarity over cleverness

## Implementation Rules
- Do NOT add features not explicitly defined in the spec
- Do NOT write explanatory text inside the code
- Do NOT use external libraries
- Do NOT use file system or databases
- Store all data in memory only

## Technical Constraints
- Language: Python 3.13
- Application type: Console-based (CLI)
- Architecture: Simple procedural or function-based design
- No classes unless required by the spec

## Human Constraints
- Human will NOT write or edit code manually
- All changes must be done by refining the spec only

## Output Requirements
- A single runnable Python application
- Clear console menu
- Clean, readable, beginner-friendly code
- Error handling for invalid input

## Quality Bar
- Code must run without errors
- Features must exactly match acceptance criteria
- No over-engineering
labels: ["constitution", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:

---

## Prompt

sp.constitution ## Purpose
Define strict rules for AI-driven, spec-based implementation of a Python console Todo application.

## Role
You are an expert Python software engineer practicing Spec-Driven Development.
You generate code strictly from the provided specification.

## Core Principles
- Spec is the single source of truth
- No assumptions beyond the spec
- No feature creep
- Clarity over cleverness

## Implementation Rules
- Do NOT add features not explicitly defined in the spec
- Do NOT write explanatory text inside the code
- Do NOT use external libraries
- Do NOT use file system or databases
- Store all data in memory only

## Technical Constraints
- Language: Python 3.13
- Application type: Console-based (CLI)
- Architecture: Simple procedural or function-based design
- No classes unless required by the spec

## Human Constraints
- Human will NOT write or edit code manually
- All changes must be done by refining the spec only

## Output Requirements
- A single runnable Python application
- Clear console menu
- Clean, readable, beginner-friendly code
- Error handling for invalid input

## Quality Bar
- Code must run without errors
- Features must exactly match acceptance criteria
- No over-engineering

## Response snapshot

Successfully wrote constitution to `.specify/memory/constitution.md`

## Outcome

- ✅ Impact: Constitution defined for project.
- 🧪 Tests: N/A
- 📁 Files: 1 file created.
- 🔁 Next prompts: Begin with `sp.specify` to define the project's first feature.
- 🧠 Reflection: Initial project constitution set up according to user's prompt.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
