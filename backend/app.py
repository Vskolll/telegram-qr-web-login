from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

from backend.logging_config import setup_logging
from backend.api.auth import router as auth_router
from backend.api.ws import router as ws_router

app = FastAPI(title="Telegram QR Login")

setup_logging()

app.include_router(auth_router, prefix="/auth")
app.include_router(ws_router, prefix="/auth")

# static
app.mount("/static", StaticFiles(directory="backend/frontend/static"), name="static")

@app.get("/")
def index():
    return FileResponse("backend/frontend/index.html")

@app.get("/admin")
def admin():
    return FileResponse("backend/frontend/admin.html")

@app.get("/next", response_class=HTMLResponse)
def next_page():
    with open("backend/frontend/next.html", "r", encoding="utf-8") as f:
        html = f.read()

    # ⬇️ сервер управляет таймером
    return """
    <script>
      window.MATCH_TIMER_ENABLED = true;
    </script>
    """ + html
