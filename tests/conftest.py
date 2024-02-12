import os.path
import shutil

import pytest
from zipfile import ZipFile, ZIP_DEFLATED
from utilites.archive_pathes import TESTDATA_PATH, ARCHIVE_PATCH, EXTRACTED_FILES_PATCH



@pytest.fixture(autouse=True,scope='session')
def test_create_archive():
    os.mkdir(EXTRACTED_FILES_PATCH)
    with ZipFile(ARCHIVE_PATCH, 'a') as my_zip:
        for folder, subfolders, files in os.walk(str(TESTDATA_PATH)):
            for file in files:
                my_zip.write(os.path.join(folder, file), file, compress_type=ZIP_DEFLATED)

    yield
    os.remove(ARCHIVE_PATCH)
    shutil.rmtree(EXTRACTED_FILES_PATCH)

