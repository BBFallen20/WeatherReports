from datetime import datetime

from files_app.server.database import student_collection


def report_helper(report) -> dict:
    return {
        "date": datetime.strptime(report["date"], '%Y-%m-%dT%H:%M:%S'),
        "report_path": report["report_path"]
    }


async def retrieve_reports():
    reports = []
    async for report in student_collection.find():
        reports.append(report_helper(report))
    return reports


async def add_report(report_data: dict) -> dict:
    student = await student_collection.insert_one(report_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return report_helper(new_student)
