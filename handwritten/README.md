# handwritten - hand-authored bundle concepts (input)

Concept files that no API document supplies: cross-cutting rules and end-to-end playbooks. Every file
here (except this README) is copied verbatim into the bundle on each build, with `{{NOW}}` and
`{{BUILDER}}` placeholders substituted.

| Here | In the bundle |
|---|---|
| `overview.md` | `/overview.md` |
| `how-to-use-this-bundle.md` | `/how-to-use-this-bundle.md` |
| `foundations/<name>.md` | `/foundations/<name>.md` (authentication, request conventions, response envelope, filter criteria, roles, data centers, enums, glossary...) |
| `workflows/<name>.md` | `/workflows/<name>.md` (multi-endpoint playbooks) |

Each file is a full OKF concept: YAML frontmatter starting with `type`, then `title`, `description`,
`tags`, `sources`, and a markdown body whose links are bundle-root-relative (`/foundations/...`).
Copy an existing file of the same kind as the template. Some foundations (`error-codes.md`, `scopes.md`,
`rate-limits.md`, `identifiers.md`, `permissions.md`) are **generated** by the builder, not kept here.

Procedures: [../agent-guide/04-change-playbooks.md](../agent-guide/04-change-playbooks.md) sections
F (change a foundation document) and G (add a workflow playbook). Frontmatter contract:
[../agent-guide/02-bundle-structure.md](../agent-guide/02-bundle-structure.md).
