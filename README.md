# TechHub workbench

One codespace for the TechHub Git and API challenges: Git, the GitHub CLI, Python with `requests`, and Claude Code,
all installed. Nothing to install on your computer.

## Set it up once

1. Click **Use this template › Create a new repository**. Name it `techhub-workbench`, owner: you. Private is fine.
2. On your copy, click **Code › Codespaces › Create codespace on main**. The first start takes a few minutes.
3. Stop the codespace when you finish for the day (github.com/codespaces › ••• › Stop) so it doesn't use your free
   hours. Your files stay; start it again from the same page.

## Git challenges (381, 382, 391–396, 406, 407)

In the codespace's terminal:

```
get 381
cd challenges/381/ridgeline-trial-balance
git log --oneline
```

`get` downloads the challenge's repository, with its whole history, into `challenges/381/`. Each challenge gets its own
folder; `challenges/` is never committed to your workbench. To start a challenge over: `get 381 --fresh`.

Challenges 403–405 work with a repository on GitHub instead: 403 clones it here (`cd challenges` first), and 404 and
405 have you fork it and open a codespace on your fork. Their pages explain.

## API challenges (383, 384, 397–402)

These are **Level 2, Processing on your computer**: a Python script you run here reads the TechHub API sandbox,
works out the answer, and writes a file. The sandbox keeps the data (Storage); your script keeps nothing.

1. Get a sandbox key: `curl -X POST -H "Content-Length: 0" https://techhub.byuaccounting.net/api/v1/keys`
2. `cp .env.example .env` and paste the key into `.env`. `.gitignore` keeps `.env` out of Git: a key never goes in a
   script or a commit.
3. Write your script in `scripts/` (Claude Code can help: type `claude`). Read the key with
   `from dotenv import load_dotenv; load_dotenv(); key = os.environ["TECHHUB_API_KEY"]`.
4. Run it with `python scripts/<name>.py`. To open a CSV it wrote in Excel, right-click it in the Explorer and choose
   **Download**.

Commit your scripts as you go. Your work is your own repository's history.
