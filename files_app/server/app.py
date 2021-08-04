from fastapi import FastAPI
from files_app.server.routes.reports import router as report_router
app = FastAPI()

app.include_router(report_router, tags=["Report"], prefix="/report")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Default page"}




