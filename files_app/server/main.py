from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from files_app.server.routes.reports import router as report_router
app = FastAPI()

app.include_router(report_router, tags=["Report"], prefix="/report")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Default page"}




