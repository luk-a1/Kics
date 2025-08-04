from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from kics_cmd import run_kics_command
from urllib.parse import quote
from pathlib import Path

UploadDir = Path() / '/home/luk/Kics/uploads'
OutputDir = Path() / '/home/luk/Kics/output'
templates = Jinja2Templates(directory="templates")
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

    # -v mapps the UploadDir to the container path
    # -t is for TTY, which is needed for interactive commands
    command = f"docker run --rm -t -v \"{UploadDir}:/path\" -v \"{OutputDir}:/output\" checkmarx/kics:latest scan -p /path/{fileName} -o /output"
    run_kics_command(command)
    command = f"rm {UploadDir}/{fileName}"
    run_kics_command(command)
    return