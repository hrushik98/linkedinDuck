# linkedinDuck

Monorepo starter with:

- `frontend/`: Next.js app (TypeScript, App Router, ESLint)
- `backend/`: FastAPI app with versioned routing and health check

## Frontend

If Node is available on your machine:

```bash
cd frontend
npm run dev
```

## Backend

```bash
cd backend
uv sync --extra dev
uv run uvicorn app.main:app --reload
```
