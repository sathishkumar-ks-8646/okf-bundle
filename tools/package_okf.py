#!/usr/bin/env python3
"""
package_okf.py - Assemble the public distribution of the Zoho Analytics OKF bundle.

Produces a self-contained, git-ready directory:

    dist/zoho-analytics-okf/
      README.md            human landing page (rendered by GitHub)
      llms.txt             AI/agent entry point (llmstxt.org convention)
      LICENSE.md           licence terms
      CHANGELOG.md         version history
      okf/                 THE BUNDLE (OKF v0.2) - the only thing consumers need
      tools/validate.py    conformance + link validator, used by CI
      .github/workflows/   CI that validates the bundle on every push and PR

Usage:
    python3 tools/package_okf.py
    python3 tools/package_okf.py --version 1.1.0 --repo-url https://github.com/<org>/zoho-analytics-okf
    python3 tools/package_okf.py --tarball

Nothing here touches git remotes or pushes. Review the output, then push it yourself.
"""
import argparse, json, os, shutil, subprocess, sys, tarfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUNDLE = os.path.join(ROOT, 'bundle')
DIST = os.path.join(ROOT, 'dist')
REPO_NAME = 'zoho-analytics-okf'

DEFAULT_REPO = 'https://github.com/zoho/zoho-analytics-okf'
DEFAULT_SITE = 'https://www.zoho.com/analytics/api/v2/okf'
DEFAULT_DOCS = 'https://www.zoho.com/analytics/api/v2/'
# Where the bundle is actually served from today. README's `git clone` line and the "Canonical copies"
# footer keep pointing at DEFAULT_REPO / DEFAULT_SITE (the intended permanent homes); every raw-file link
# in README and llms.txt uses this base so that agents fetch a URL that resolves now.
# Set to None once the repository moves to DEFAULT_REPO, and the raw base is derived from --repo-url.
DEFAULT_BASE_URL = 'https://raw.githubusercontent.com/sathish-dev-git/zoho-analytics-okf/main'


def raw_base(repo_url, ref='main'):
    """Raw-file base URL for a GitHub repo, which is what agents fetch."""
    if 'github.com/' in repo_url:
        owner_repo = repo_url.split('github.com/', 1)[1].strip('/')
        return 'https://raw.githubusercontent.com/' + owner_repo + '/' + ref
    return repo_url.rstrip('/')


