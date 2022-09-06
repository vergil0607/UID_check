from github import Github
from tempfile import NamedTemporaryFile
import base64
import openpyxl
import os
from decouple import config

def store_Github(workbook):
    key = "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"
    g = Github(key)

    f = NamedTemporaryFile(delete=False)
    workbook.save(f.name)
    data = f.read()
    f.close()

    # Then play with your Github objects:
    repository = g.get_user().get_repo('UID_check')
    contents = repository.get_contents("UID_numbers.xlsx")

    f = repository.update_file("UID_numbers.xlsx", "Update UID", data, contents.sha)

    return "file was stored"

