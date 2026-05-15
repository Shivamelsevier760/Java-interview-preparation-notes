# Setup — Push to GitHub and Go Live

Roughly 5 minutes of work. You'll end up with:

- A private (or public) GitHub repo holding your entire interview vault
- An auto-updating Medium article feed (runs every morning at 06:00 UTC)
- An auto-rebuilt README + cheatsheet whenever you add notes
- Optional GitHub Pages site for browsing in a browser / on mobile

## 1. Create the GitHub repo

Go to <https://github.com/new>, name it something like `interview-vault` (private if you want), **do not** initialize with README/license/.gitignore (the vault already has its own).

## 2. Push from your machine

Unzip the vault to a folder, then:

```bash
cd interview-vault              # or whatever you named the unzipped folder
git init
git add .
git commit -m "feat: import organized Notion vault"
git branch -M main
git remote add origin https://github.com/<your-username>/interview-vault.git
git push -u origin main
```

## 3. Verify the daily Medium fetcher

Go to your repo → Actions tab → "Fetch Medium articles" → click "Run workflow" to trigger it once manually. Within ~30 seconds you should see a commit appear in `12-medium-feed/` with a stack of new article stubs.

If you want to add or remove tags/authors, edit `scripts/fetch_medium.py` — the two lists at the top (`TAG_FEEDS`, `AUTHOR_FEEDS`).

## 4. (Optional) Enable GitHub Pages

If you want a browsable website over your vault:

1. Repo → Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` / `/ (root)`
4. Save

It'll publish at `https://<your-username>.github.io/interview-vault`. GitHub renders markdown files automatically, and the README.md at the root becomes the landing page. Click into folders to drill down.

For a prettier site, drop a Jekyll theme — add a `_config.yml`:

```yaml
theme: jekyll-theme-cayman
title: Senior Java Interview Vault
```

…and push. The same Markdown becomes a themed site.

## 5. Open the vault locally

For day-to-day reading and editing pick one:

- **VS Code** — `code .` in the repo. Markdown preview is Ctrl/Cmd-Shift-V.
- **Obsidian** — File → Open vault → point at the repo folder. You get backlinks, graph view, search across everything.
- **GitHub mobile app** — read on your phone, leave notes via in-browser edit.

## 6. Day-to-day workflow

- Read a Medium stub in `12-medium-feed/` → fill in `read: true`, `rating: 4`, `notes: "..."`.
- Move articles you loved into the relevant topic folder (`01-java/`, `02-microservices/`, etc.) — the daily push auto-rebuilds the index.
- Edit notes directly in markdown. Push when ready.
- Night before an interview, open `cheatsheet.md` and grep.

## Re-running the reorganizer

If you do another Notion export in the future and want to merge it in:

```bash
python scripts/reorganize.py <path-to-new-export> /tmp/new-vault
# manual diff / copy in what's actually new
```

## Files in this repo

```
.
├── README.md             # generated index — links to every section
├── cheatsheet.md         # consolidated review file (inlines high-signal sections)
├── SETUP.md              # this file
├── scripts/
│   ├── reorganize.py     # the script that built this vault from your Notion export
│   ├── build_index.py    # generates README + cheatsheet
│   └── fetch_medium.py   # daily Medium RSS fetcher
├── .github/workflows/
│   ├── fetch-medium.yml
│   └── rebuild-index.yml
├── 01-java/              # Java interview content (your biggest section)
├── 02-microservices/
├── 03-medium-series/     # Your own curated Medium series (parts 1–7)
├── 04-networking/
├── 05-aws-cloud-practitioner/
├── 06-aws-developer-associate/
├── 07-devops/
├── 08-behavioral/
├── 09-references/
├── 10-work/              # Elsevier / CDM / Semarchy
├── 11-personal/          # Journal, tasks, etc.
├── 12-medium-feed/       # auto-populated by the workflow (created on first run)
└── 99-uncategorized/
```
