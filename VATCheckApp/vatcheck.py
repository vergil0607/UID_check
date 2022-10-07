import openpyxl
from zeep import Client
from datetime import datetime
from io import BytesIO
from .file_storage import store_Github

def read_xl(file):
    workbook = openpyxl.open(file)
    worksheet = workbook[workbook.sheetnames[0]]
    return worksheet


def validate(response):
    if response:
        return "gültig"
    else:
        return "nicht gültig"


def validate_UIDs(file, max_rows=None):
    workbook = openpyxl.open(file)
    worksheet = workbook[workbook.sheetnames[0]]
    if not max_rows:
        max_rows = worksheet.max_row
    client = Client("http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl")
    for j, row in enumerate(worksheet.iter_rows(min_row=1, max_row=max_rows)):
        print(row[0].value)
        if j % 100 == 0:
            print(j)
        if row[0].value is not None:
            try:
                country = row[0].value[:2]
                vat = row[0].value[2:]
                response = client.service.checkVat(countryCode=country, vatNumber=vat)['valid']
                row[4].value = validate(response)

            except Exception as e:
                print(e)
                row[4].value = "ungültiger input"
        else:
            row[4].value = 'blank'

        print(row[4].value)
    return workbook


def handle_uploaded_file(file, rows=None):

    filetype = str(file).split(".")[-1]
    if filetype not in ("xlsx", "xls"):
        print("Bitte ein Excel file verwenden")
    else:
        workbook = validate_UIDs(file, rows)
        print("workbook was validated, next thing is saving")
        # store_Github(workbook)
        filename = str(file).split(".")[0] + '_checked.xlsx'
        workbook.save(f'media/validated_Documents/{filename}')
        print("The file was stored")
        return filename