def readme(m, repo_url, site_url, docs_url, raw):
    c = m['counts']
    return f"""# Zoho Analytics REST API v2 - Open Knowledge Format bundle

Machine-readable, agent-friendly knowledge base for the [Zoho Analytics REST API v2]({docs_url}).
It packages every public endpoint, the conventions they share, and their error codes, OAuth scopes
and permissions as an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)
(OKF v{m['okf_version']}) bundle: a directory of markdown files with YAML frontmatter.

**Bundle version {m['version']}** - {c['endpoints']} endpoints, {c['domains']} domains, {c['groups']} groups,
{c['error_codes']} error codes, {c['oauth_scopes']} OAuth scopes, {c['workflow_playbooks']} workflow playbooks,
{c['sdk_example_documents']} SDK example documents in 9 languages.

This is documentation, not a client library. For the SDKs themselves see the
[Zoho Analytics API documentation]({docs_url}).

## Quick start

**For an AI assistant or agent.** Point it at [`llms.txt`]({raw}/llms.txt) and let it follow the links.
Inside the bundle, links that begin with `/` are relative to the bundle root, which is `okf/`.

```
{raw}/llms.txt                                  curated entry point
{raw}/okf/manifest.json                         version, counts, entry points
{raw}/okf/overview.md                           what the API is, five shared conventions
{raw}/okf/how-to-use-this-bundle.md             frontmatter contract and navigation rules
{raw}/okf/references/endpoint-catalog.json      every endpoint, machine-readable
```

**For a human.** Start at [`okf/overview.md`](okf/overview.md), then
[`okf/endpoint-catalog.md`](okf/endpoint-catalog.md) to find an endpoint, then the endpoint document.

**For tooling** such as SDK generators, Postman collections and MCP servers. Read
[`okf/references/endpoint-catalog.json`](okf/references/endpoint-catalog.json) for the inventory and
[`okf/references/openapi/`](okf/references/openapi/) for request and response schemas.

```bash
git clone {repo_url}.git
```

## What is in the bundle

| Path | Contents |
|---|---|
| `okf/index.md` | Bundle root. Declares `okf_version`. Lists everything below. |
| `okf/overview.md` | What the API is, the object model, the five conventions every call shares. |
| `okf/how-to-use-this-bundle.md` | Directory layout, the `api:` frontmatter contract, navigation rules for agents. |
| `okf/endpoint-catalog.md` | All {c['endpoints']} endpoints in one table. |
| `okf/foundations/` | Rules shared by every call: authentication, data centers, request conventions and CONFIG encoding, response envelope, HTTP statuses, error catalog, OAuth scopes, roles and permissions, permission matrix, identifiers, filter criteria syntax, asynchronous jobs, rate limits, export and import enumerations, White Label, glossary, SDK clients. |
| `okf/domains/` | One document per domain, per API group and per endpoint. |
| `okf/workflows/` | Step-by-step playbooks for multi-endpoint tasks. |
| `okf/sdk-examples/` | Code samples per endpoint in cURL, C#, Go, Java, PHP, Python, Node.js, Ruby and Deluge. |
| `okf/references/` | The OpenAPI 3 specifications and the machine-readable endpoint catalog. |
| `okf/manifest.json` | Bundle name, version, OKF version, counts and entry points. |

## How the documents are structured

Every endpoint document carries an `api:` block in its frontmatter so tools never have to parse prose:

```yaml
type: API Endpoint
title: Share Views
api:
  operation_id: shareViews
  method: POST
  path: /restapi/v2/workspaces/{{workspace-id}}/share
  oauth_scopes: [ZohoAnalytics.share.create]
  org_id_header: required
  config_parameter: {{ location: form, required: true }}
  success_status: 204
  error_codes: [7301, 7307, 7320]
  openapi: {{ file: /references/openapi/share-publish-grouped-api.json, pointer: "#/paths/..." }}
```

The body always uses the same H1 sections in the same order: Summary, Endpoint, Request, Response,
Examples, Notes and Behaviour, Error Codes, Related. Full contract in
[`okf/how-to-use-this-bundle.md`](okf/how-to-use-this-bundle.md).

## Versioning

Bundle versions follow semantic versioning, independent of the API version, which is always v2.

| Change | Bump |
|---|---|
| An endpoint is removed or renamed, or the bundle layout changes | major |
| Endpoints, scopes or documents are added | minor |
| Content corrections and clarifications | patch |

Pin a version by cloning a tag or downloading the release tarball. `main` always holds the newest bundle.

## Provenance and trust

Concepts are derived from the Zoho Analytics API reference documents and the OpenAPI specifications
shipped in `okf/references/openapi/`. Each concept records `generated.at` and, where applicable,
`sources`. No concept carries a `verified` entry yet, so the bundle's OKF trust tier is **unverified**:
content is faithful to the source documents but has not been re-confirmed against the live service.
Reviewers should add `verified` entries to the concepts they check.

## Feedback and contributions

Open an issue for anything wrong, missing or ambiguous. Include the bundle version from
`okf/manifest.json` and the path of the document.

If you send a pull request, run the validator first. It is the same check that CI runs, and it is the
only thing in this repository aimed at maintainers rather than consumers. You do not need it to *use*
the bundle.

```bash
python3 tools/validate.py        # finds okf/ automatically; needs Python 3.8+, no dependencies
```

It verifies OKF v0.2 conformance, that no `resource` points outside the bundle, and that every internal
link and anchor resolves. It exits non-zero on any error.

## Licence

See [LICENSE.md](LICENSE.md).

---

Canonical copies: [{repo_url}]({repo_url}) and [{site_url}]({site_url}).
"""


