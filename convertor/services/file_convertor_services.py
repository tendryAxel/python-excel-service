import io
import tempfile

import pandas as pd
from fastapi import UploadFile, Depends


async def csv_to_excel(
        file: UploadFile,
        temp_file = tempfile.NamedTemporaryFile,
) -> None:
    contents = await file.read()
    contents = io.StringIO(contents.decode("utf-8"))
    result = pd.read_csv(contents)
    result.to_excel(temp_file.file.name, index=False)
