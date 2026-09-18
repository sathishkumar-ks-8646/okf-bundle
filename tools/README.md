# tools

Three standard-library Python scripts (3.8+). Run them from the repository root; each locates the
repository by its own path, so the working directory does not matter.

| Script | Reads | Writes | Purpose |
|---|---|---|---|
| `build_okf.py` | `analytics-api-docs/`, `handwritten/` | `bundle/` (deleted and recreated) | Generates the OKF bundle. Prints `endpoints=… groups=… errors=… sdk=…` on success and `WARN` lines when markdown and OpenAPI disagree. |
| `validate_okf.py [dir]` | `bundle/` (or the directory given) | nothing | OKF v0.2 conformance, frontmatter, reserved files, `resource` provenance, links and anchors. Must end with `errors=0 warnings=0 broken_links=0`. Copied into the public repo as `tools/validate.py` for CI. |
| `package_okf.py` | `bundle/`, `validate_okf.py` | `dist/zoho-analytics-okf/` (+ `.tar.gz` with `--tarball`) | Assembles the public repository layout: `README.md`, `llms.txt`, `LICENSE.md`, `CHANGELOG.md`, `okf/`, CI workflow. Preserves an existing `dist/zoho-analytics-okf/.git`. Never pushes. |

```bash
python3 tools/build_okf.py
python3 tools/validate_okf.py
python3 tools/package_okf.py --tarball --version X.Y.Z    # URLs come from the DEFAULT_* constants in the packager
```

What to edit inside `build_okf.py` (configuration tables such as `DOMAINS`, `TITLE_MAP`, `MD_ONLY_OPS`,
`CANONICAL`, `ID_SOURCES`), and every flag of the packager, is documented in
[../agent-guide/05-builder-internals.md](../agent-guide/05-builder-internals.md).
