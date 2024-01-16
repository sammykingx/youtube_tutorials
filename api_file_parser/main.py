from fastapi import FastAPI, UploadFile
import utils, file_reader


app = FastAPI(
        title="Api File Parser",
        summary="This is the summary for my api"
    )


@app.get("/")
def index():
    """the index of app"""

    return {"msg": "connection successfull"}


@app.post("/uploadFile")
async def upload_file(file: UploadFile):
    """uploads file"""

    utils.check_file(file)
    binary_data = await file.read()
    file_data = file_reader.read_file(binary_data)
    
    return file_data
