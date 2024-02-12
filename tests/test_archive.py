from pages.archives_page import ArhivesPage


class TestArchives(ArhivesPage):
    expected_data_sheet_csv_xlsx = ['Abril', 'Hashimoto', 'Gent', 'Hanner', 'Magwood', 'Brumm', 'Hurn', 'Melgar',
                                    'Weiland',
                                    'Winward', 'Bouska', 'Unknow', 'Ascencio', 'Zabriskie', 'Hazelton', 'Pia', 'Benito',
                                    'Perrine', 'Curren', 'Strawn', 'Partain', 'Eudy', 'Cuccia', 'Dalby', 'Prothro',
                                    'Hail',
                                    'Vong', 'Beaudreau', 'Gangi', 'Trumbull', 'Muntz', 'Becker', 'Grindle', 'Claywell',
                                    'Borger', 'Hacker', 'Wachtel', 'Pfau', 'Mccrystal', 'Karner', 'Underdahl', 'Darity',
                                    'Sanor', 'Harn', 'Martina', 'Lafollette', 'Cail', 'Abbey', 'Danz', 'Alkire']

    expected_data_pdf = ""

    file_name_csv = 'file_example_XLSX_50.csv'

    file_name_xlsx = 'file_example_XLSX_50.xlsx'

    file_name_pdf = 'Python Testing with Pytest (Brian Okken) (1).pdf'

    def test_csv_archive(self):
        self.extract_file(self.file_name_csv)
        self.check_csv_file(self.file_name_csv, self.expected_data_sheet_csv_xlsx)
        self.remove_file(self.file_name_csv)

    def test_xlsx_archive(self):
        self.extract_file(self.file_name_xlsx)
        self.check_xlsx_file(self.file_name_xlsx, self.expected_data_sheet_csv_xlsx)
        self.remove_file(self.file_name_xlsx)

    def test_pdf_archive(self):
       self.extract_file(self.file_name_pdf)
       self.check_pdf_file(self.file_name_pdf, self.expected_data_pdf)
       self.remove_file(self.file_name_pdf)


