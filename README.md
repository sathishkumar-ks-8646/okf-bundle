# Zoho Analytics REST API v2 - OKF bundle sources

This repository holds everything needed to **generate, validate and package** the Open Knowledge
Format (OKF v0.2) bundle for the Zoho Analytics REST API v2: a pinned reference to the API source
documents, the hand-written concept files, the generator scripts, the generated bundle, and the guide
that tells an AI agent (or a human) how to update all of it when the API changes.

The public artefact - the folder that is pushed to the public GitHub repository - is **not** stored
here. It is produced into `dist/` (git-ignored) by `tools/package_okf.py`.

## Layout

| Folder | Role | Edited by hand? |
|---|---|---|
| [`analytics-api-docs/`](analytics-api-docs/README.md) | **Input.** API reference markdown, OpenAPI specs, SDK samples and the common JSON. A **git submodule** of the [analytics-api-docs](https://github.com/sathish-dev-git/analytics-api-docs) repository, pinned to one commit and tracking `main`. | **Not here.** Edit in that repository, then move the pin (below). |
| [`handwritten/`](handwritten/README.md) | **Input.** Cross-cutting concepts no API document provides: foundations, workflow playbooks, the bundle overview. Copied into the bundle on every build. | Yes. |
| [`tools/`](tools/README.md) | Generator (`build_okf.py`), validator (`validate_okf.py`), packager (`package_okf.py`). | Only the configuration tables in `build_okf.py`, in normal operation. |
| `bundle/` | **Output.** The generated OKF bundle (manifest name `zoho-analytics-rest-api-v2`). Deleted and rebuilt on every build. Committed so that every rebuild appears as a reviewable diff. | **Never.** |
| `dist/` | **Output, git-ignored.** Public repository layout (`README.md`, `llms.txt`, `okf/`, CI workflow) plus the release tarball. | Never. |
| [`agent-guide/`](agent-guide/README.md) | Maintainer manual for agents and humans: layout, bundle structure, source format, change playbooks, builder internals, release checklist. | Yes, when the process itself changes. |

`CLAUDE.md` is a short pointer so that an AI coding agent opening this repository lands on the guide.

## Pipeline

```
analytics-api-docs/**  (submodule) ─┐
handwritten/**                     ─┴─►  tools/build_okf.py ──►  bundle/  ──►  tools/validate_okf.py  ──►  tools/package_okf.py  ──►  dist/zoho-analytics-okf/
                                                              errors=0 broken_links=0                                   push to the public repo
```

## Quick start

Python 3.8+, standard library only. Run from the repository root.

```bash
git submodule update --init                # fetch analytics-api-docs at the pinned commit (once per clone)
python3 tools/build_okf.py                 # prints endpoints=… groups=… errors=… sdk=…
python3 tools/validate_okf.py              # must end with errors=0 warnings=0 broken_links=0
python3 tools/package_okf.py --tarball --version X.Y.Z    # URLs come from the DEFAULT_* constants in the packager
```

## Updating the bundle for an API change

1. Land the change in the analytics-api-docs repository first (its validator must pass), then move the
   pin here to the commit you want to build from:

   ```bash
   git submodule update --remote --merge analytics-api-docs   # pin -> tip of main
   git diff --submodule                                       # the upstream commits that came in
   ```

   The build regenerates the whole bundle from whatever the pinned commit holds.
2. Follow the matching playbook in [agent-guide/04-change-playbooks.md](agent-guide/04-change-playbooks.md)
   (new endpoint, changed attribute, new error code, new domain, deprecated endpoint...).
3. Build and validate. Fix any `WARN` lines the builder prints (title mismatches between markdown and
   OpenAPI are the usual cause; see [agent-guide/05-builder-internals.md](agent-guide/05-builder-internals.md)).
4. Review `git diff bundle/`; commit the submodule pin, any builder configuration change and the bundle
   together, so the history says which source revision produced which bundle.
5. When releasing, follow [agent-guide/06-rules-and-release-checklist.md](agent-guide/06-rules-and-release-checklist.md):
   package into `dist/`, review the output, then push `dist/zoho-analytics-okf/` to the public repository.

## For AI agents

Start at [agent-guide/README.md](agent-guide/README.md). The one rule: never edit `bundle/` or `dist/`
by hand - change the source in the analytics-api-docs repository and move the pin, or change
`handwritten/` or the configuration tables in `tools/build_okf.py`, then rebuild and validate.
