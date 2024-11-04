import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List, Optional
import subprocess
import json
from pydantic import BaseModel

UPLOAD_DIR = "/tmp/teste-api"

os.makedirs(UPLOAD_DIR, exist_ok=True)


script_path = Path(__file__).parent / "script.sh"
os.chmod(script_path, 0o755)

app = FastAPI()

class User(BaseModel):
    username: str
    folder: str
    numberMessages: int
    size: int

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):

    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')
    if not set(file.filename).issubset(allowed_chars):
        raise HTTPException(status_code=400, detail="Invalid characters in file name")

    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    status_code = 201 if not os.path.exists(file_path) else 204

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"message": "File uploaded successfully"}, status_code

@app.get("/files/", response_model=List[User])
def list_files(limit: int = 10, offset: int = 0):
    files = [file for file in os.listdir(UPLOAD_DIR) if file.endswith('.csv')]
    files = files[offset: offset + limit]

    return [User(username=file.split('.')[0], folder='', numberMessages=0, size=0) for file in files]

@app.get("/users/{filename}/size", response_model=User)
def get_user_by_size(filename: str, size_type: str = "max"):
    file_path = os.path.join(UPLOAD_DIR, f"{filename}.csv")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File Not Found")

    cmd = f"/bin/sh {script_path} --file {file_path} --size_type {size_type}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    return User(**data)

@app.get("/users/", response_model=List[User])
def get_users_ordered_by_name(order: Optional[str] = "asc", username: Optional[str] = None, limit: int = 10, offset: int = 0):
    order_param = "asc" if order == "asc" else "desc"
    filter_param = f"username={username}" if username else ""

    cmd = f"/bin/sh {script_path} --order={order_param} --filter={filter_param}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    data = sorted([User(**item) for item in data], key=lambda x: x.username)
    data = data[offset: offset + limit]

    return data

@app.get("/users/inbox/{min_messages}/{max_messages}", response_model=List[User])
def get_users_inbox(min_messages: int, max_messages: int, username: Optional[str] = None, limit: int = 10, offset: int = 0):
    filter_param = f"username={username}" if username else ""

    cmd = f"/bin/sh {script_path} --min={min_messages} --max={max_messages} {filter_param}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    data = sorted([User(**item) for item in data], key=lambda x: x.numberMessages)
    data = data[offset: offset + limit]

    return data

