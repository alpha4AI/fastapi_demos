"""
Author: alpha<alpha@57blocks.com>
Time: 2024-06-17,
Description:This script is used to serve fastapi demo
"""
from fastapi import FastAPI, File, UploadFile
import cv2
import shutil
import base64

app = FastAPI()


# Post,put,get,delete are supported ,and the local function must be  same with the server
@app.post("/predict/")
async def load(file: UploadFile = File(...)):
    """

    :param file:
    :return:
    """
    with open(f"temp_{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image_path = buffer.name
    data = cv2.imread(image_path, -1)
    _, encoded_image = cv2.imencode('.jpg', data)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    return {"base64_image": base64_image}
# Then run the server in command line.
# uvicorn fastapi_serve_demo:app --host 0.0.0.0 --port 8000
