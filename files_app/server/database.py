import os

import pymongo

MONGO_URL = os.environ.get('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)

database = client.reports

reports_collection = database["weather_reports_collection"]
