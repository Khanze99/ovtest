from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from fastapi.staticfiles import StaticFiles

from core.database import SessionLocal
from routes import routes
from ov.templates import templates


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(routes)


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get('/', include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
