from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/")
def get_time():
    current_time = datetime.now()
    current_time = current_time.strftime("%m%d%I%M%Y.%S")
    return {"time": current_time}