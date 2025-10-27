from typing import Generator

from fastapi import FastAPI, responses, UploadFile, File, Depends
import pandas as pd
import tempfile


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

def generate_temp_file() -> Generator[tempfile.NamedTemporaryFile, None, None]:
    file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsx",
    )
    try:
        yield file
    finally:
        file.delete = True
        del file

@app.post("/csv-to-excel")
def csv_to_excel(file: UploadFile = File(...), temp_file = Depends(generate_temp_file)):
    result = pd.read_csv(file.file)
    result.to_excel(temp_file.file.name, index=False)
    return responses.FileResponse(
        temp_file.file.name,
        media_type="application/vnd.ms-excel",
        headers={'Content-Disposition': 'attachment; filename="Book.xlsx"'},
    )
