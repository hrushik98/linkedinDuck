# Backend

FastAPI starter organized for feature growth:

- `app/main.py`: application bootstrap and middleware
- `app/api/router.py`: top-level API composition
- `app/api/v1/endpoints/`: versioned route modules
- `app/core/config.py`: settings management
- `app/schemas/`: shared response/request schemas
- `tests/`: backend tests

## Run

```bash
cd backend
uv sync --extra dev
uv run uvicorn app.main:app --reload
```
