# OWASP FinBot CTF

See Collaborator Hub for details on this project: https://github.com/OWASP-ASI/FinBot-CTF-workstream


## Dev Guide (Temporary)

** Warning: `main` branch is potentially unstable **

Please follow below instructions to test drive the current branch

### Prerequisites

Check if you have the required tools:
```bash
python scripts/check_prerequisites.py
```

### Setup

```bash
# Install dependencies
uv sync

# Setup database (defaults to sqlite, runs migrations)
uv run python scripts/db.py setup

# For PostgreSQL: start the database server first
docker compose up -d postgres
DATABASE_TYPE=postgresql uv run python scripts/db.py setup

# Start the platform
uv run python run.py
```

Platform runs at http://localhost:8000
