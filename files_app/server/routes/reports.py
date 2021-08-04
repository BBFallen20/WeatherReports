from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from files_app.server.crud.reports import (
    add_report,
    retrieve_reports, update_report, delete_report, retrieve_report,
)
from files_app.server.models.weather_report import (
    WeatherReportSchema,
    response_model, error_response_model, UpdateWeatherModel
)

router = APIRouter()


@router.get("/", response_description="Reports retrieved")
def get_students():
    students = retrieve_reports()
    if students:
        return response_model(students, "Reports data retrieved successfully")
    return response_model(students, "Empty list returned")


@router.post("/add", response_description="Report data added into the database")
def add_student_data(student: WeatherReportSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = add_report(student)
    return response_model(new_student, "Report added successfully.")


@router.put("/{id}")
def update_student_data(report_id: str, req: UpdateWeatherModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_report = update_report(report_id, req)
    if updated_report:
        return response_model(
            "Report with ID: {} update is successful".format(report_id),
            "Report updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Report data deleted from the database")
def delete_student_data(report_id: str):
    deleted_student = delete_report(report_id)
    if deleted_student:
        return response_model(
            "Report with ID: {} removed".format(report_id), "Report deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Report with id {0} doesn't exist".format(report_id)
    )


@router.get("/{id}", response_description="Report data retrieved")
def get_student_data(report_id):
    student = retrieve_report(report_id)
    if student:
        return response_model(student, "Report data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Student doesn't exist.")
