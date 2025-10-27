from fastapi import FastAPI, responses, UploadFile, File, Depends

from convertor.utils import generate_temp_file
from convertor.services import file_convertor_services as converter

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/csv-to-excel")
def csv_to_excel(
        file: UploadFile = File(...),
        temp_file = Depends(generate_temp_file(".xlsx")),
):
    converter.csv_to_excel(file, temp_file)
    return responses.FileResponse(
        temp_file.file.name,
        media_type="application/vnd.ms-excel",
        headers={'Content-Disposition': 'attachment; filename="Book.xlsx"'},
    )