def llms_txt(m, base):
    c = m['counts']
    return f"""# Zoho Analytics REST API v2

> Open Knowledge Format (OKF v{m['okf_version']}) bundle for the Zoho Analytics REST API v2: {c['endpoints']} endpoints across {c['domains']} domains, with the conventions, OAuth scopes, roles, identifiers and {c['error_codes']} error codes they share. Base URL https://analyticsapi.zoho.com, path prefix /restapi/v2, OAuth 2.0 with the Zoho-oauthtoken scheme, structured input in a single JSON parameter named CONFIG.

Read overview.md first, then how-to-use-this-bundle.md for the frontmatter contract and navigation rules. Links inside the bundle that begin with a slash are relative to the bundle root, which is {base}/okf.

## Start here

- [Overview]({base}/okf/overview.md): what the API is, the object model, and the five conventions every call shares.
- [How to use this bundle]({base}/okf/how-to-use-this-bundle.md): directory layout, the api frontmatter contract, navigation rules for agents and generators.
- [Endpoint catalog]({base}/okf/endpoint-catalog.md): all {c['endpoints']} endpoints with method, path, operation ID, group, scope and success status.
- [Bundle index]({base}/okf/index.md): the full table of contents.

## Foundations (rules shared by every call)

- [Authentication]({base}/okf/foundations/authentication.md): OAuth 2.0 flow, Authorization header, token lifetime and refresh.
- [OAuth scopes]({base}/okf/foundations/oauth-scopes.md): all {c['oauth_scopes']} scopes and the operations each one covers.
- [Data centers]({base}/okf/foundations/data-centers.md): API host and accounts host per region.
- [Request conventions]({base}/okf/foundations/request-conventions.md): URL structure, headers, and how to encode the CONFIG parameter per HTTP method.
- [Response envelope]({base}/okf/foundations/response-envelope.md): the success and failure JSON shapes, the 204 no-body pattern, file responses.
- [Error code catalog]({base}/okf/foundations/error-codes.md): {c['error_codes']} codes with meaning, HTTP status, resolution and the operations that raise them.
- [Error codes quick reference]({base}/okf/foundations/error-codes-quick-reference.md): one compact row per code.
- [Roles and permissions]({base}/okf/foundations/roles-and-permissions.md): organization roles, workspace roles, view-level share permissions.
- [Permission matrix]({base}/okf/foundations/permission-matrix.md): scope, organization header and required role for every endpoint.
- [Identifiers]({base}/okf/foundations/identifiers.md): every ID used in paths and headers, and the call that returns it.
- [Filter criteria syntax]({base}/okf/foundations/filter-criteria-syntax.md): the SQL-like row filter used by exports, row writes, shares and embeds.
- [Asynchronous jobs]({base}/okf/foundations/asynchronous-jobs.md): job codes, polling, callbacks, batch imports, retention.
- [Rate limits and quotas]({base}/okf/foundations/rate-limits-and-quotas.md): throttles, concurrency guards, plan quotas, API units.
- [HTTP status codes]({base}/okf/foundations/http-status-codes.md): which status each failure class returns.
- [Glossary]({base}/okf/foundations/glossary.md): every Zoho Analytics object and term.

## API domains

- [Organization Management]({base}/okf/domains/organization-management/overview.md): organizations, plan and resource usage, name to ID resolution.
- [Users and Groups]({base}/okf/domains/users-and-groups/overview.md): organization users, workspace users, workspace groups.
- [Workspace Management]({base}/okf/domains/workspace-management/overview.md): workspaces, folders, preferences, White Label domain access.
- [Data Modeling and Schema]({base}/okf/domains/data-modeling-and-schema/overview.md): tables, columns, lookups, query tables, formulas, variables.
- [Data Operations]({base}/okf/domains/data-operations/overview.md): import, export, row writes, datasource sync.
- [Views Management]({base}/okf/domains/views-management/overview.md): view lifecycle, favourites, trash, auto analysis.
- [Reports and Dashboards]({base}/okf/domains/reports-and-dashboards/overview.md): analysis views and dashboards.
- [Share and Publish]({base}/okf/domains/share-and-publish/overview.md): sharing, public and private URLs, embed URLs, slideshows.
- [Schedules and Alerts]({base}/okf/domains/schedules-and-alerts/overview.md): recurring email delivery of views.
- [Data Science and Machine Learning]({base}/okf/domains/dsml/overview.md): AutoML training, deployment and scoring.

## Workflows

- [Workflow playbooks]({base}/okf/workflows/index.md): {c['workflow_playbooks']} step-by-step procedures spanning several endpoints, including bootstrapping identifiers, asynchronous export, large imports, sharing with row filters, multi-tenant embedding, email schedules, user provisioning and AutoML.

## Machine-readable

- [manifest.json]({base}/okf/manifest.json): bundle version, OKF version, counts, entry points.
- [endpoint-catalog.json]({base}/okf/references/endpoint-catalog.json): every endpoint with method, path, scopes, permission, error codes and document paths.
- [OpenAPI specifications]({base}/okf/references/openapi/): OpenAPI 3 files, one per domain plus shared components.

## Optional

- [SDK examples]({base}/okf/sdk-examples/index.md): per-endpoint code samples in cURL, C#, Go, Java, PHP, Python, Node.js, Ruby and Deluge.
- [SDK clients]({base}/okf/foundations/sdk-clients.md): how each official client library is constructed.
"""


