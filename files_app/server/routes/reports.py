from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from files_app.server.crud.reports import (
    add_report,
    retrieve_reports,
)
from files_app.server.models.weather_report import (
    WeatherReportSchema,
    response_model
)

router = APIRouter()


@router.get("/", response_description="Reports retrieved")
async def get_students():
    students = await retrieve_reports()
    if students:
        return response_model(students, "Reports data retrieved successfully")
    return response_model(students, "Empty list returned")


@router.post("/add", response_description="Report data added into the database")
async def add_student_data(student: WeatherReportSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_report(student)
    return response_model(new_student, "Report added successfully.")
