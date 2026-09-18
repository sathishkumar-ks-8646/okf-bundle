# 01 - Repository layout

Tooling, hand-written sources, the generated bundle and the packaged distribution sit side by side. The
API source documents are the one thing not stored here: they arrive through a git submodule. Folder names say what a folder is for; every folder that a maintainer touches has a
`README.md`.

```
<repo-root>/
├── README.md                         repository entry point: layout, pipeline, quick start
├── CLAUDE.md                         pointer for AI coding agents -> agent-guide/README.md
├── .gitignore                        ignores dist/ and tarballs
├── .gitmodules                       declares the analytics-api-docs submodule (url, branch = main)
├── agent-guide/                      this guide (internal, never published)
├── analytics-api-docs/               SOURCES - git submodule of the analytics-api-docs repository, pinned to one commit
│   ├── md/
│   │   ├── 01 · Organization Management/ORG_INFO_AND_SETTINGS.md
│   │   ├── 02 · User & Groups/{ORG_USERS,CUSTOM_ROLES,WORKSPACE_USERS,WORKSPACE_GROUPS}.md
│   │   ├── 03 · Workspace Management/{WORKSPACE_OPERATIONS,WORKSPACE_FOLDERS,WORKSPACE_PREFERENCES,DOMAIN_AND_WHITE_LABEL}.md
│   │   ├── 04 · Data Modeling & Schema/{TABLE_AND_SCHEMA,COLUMNS,LOOKUPS_AND_RELATIONSHIPS,QUERY_TABLES,FORMULA_COLUMNS,AGGREGATE_FORMULAS,WORKSPACE_VARIABLES}.md
│   │   ├── 05 · Data Operations/{SYNC_DATA_IMPORT,ASYNC_DATA_IMPORT,SYNC_DATA_EXPORT,ASYNC_DATA_EXPORT,ROW_OPERATIONS,DATA_SYNC_AND_CONNECTIVITY}.md
│   │   ├── 06 · Views Management/{VIEW_OPERATIONS,VIEW_PREFERENCES,TRASH_MANAGEMENT,AUTO_ANALYSIS,TAGS}.md
│   │   ├── 07 · Reports & Dashboards/{REPORTS,DASHBOARDS}.md
│   │   ├── 08 · Share & Publish/{SHARING,PUBLISH,EMBED_URL,SLIDESHOW_MANAGEMENT}.md
│   │   ├── 09 · Schedules & Alerts/EMAIL_SCHEDULES.md
│   │   └── 10 · DSML/AUTOML_ANALYSIS.md
│   ├── zenesis-oas/<domain>-grouped-api.json          OpenAPI 3, one file per domain (10 files)
│   ├── zenesis-oas-samples/<domain>-grouped-api-samples.json   SDK snippets keyed by path + method
│   ├── zoho-analytics-api-common.json                 OAuth scopes, Error schema, common responses
│   └── tools/validate_api_docs.py                     that repository's own naming and completeness check
├── handwritten/                      SOURCES - hand-authored concepts copied into the bundle on every build (README inside)
│   ├── overview.md                       -> bundle /overview.md
│   ├── how-to-use-this-bundle.md         -> bundle /how-to-use-this-bundle.md
│   ├── foundations/*.md                  -> bundle /foundations/<same name>.md
│   └── workflows/*.md                    -> bundle /workflows/<same name>.md
├── tools/                            (README inside)
│   ├── build_okf.py                  generator: analytics-api-docs + handwritten -> bundle
│   ├── validate_okf.py               OKF conformance + link + provenance checks
│   └── package_okf.py                bundle -> dist/ public repo layout (+ tarball)
├── bundle/                           THE BUNDLE - generated, deleted and rebuilt on every build; committed
└── dist/                             git-ignored: packaged public repo (git-initialised) and release tarballs
    ├── zoho-analytics-okf/           README.md, llms.txt, LICENSE.md, CHANGELOG.md, okf/, tools/validate.py, .github/
    └── zoho-analytics-okf-<version>.tar.gz
```

The bundle directory is named `bundle/` in this repository; the bundle's own name, as declared in its
`manifest.json`, is `zoho-analytics-rest-api-v2`. The packager copies `bundle/` to `okf/` in `dist/`.

## Who writes what

| Folder | Written by | Edited by agents? |
|---|---|---|
| `analytics-api-docs/md` | API documentation authors, in the analytics-api-docs repository | **Yes, upstream** - this is where endpoint facts change. Here, only the pin moves. |
| `analytics-api-docs/zenesis-oas` | Exported from the Zenesis documentation system, in the analytics-api-docs repository | Yes, upstream, when adding operations, schemas, samples or error codes. Keep valid JSON. |
| `analytics-api-docs/zenesis-oas-samples` | Same system, same repository | Yes, upstream, when adding SDK snippets for a new operation. |
| `analytics-api-docs/zoho-analytics-api-common.json` | Same system, same repository | Rarely: only for a new OAuth scope or a new common error example. |
| `handwritten/` | Bundle maintainers | **Yes**, for cross-cutting rules and playbooks. |
| `tools/build_okf.py` | Bundle maintainers | Yes, but only its configuration tables in normal operation. |
| `bundle/` | `build_okf.py` | **Never.** |
| `dist/` | `package_okf.py` | Never by hand, except `git` operations inside `dist/zoho-analytics-okf/`. Git-ignored in this repository. |

## Two pairs that must stay in step

1. **A markdown endpoint section and its OpenAPI operation.** The generator joins them by title:
   the markdown `## N. Title` must equal the operation's `x-zenesis-title` (or `summary`), or be
   listed in `TITLE_MAP` in the builder. The markdown supplies the narrative, CONFIG tables, samples,
   notes and error tables; the OpenAPI supplies the operation ID, path, scopes, parameters, content
   types, success status, schemas, throttles and its own error list.
2. **A group and its domain.** Every markdown file belongs to exactly one domain folder and one
   OpenAPI file. The mapping is the `DOMAINS` table in the builder; group and domain slugs become
   directory names in the bundle.

## Things that are deliberately *not* sources

- `bundle/` (generated).
- `dist/` (packaged copy of the generated bundle).
- Anything outside this repository (older `PRD/` folders, zip archives). They are unrelated to this pipeline.
