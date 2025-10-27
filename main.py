from fastapi import FastAPI, responses, UploadFile, File, Depends
import pandas as pd

from convertor.utils import generate_temp_file

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/csv-to-excel")
def csv_to_excel(
        file: UploadFile = File(...),
        temp_file = Depends(generate_temp_file(".xlsx")),
):
    result = pd.read_csv(file.file)
    result.to_excel(temp_file.file.name, index=False)
    return responses.FileResponse(
        temp_file.file.name,
        media_type="application/vnd.ms-excel",
        headers={'Content-Disposition': 'attachment; filename="Book.xlsx"'},
    )
