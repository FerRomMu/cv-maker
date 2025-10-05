# CV Maker

Small project to build and manage CV generation using Python.

---

## 🧩 Project Setup

This repository uses `pip-tools` to manage dependencies and `pre-commit` for code quality checks.

---

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
# On Windows use: .venv\Scripts\activate
```

---

### 2. Install `pip-tools`

Install only `pip-tools` first — it will be used to compile the `.in` files into `.txt`:

```bash
pip install --upgrade pip
pip install pip-tools
```

Recommended version: 7.4.1

---

### 3. Compile and install dependencies

Use `pip-tools` to generate locked dependency files:

```bash
pip-compile requirements-dev.in
```

This will produce `requirements-dev.txt` with fully resolved versions.

Then install the dependencies:

```bash
pip install -r requirements-dev.txt
```

---

### 4. Configure Pre-commit

Once everything is installed, set up the git hooks:

```bash
pre-commit install
```

To check all files manually at any time:

```bash
pre-commit run --all-files
```

---

### 6. Updating dependencies

Whenever you modify `requirements.in` or `requirements-dev.in`, recompile and reinstall:

```bash
pip-compile requirements-dev.in
pip install -r requirements-dev.txt
```

---

### 7. Notes

- `requirements.in` → production dependencies
- `requirements-dev.in` → development-only dependencies (linters, formatters, etc.)
- `pip-tools` ensures dependency consistency across environments.
- `pre-commit` automatically enforces code quality before each commit.