def license_md():
    return """# Licence

**Status: to be confirmed before this repository is made public.**

This bundle is API reference documentation derived from the Zoho Analytics API reference documents and
OpenAPI specifications. It contains no product source code.

Recommended terms, subject to confirmation by the documentation and legal owners:

- **Documentation** (every `.md` file and the JSON files under `okf/`):
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
  This lets developers, SDK authors and AI tools copy, adapt and redistribute the content with attribution,
  which is the point of publishing it.
- **Code samples** under `okf/sdk-examples/`: a permissive code licence such as
  [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) or MIT, so they can be pasted into
  products without attribution friction.
- **Trademarks**: Zoho, Zoho Analytics and related marks are not licensed by the above and remain the
  property of Zoho Corporation.

Replace this file with the approved licence text before the repository is published.

Copyright (c) Zoho Corporation Pvt. Ltd. All rights reserved.
"""


def changelog(m):
    c = m['counts']
    return f"""# Changelog

All notable changes to this bundle are recorded here. Versions follow semantic versioning: major for a
removed or renamed endpoint or a layout change, minor for additions, patch for corrections.

## {m['version']} - {m['generated']['at'][:10]}

### Added

- First public release of the Zoho Analytics REST API v2 Open Knowledge Format bundle (OKF v{m['okf_version']}).
- {c['endpoints']} endpoint concepts across {c['domains']} domains and {c['groups']} API groups.
- Foundations covering authentication, data centers, request conventions, response envelope, HTTP statuses,
  OAuth scopes, roles and permissions, the permission matrix, identifiers, filter criteria syntax,
  asynchronous jobs, rate limits and quotas, export and import enumerations, White Label behaviour,
  the glossary and SDK clients.
- Error catalog with {c['error_codes']} codes plus a compact quick reference.
- {c['workflow_playbooks']} workflow playbooks for multi-endpoint tasks.
- {c['sdk_example_documents']} SDK example documents covering 9 languages.
- Machine-readable `manifest.json` and `references/endpoint-catalog.json`, and the OpenAPI 3 specifications.

### Known limitations

- Trust tier is `unverified`: no concept carries a `verified` entry yet.
- Two endpoints, Fetch All Embed URLs and Delete Embed URL, are documented from the API reference only.
  They are absent from the OpenAPI specifications and their documents say so.
"""


