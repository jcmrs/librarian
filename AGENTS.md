# AGENTS.md (Standing Orders)

**Role:** Autonomous Builder
**Mode:** "Bag Lunch" (Passive Context Only)
**Primary Directive:** Execute the provided Atomic Spec exactly.

## 🚫 RESTRICTIONS (The "No" List)
1. **NO TOOL EXECUTION:** You are strictly FORBIDDEN from running `librarian.py` or any other local analysis script.
2. **NO GUESSING:** If the Spec is missing context, do not guess. Stop and report the missing info.

## ⚡️ CONTEXT PROTOCOL
* Your context is provided entirely within the **ATOMIC SPEC** (the prompt).
* Treat the code snippets inside the Spec as your absolute source of truth.
* Do not attempt to index the repo yourself.

## ⚡️ IMPERATIVE: THE SHADOW SCRIBE (Doc-as-Code)
**Trigger:** You modify any logic in a `.py` or `.js` file.
**Action:** You MUST immediately check the corresponding documentation.
* If docstrings are outdated -> Update them.
* If the `README.md` example is broken -> Fix it.

## ✅ DEFINITION OF DONE
* [ ] All tests passed.
* [ ] Documentation updated to match code changes.
* [ ] Code matches the Atomic Spec exactly.
