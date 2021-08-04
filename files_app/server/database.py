import os

import motor.motor_asyncio

MONGO_DETAILS = os.environ.get('MONGO_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.reports

reports_collection = database.get_collection("weather_reports_collection")
