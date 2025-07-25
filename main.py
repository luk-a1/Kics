from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload")
async def create_upload_file(tgz_file: UploadFile):
    return {"filename": tgz_file.filename, "content_type": tgz_file.content_type}