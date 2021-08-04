from datetime import datetime

from files_app.server.database import reports_collection


def report_helper(report) -> dict:
    return {
        "date": datetime.strptime(report.get('date'), '%Y-%m-%dT%H:%M:%S'),
        "report_path": report.get('report_path')
    }


def retrieve_reports():
    reports = []
    for report in reports_collection.find():
        reports.append(report_helper(report))
    return reports


def add_report(report_data: dict) -> dict:
    student = reports_collection.insert_one(report_data)
    new_student = reports_collection.find_one({"_id": student.inserted_id})
    return report_helper(new_student)
