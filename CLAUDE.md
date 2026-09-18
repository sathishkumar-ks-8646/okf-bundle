# Zoho Analytics OKF bundle - agent instructions

Read `agent-guide/README.md` before changing anything; it routes every kind of change to a playbook.

The one rule: **never edit `bundle/` or `dist/` by hand.** Both are generated. Change the inputs
(`handwritten/`, or the configuration tables in `tools/build_okf.py`), then run:

```bash
python3 tools/build_okf.py        # analytics-api-docs + handwritten -> bundle/
python3 tools/validate_okf.py     # must end with errors=0 warnings=0 broken_links=0
git diff --stat bundle/           # review what the rebuild changed
```

`analytics-api-docs/` is a git submodule, not a folder of this repository. API facts are edited in the
analytics-api-docs repository; here you only move the pin
(`git submodule update --remote --merge analytics-api-docs`) and rebuild. Run
`git submodule update --init` once after cloning or the builder stops with an explanatory error.

Package for publishing only when asked: `python3 tools/package_okf.py --tarball --version X.Y.Z`
(see `agent-guide/06-rules-and-release-checklist.md`). Nothing in this repository pushes to a remote.
