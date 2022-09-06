from django.shortcuts import redirect, render
from django.core.files.storage import default_storage
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import time
from .models import Document
from .forms import DocumentForm
from .vatcheck import handle_uploaded_file
from datetime import datetime
import openpyxl
import os


def my_view(request):
    if request.method == 'GET':
        return render(request, 'list.html')
    if request.method == 'POST':
        print('post request')
        file = request.FILES.get('files[]', None)
        try:
            print("In view wird handle uploaded File gestartet")
            filename = handle_uploaded_file(file, rows=20)
            if filename:
                download_file = f'https://github.com/vergil0607/UID_check/blob/master/UID_numbers.xlsx?raw=true'
                return JsonResponse({'msg':'<div class="alert alert-success" role="alert">File erfolgreich validiert</div>',
                                     'download':
                                         f'<button id="download" class="btn btn-success text-light">'
                                         f'<a class="text-light" href="{download_file}" download>Download</a>'
                                         f'</button>'})
            else:
                return JsonResponse({'msg':'<div class="alert alert-danger" role="alert">Bitte ein Excel file uploaden</div>'})

        except Exception as e:
            print(e)
            return JsonResponse({'msg': '<div class="alert alert-danger" role="alert">Ein unerwartetes Problem ist aufgetreten</div>'})
    return render(request, 'list.html', )

