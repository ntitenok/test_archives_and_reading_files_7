from zipfile import ZipFile
from utilites.archive_pathes import ARCHIVE_PATCH, EXTRACTED_FILES_PATCH
import csv
import os
from openpyxl import load_workbook
import pypdf


class ArhivesPage:

    def extract_file(self, file_name: str):
        with ZipFile(ARCHIVE_PATCH) as zf:
            zf.extract(file_name, EXTRACTED_FILES_PATCH)

    def check_csv_file(self, file_name, expected_data):
        with open(f'{EXTRACTED_FILES_PATCH}\\{file_name}', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            list_row = []
            for row in reader:
                list_row.append(row['Last Name'])
            print(list_row)
            assert list_row == expected_data, f'Результат{list_row}, ожидаемый результат {expected_data}'

    def check_xlsx_file(self, file_name, expected_data):
        workbook = load_workbook(f'{EXTRACTED_FILES_PATCH}\\{file_name}')
        sheet_ranges = workbook.active
        column_c = sheet_ranges['C']
        list_row = []

        for row in range(len(column_c)):
            list_row.append(column_c[row].value)
        list_row.pop(0)
        print(list_row)
        assert list_row == expected_data, f'Результат{list_row}, ожидаемый результат {expected_data}'

    def check_pdf_file(self, file_name, expected_data):
        reader = pypdf.PdfReader(f'{EXTRACTED_FILES_PATCH}\\{file_name}')
        text = (reader.pages[1].extract_text())
        print(text)
        assert expected_data in text, 'Не найден текст'

    def remove_file(self, file_name):
        os.remove(f'{EXTRACTED_FILES_PATCH}\\{file_name}')