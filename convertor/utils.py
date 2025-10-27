import tempfile
from typing import Callable, Generator


def generate_temp_file(suffix: str) -> Callable[[], Generator[tempfile.NamedTemporaryFile, None, None]]:
    def file_generator():
        file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        )
        try:
            yield file
        finally:
            file.delete = True
            del file
    return file_generator
