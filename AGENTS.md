Overwrite the following files with the EXACT content provided below.

FILE: AGENTS.md
# AGENTS.md (Standing Orders)
**Role:** Autonomous Builder
**Mode:** PASSIVE (Bag Lunch Protocol)

## 🚫 RESTRICTIONS
1. **NO TOOL EXECUTION:** You are strictly FORBIDDEN from running `librarian.py`, `pip`, or any local scripts.
2. **NO GUESSING:** If context is missing from the Spec, stop and ask.

## ⚡️ WORKFLOW
1. Read the **ATOMIC SPEC** provided in the issue.
2. Use the code snippets provided in the Spec as your source of truth.
3. Write the code.

## ✅ DEFINITION OF DONE
* Tests pass.
* Docs updated.

FILE: .github/workflows/jules_brain.yml
name: Jules (Listener)
on:
  issues: [opened, edited]
  issue_comment: [created]
permissions:
  contents: write
  issues: write
  pull-requests: write
jobs:
  jules_execute:
    if: contains(github.event.issue.body, '@Jules')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Acknowledge
        env:
          ISSUE_BODY: ${{ github.event.issue.body }}
        run: echo "Jules Online. Waiting for Spec."

FILE: .gitignore
__pycache__/
*.pyc
.env
.cognee_memory/
.DS_Store

FILE: ai_ops/requirements.txt
cognee
litellm
python-dotenv
networkx
lancedb

DELETE FILE: src/utils/test_math.py
