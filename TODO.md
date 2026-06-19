# TODO - AI Study Planner (prolevel)

## Step 1: Upgrade implementation
- [ ] Replace stub in `study_planner_ai/study_planner_ai.py` with a full CLI app.
- [ ] Implement persistence to `study_planner_ai/.study_planner_state.json`.
- [ ] Implement spaced-repetition inspired scheduling (SM-2 style) and session generation.
- [ ] Add commands: `init`, `add-topic`, `plan`, `next-sessions`, `review-log`, `export`.

## Step 2: Improve code quality
- [ ] Add type hints, dataclasses, validation, and structured logging.
- [ ] Implement helpful `--help` output and consistent JSON/CSV export.

## Step 3: Update docs & dependencies
- [ ] Update `study_planner_ai/README.md` with CLI examples.
- [ ] Update `study_planner_ai/requirements.txt` to minimal dependencies (prefer standard library).

## Step 4: Add tests
- [ ] Add `study_planner_ai/test_study_planner_ai.py` using unittest.
- [ ] Tests cover load/save, scheduling determinism, and basic CLI-less function behavior.

## Step 5: Verify
- [ ] Run unit tests.
- [ ] Smoke test key commands (`--help`, `init`, `add-topic`, `plan`).

