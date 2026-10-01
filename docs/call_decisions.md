# Judgment calls (runbook 🛑 markers)

Recorded decisions for the five-day build. Do not invent values for open cells.

## Call #1 — Data Scientists ESCO / ISCO mapping

**Status:** OPEN

Evidence remains in [`docs/crosswalk.md`](crosswalk.md). Options (a)/(b)/(c) not selected.
Day 4 populate proceeds **O\*NET-only** for occupation individuals until this is decided
(no `mapsToESCO` / ESCO skill necessity edges asserted from crosswalk guesses).

## Call #2 — O\*NET Essential/Transferable vs ESCO essential/optional

**Status:** DECIDED — **(a)**

Keep both distinctions:

| Distinction | Meaning | How modeled |
|---|---|---|
| O\*NET essential vs transferable | Skill *type* (foundational vs portable) | Datatype `onetSkillCategory` + classes `EssentialSkill` / `TransferableSkill` |
| ESCO essential vs optional | Necessity for an *occupation* | Object properties `requiresEssentialSkill` / `requiresOptionalSkill` (subproperties of `requiresSkill`) |

Do **not** map O\*NET `skill_kind` onto `requiresEssentialSkill` / `requiresOptionalSkill`.

## Call #3 — Trust / threshold for derived task→skill edges

**Status:** OPEN (runbook recommendation was (a)+(c): populate all edges weighted by Importance, plus hand-review sample)

Until decided, populate script default: **accept all structural edges**; set `importanceScore` / `confidence` from Importance when present; leave null when absent (no imputation). Hand-review sample already started in [`docs/edge_audit.md`](edge_audit.md).
