import tempfile

import pandas as pd
from fastapi import UploadFile, Depends


def csv_to_excel(
        file: UploadFile,
        temp_file = tempfile.NamedTemporaryFile,
) -> None:
    result = pd.read_csv(file.file)
    result.to_excel(temp_file.file.name, index=False)
