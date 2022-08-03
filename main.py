from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


"""
The reason for writing this API was to help the Android team to get
the date and time of the new devices fixed. Because the and time on
the devices is not correct by default so it was causing errors when
connecting to Web Socket as AWS has some restrictions based on date
and time to connect to the Web Socket.
"""
@app.get("/")
def get_time():
    current_time = datetime.now()
    current_time = current_time.strftime("%m%d%I%M%Y.%S")
    return {"time": current_time}