WORKFLOW = """name: Validate OKF bundle

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Validate OKF conformance and links
        run: python3 tools/validate.py okf
      - name: Check machine-readable files parse
        run: |
          python3 -c "import json;json.load(open('okf/manifest.json'))"
          python3 -c "import json;json.load(open('okf/references/endpoint-catalog.json'))"
          for f in okf/references/openapi/*.json; do
            python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$f"
          done
"""

GITIGNORE = """.DS_Store
__pycache__/
*.pyc
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--version', help='override the bundle version from manifest.json')
    ap.add_argument('--repo-url', default=DEFAULT_REPO, help='public repository URL')
    ap.add_argument('--site-url', default=DEFAULT_SITE, help='documentation-site mirror URL')
    ap.add_argument('--docs-url', default=DEFAULT_DOCS, help='Zoho Analytics API documentation URL')
    ap.add_argument('--base-url', default=DEFAULT_BASE_URL, help='base URL for raw-file links in README and llms.txt (default: DEFAULT_BASE_URL, else the raw file URL of --repo-url)')
    ap.add_argument('--ref', default='main', help='git ref used to build raw file URLs')
    ap.add_argument('--out', default=DIST, help='output directory (default <repo>/dist)')
    ap.add_argument('--tarball', action='store_true', help='also write a .tar.gz next to the directory')
    a = ap.parse_args()

    if not os.path.isdir(BUNDLE):
        sys.exit('bundle not found: ' + BUNDLE + '\nRun tools/build_okf.py first.')
    with open(os.path.join(BUNDLE, 'manifest.json'), encoding='utf-8') as f:
        m = json.load(f)
    if a.version:
        m['version'] = a.version
    raw = a.base_url or raw_base(a.repo_url, a.ref)

    out = os.path.join(a.out, REPO_NAME)
    git_dir = os.path.join(out, '.git')
    saved_git = None
    if os.path.isdir(out):
        if os.path.isdir(git_dir):                       # preserve history across re-packaging
            saved_git = os.path.join(a.out, '.git-saved')
            shutil.rmtree(saved_git, ignore_errors=True)
            shutil.move(git_dir, saved_git)
        shutil.rmtree(out)
    os.makedirs(out)
    if saved_git:
        shutil.move(saved_git, git_dir)

    shutil.copytree(BUNDLE, os.path.join(out, 'okf'))
    if a.version:                                        # keep the shipped manifest in step
        with open(os.path.join(out, 'okf', 'manifest.json'), 'w', encoding='utf-8') as f:
            json.dump(m, f, indent=2, ensure_ascii=False)
            f.write('\n')

    files = {
        'README.md': readme(m, a.repo_url, a.site_url, a.docs_url, raw),
        'llms.txt': llms_txt(m, raw),
        'LICENSE.md': license_md(),
        'CHANGELOG.md': changelog(m),
        '.gitignore': GITIGNORE,
        os.path.join('.github', 'workflows', 'validate-okf.yml'): WORKFLOW,
    }
    for rel, text in files.items():
        path = os.path.join(out, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text if text.endswith('\n') else text + '\n')

    os.makedirs(os.path.join(out, 'tools'), exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'tools', 'validate_okf.py'), os.path.join(out, 'tools', 'validate.py'))

    rc = subprocess.call([sys.executable, os.path.join(out, 'tools', 'validate.py'), os.path.join(out, 'okf')])
    if rc != 0:
        sys.exit('validation failed; distribution not packaged')

    n = sum(len(fs) for d, _, fs in os.walk(out) if os.sep + '.git' + os.sep not in d + os.sep)
    print('packaged ' + out + '  (version ' + m['version'] + ', ' + str(n) + ' files)')

    if a.tarball:
        tar = os.path.join(a.out, REPO_NAME + '-' + m['version'] + '.tar.gz')
        with tarfile.open(tar, 'w:gz') as t:
            t.add(out, arcname=REPO_NAME + '-' + m['version'],
                  filter=lambda ti: None if '/.git/' in ti.name + '/' else ti)
        print('tarball  ' + tar + '  (%.1f MB)' % (os.path.getsize(tar) / 1048576))


if __name__ == '__main__':
    main()
