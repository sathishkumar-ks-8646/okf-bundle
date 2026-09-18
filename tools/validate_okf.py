#!/usr/bin/env python3
"""
OKF v0.2 conformance and hygiene checks for a bundle directory.

Checks that every non-reserved markdown file has parseable frontmatter with a non-empty `type`,
that reserved files (index.md, log.md) follow their structure, that no `resource` points outside
the bundle, and that every internal link and anchor resolves.

Usage:
    python3 validate.py [bundle-directory]

With no argument it looks for the bundle next to this script: ./okf, ./bundle, ./zoho-analytics-rest-api-v2,
or the current directory if that is itself a bundle root.

Audience: maintainers and contributors. Consumers of the bundle do not need to run this; it exists
so that continuous integration can refuse to publish a bundle that is malformed or has broken links.
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUNDLE_DIRS = ('okf', 'bundle', 'zoho-analytics-rest-api-v2', '.')


def is_bundle(d):
    """A bundle root is a directory whose index.md declares okf_version."""
    idx = os.path.join(d, 'index.md')
    return os.path.isfile(idx) and 'okf_version' in open(idx, encoding='utf-8').read(400)


def find_bundle():
    if len(sys.argv) > 1:
        d = os.path.abspath(sys.argv[1])
        if not os.path.isdir(d):
            sys.exit(f'not a directory: {sys.argv[1]}')
        if not is_bundle(d):
            sys.exit(f'not an OKF bundle root (no index.md declaring okf_version): {sys.argv[1]}')
        return d
    for base in (os.getcwd(), ROOT):
        for name in BUNDLE_DIRS:
            d = os.path.abspath(os.path.join(base, name))
            if os.path.isdir(d) and is_bundle(d):
                return d
    sys.exit('no OKF bundle found. Pass the bundle directory as an argument, '
             'for example: python3 ' + os.path.basename(__file__) + ' okf')


OUT = find_bundle()
RESERVED = ('index.md', 'log.md')

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m: return None, text
    return m.group(1), text[m.end():]

def headings(text):
    out, fence = [], False
    for line in text.split('\n'):
        if line.startswith('```'): fence = not fence
        if not fence:
            mm = re.match(r'^#{1,6} (.+)$', line)
            if mm: out.append(mm.group(1))
    return out

def slugify(s):
    s = re.sub(r'`', '', s).strip().lower()
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    return s.replace(' ', '-')

errors, warnings = [], []
docs = {}
for dirpath, dirnames, filenames in os.walk(OUT):
    rel_dir = os.path.relpath(dirpath, OUT)
    if 'index.md' not in filenames:
        warnings.append(f'missing index.md in {rel_dir}')
    for f in filenames:
        p = os.path.join(dirpath, f)
        relp = '/' + os.path.relpath(p, OUT).replace(os.sep, '/')
        if not f.endswith('.md'):
            docs[relp] = None; continue
        text = open(p, encoding='utf-8').read()
        fm, body = parse_frontmatter(text)
        docs[relp] = (fm, body, text)
        if f in RESERVED:
            if f == 'index.md' and fm is not None and rel_dir != '.':
                errors.append(f'{relp}: index.md must not carry frontmatter except at bundle root')
            if fm is None and not re.search(r'(?m)^# ', body):
                warnings.append(f'{relp}: reserved file has no section heading')
            continue
        if fm is None:
            errors.append(f'{relp}: missing YAML frontmatter'); continue
        if not re.search(r'(?m)^type: \S', fm):
            errors.append(f'{relp}: frontmatter has no non-empty type')
        for key in ('title', 'description'):
            if not re.search(rf'(?m)^{key}: \S', fm):
                warnings.append(f'{relp}: frontmatter missing {key}')
        if '{{' in fm: errors.append(f'{relp}: unexpanded template placeholder in frontmatter')
        if re.search(r'(?m)^generated:', fm) and re.search(r'(?m)^  by: ', fm):
            errors.append(f'{relp}: generated.by must not be present')
        for res in re.findall(r'(?m)^\s+resource: "?([^"\n]+?)"?\s*$', fm) + re.findall(r'(?m)^resource: "?([^"\n]+?)"?\s*$', fm):
            if res.startswith(('http://', 'https://')): continue
            if res.startswith('/') and os.path.exists(os.path.join(OUT, res.lstrip('/'))): continue
            errors.append(f'{relp}: resource outside the bundle or missing: {res}')

# link check
anchors = {}
for relp, v in docs.items():
    if v: anchors[relp] = {slugify(h) for h in headings(v[1])}
broken = []
for relp, v in docs.items():
    if not v: continue
    fence = False
    for line in v[2].split('\n'):
        if line.startswith('```'): fence = not fence
        if fence: continue
        for label, target in re.findall(r'\[([^\]]*)\]\(([^)\s]+)\)', line):
            if target.startswith(('http://', 'https://', 'mailto:')): continue
            path, _, anchor = target.partition('#')
            if path == '':
                if anchor and anchor not in anchors.get(relp, set()) and not re.match(r'^error-\d+$', anchor):
                    broken.append((relp, target, 'anchor'))
                continue
            if path.startswith('/'):
                tgt = path
            else:
                tgt = os.path.normpath(os.path.join(os.path.dirname(relp), path)).replace(os.sep, '/')
                if not tgt.startswith('/'): tgt = '/' + tgt
            if tgt.endswith('/'): tgt += 'index.md'
            if tgt not in docs:
                if os.path.isdir(os.path.join(OUT, tgt.lstrip('/'))): continue
                broken.append((relp, target, 'file'))
            elif anchor and docs[tgt] and anchor not in anchors.get(tgt, set()):
                broken.append((relp, target, 'anchor'))

concepts = sum(1 for p, v in docs.items() if v and os.path.basename(p) not in RESERVED)
print(f'bundle={os.path.relpath(OUT, os.getcwd())} files={len(docs)} concepts={concepts} errors={len(errors)} warnings={len(warnings)} broken_links={len(broken)}')
for e in errors: print('ERROR', e)
for w in warnings[:40]: print('WARN ', w)
import collections
bt = collections.Counter((b[2]) for b in broken); print('broken by kind:', dict(bt))
for b in broken[:60]: print('LINK ', b)
sys.exit(1 if errors else 0)
