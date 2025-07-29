from fastapi import FastAPI, UploadFile
from kics_cmd import run_kics_command
from pathlib import Path

UploadDir = Path() / '/home/luka/KicsWeb/uploads'
#print(UploadDir) #return uploads as a path
app = FastAPI() 

@app.post("/upload")
async def create_upload_file(tgz_file: UploadFile):
    # Reads the data
    fileName = tgz_file.filename
    data = await tgz_file.read()

    # basicaly this means path of UploadDir + fileName
    save_path = UploadDir / fileName

    # Opens the file in binary write mode and saves the data in the specified path

    with open(save_path, "wb") as f:
        f.write(data)

    # first it requires the directory of the file and after that the file name
    command = f"docker run -t -v \"{UploadDir}:/path\" checkmarx/kics:latest scan -p /path/{fileName}"
    return_code = run_kics_command(command)

    return {"filename": tgz_file.filename}