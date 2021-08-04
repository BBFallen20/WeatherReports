from datetime import datetime
from pydantic import BaseModel, Field


class WeatherReportSchema(BaseModel):
    date: datetime = Field(...)
    report_path: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "date": datetime.strptime('2021-10-10T09:00:00', '%Y-%m-%dT%H:%M:%S'),
                "report_path": "/user/PycharmProjects/MongoFU/files_app/reports/test.txt"
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
