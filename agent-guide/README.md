# Agent guide for maintaining the Zoho Analytics OKF bundle

This folder is **internal**. It is never packaged or published. Its only purpose is to let an AI agent
(or a human) update the Open Knowledge Format bundle correctly when the Zoho Analytics REST API v2
changes: a new endpoint, a new CONFIG attribute, a changed behaviour, a new error code, a new API group.

All paths in this guide are relative to the repository root (the folder that holds `agent-guide/`,
`tools/` and `bundle/`). The repository may be cloned anywhere; nothing here depends on its absolute location.

`analytics-api-docs/` is a **git submodule** of the
[analytics-api-docs](https://github.com/sathish-dev-git/analytics-api-docs) repository, pinned to one
commit. Where a playbook says to edit a file under `analytics-api-docs/`, that edit is made in that
repository - either directly there, or inside the submodule on a branch that is pushed there - and this
repository then moves its pin: `git submodule update --remote --merge analytics-api-docs`. Its own
validator (`python3 tools/validate_api_docs.py` inside the submodule) must pass before the pin moves.

## The one rule

**Never edit anything under `bundle/` by hand.** That directory is deleted and
regenerated on every build. Change the *inputs*, run the build, validate, and the bundle follows.

```
inputs                                     generator                     outputs
analytics-api-docs/md/**/*.md                    ─┐
analytics-api-docs/zenesis-oas/*.json             ├──►  tools/build_okf.py  ──►  bundle/   (the OKF bundle)
analytics-api-docs/zenesis-oas-samples/*.json     │                                 │
analytics-api-docs/zoho-analytics-api-common.json │                                 ▼
handwritten/**/*.md                    ─┘     tools/validate_okf.py  (must print errors=0 broken_links=0)
                                                                          │
                                              tools/package_okf.py  ──►  dist/zoho-analytics-okf/   (public repo, git-ignored here)
```

## Where to start, by task

| I need to... | Read | Then edit |
|---|---|---|
| Understand the folder layout and pipeline | [01-repository-layout.md](01-repository-layout.md) | - |
| Understand what each bundle file contains and where it comes from | [02-bundle-structure.md](02-bundle-structure.md) | - |
| Write or edit a source markdown section so the parser picks it up | [03-source-document-format.md](03-source-document-format.md) | `analytics-api-docs/md/...` |
| Add a new endpoint | [04-change-playbooks.md](04-change-playbooks.md#a-add-a-new-endpoint) | `analytics-api-docs/md`, `analytics-api-docs/zenesis-oas`, samples, maybe `tools/build_okf.py` config |
| Add or change a CONFIG attribute or response field | [04-change-playbooks.md](04-change-playbooks.md#b-add-or-change-a-config-attribute-or-response-field) | `analytics-api-docs/md`, `analytics-api-docs/zenesis-oas` |
| Add or change an error code | [04-change-playbooks.md](04-change-playbooks.md#c-add-or-change-an-error-code) | `analytics-api-docs/md`, maybe `CANONICAL` in the builder |
| Add a new API group or domain | [04-change-playbooks.md](04-change-playbooks.md#d-add-a-new-api-group-or-domain) | `tools/build_okf.py` `DOMAINS`, new MD file, new or existing OAS file |
| Change a shared rule (auth, headers, criteria, roles...) | [04-change-playbooks.md](04-change-playbooks.md#f-change-a-foundation-document) | `handwritten/foundations/` |
| Add a workflow playbook | [04-change-playbooks.md](04-change-playbooks.md#g-add-a-workflow-playbook) | `handwritten/workflows/` |
| Deprecate or remove an endpoint | [04-change-playbooks.md](04-change-playbooks.md#e-deprecate-or-remove-an-endpoint) | `analytics-api-docs`, OAS `deprecated: true` |
| Know which builder table to touch | [05-builder-internals.md](05-builder-internals.md) | `tools/build_okf.py` |
| Release: version, changelog, publish | [06-rules-and-release-checklist.md](06-rules-and-release-checklist.md) | `tools/package_okf.py --version`, `dist/` |

## The standard loop

```bash
cd <repo-root>
git submodule update --init           # once per clone: fetch analytics-api-docs at the pinned commit
python3 tools/build_okf.py            # regenerates bundle/ ; prints endpoints=… errors=… sdk=…
python3 tools/validate_okf.py         # must end with errors=0 warnings=0 broken_links=0
git -C dist/zoho-analytics-okf status # (optional) see what the public copy would change
python3 tools/package_okf.py --tarball --version X.Y.Z   # only when releasing
```

Both scripts need only Python 3.8+ and the standard library. The build takes a few seconds.

If `build_okf.py` prints `WARN no OAS operation for markdown endpoint: <title>` or
`WARN OAS operation without markdown section: <title>`, the markdown and OpenAPI titles disagree;
fix the title or add a `TITLE_MAP` entry (see [05-builder-internals.md](05-builder-internals.md)).
If it prints `unresolved links:`, a markdown link points at a heading or file the resolver cannot find.

## Files in this folder

| File | Purpose |
|---|---|
| `README.md` | This page. Entry point and task router. |
| `01-repository-layout.md` | Every folder in the repository, what it holds, who writes it. |
| `02-bundle-structure.md` | Every directory and concept type in the bundle, the frontmatter contracts, and the source of each body section. |
| `03-source-document-format.md` | The exact markdown, OpenAPI and sample-file conventions the generator parses. |
| `04-change-playbooks.md` | Step-by-step procedures for each kind of API change. |
| `05-builder-internals.md` | The configuration tables and functions inside `tools/build_okf.py`, and the validator and packager. |
| `06-rules-and-release-checklist.md` | Invariants that must hold, things that must never appear, versioning, and the release checklist. |
