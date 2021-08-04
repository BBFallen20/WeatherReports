from datetime import datetime

from bson import ObjectId

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


def retrieve_report(report_id: str):
    report = reports_collection.find_one({"_id": ObjectId(report_id)})
    if report:
        return report_helper(report)
    return False


def add_report(report_data: dict) -> dict:
    report = reports_collection.insert_one(report_data)
    new_report = reports_collection.find_one({"_id": report.inserted_id})
    return report_helper(new_report)


def update_report(report_id: str, data: dict):
    if len(data) < 1:
        return False
    report = reports_collection.find_one({"_id": ObjectId(report_id)})
    if report:
        updated_report = reports_collection.update_one(
            {"_id": ObjectId(report_id)}, {"$set": data}
        )
        if updated_report:
            return True
        return False


def delete_report(report_id: str):
    report = reports_collection.find_one({"_id": ObjectId(report_id)})
    if report:
        reports_collection.delete_one({"_id": ObjectId(report_id)})
        return True
