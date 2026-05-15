# Setup — Turn the repo into a study website

You're adding four files (and one folder) to your existing repo. After pushing, GitHub Actions builds the site and deploys it to GitHub Pages automatically.

## What's in this add-on

```
mkdocs.yml                                # MkDocs Material config
requirements.txt                          # Python deps
index.md                                  # homepage (replaces README.md as front page)
.pages                                    # nav order + section labels
.github/workflows/deploy-pages.yml        # build & deploy on every push
```

## Step-by-step

### 1. Drop the files into your repo

Unzip this archive into the same folder as your `Java-interview-preparation-notes` checkout. The four config files land at the repo root and the workflow lands in `.github/workflows/`.

### 2. Commit and push

```bash
cd Java-interview-preparation-notes
git add mkdocs.yml requirements.txt index.md .pages .github/workflows/deploy-pages.yml SETUP-WEBSITE.md
git commit -m "feat: add MkDocs Material study website"
git push
```

### 3. Enable GitHub Pages with the new source

1. Repo → **Settings** → **Pages**
2. Source: **GitHub Actions** (not "Deploy from a branch" anymore)
3. Save

That's it. If Pages was previously set to "Deploy from a branch", just switch it to "GitHub Actions".

### 4. Watch the first build

Go to your repo → **Actions** tab → "Deploy MkDocs site to GitHub Pages" → the most recent run. First build takes ~2 minutes (installs Python deps, renders 311 markdown files, uploads artifact). When it goes green, the site is live at:

**https://shivamelsevier760.github.io/Java-interview-preparation-notes/**

## How daily use works

- **Edit a note locally or on GitHub** → commit and push → site rebuilds in ~90 seconds.
- **Search** — press `/` anywhere on the site to focus the search bar. Full-text across every note.
- **Dark mode** — toggle in the top right; respects your OS preference by default.
- **Edit a page directly** — click the pencil icon in the top right of any page, edit in GitHub's web editor, save. Site rebuilds automatically.

## Customizing

**Change the site name / colors** — edit `mkdocs.yml`:
- `site_name:` line at top
- `palette` → `primary` / `accent` (try `deep purple`, `teal`, `amber`)

**Reorder or rename sections in the sidebar** — edit `.pages` at the repo root.

**Add a new top-level section** — create a folder at the repo root (e.g., `13-databases/`), add a couple of `.md` files in it, push. It auto-appears in the nav.

**Test locally before pushing** (optional but recommended for big edits):

```bash
pip install -r requirements.txt
mkdocs serve
# open http://127.0.0.1:8000
```

## Troubleshooting

- **Build fails with "permission denied for Pages"** → Settings → Actions → General → Workflow permissions → "Read and write permissions" → Save. Re-run the workflow.
- **Build is green but the site shows 404** → wait ~1 minute, GitHub Pages takes a moment to propagate the first deploy.
- **Sidebar shows ugly folder names** → edit `.pages` and add a per-folder `.pages` file inside the folder, e.g. inside `01-java/` create a `.pages` with `title: Java Core`.
- **Search isn't finding something** → it indexes during build, so it covers everything in your main branch after the latest deploy succeeds.
