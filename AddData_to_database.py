import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


cred = credentials.Certificate("serviceAccountKey.json")#generate your service account key
firebase_admin.initialize_app(cred,{
    'databaseURL': os.environ['API_KEY']
    
})
ref=db.reference('Students')

data={
"321654": # in order to mark the attendace of the person, image name should be 321654.png same goes for all.
        {
            "name":"Atul Sharma",
            "major": "robotics",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"852741":
        {
            "name": "EMILY BLUNT ",
            "major": "economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"963852":
    {
        "name": "ELON MUSK  ",
        "major": "economics",
        "starting_year": 2018,
        "total_attendance": 12,
        "standing": "B",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
"12345":
    {
        "name": "MARK ZUCKERBERG",
        "major": "facebook",
        "starting_year": 2018,
        "total_attendance": 12,
        "standing": "B",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    
    

}

for key,value in data.items():
    ref.child(key).set(value)