from django.shortcuts import render
from django.http import JsonResponse
from .vatcheck import handle_uploaded_file


def my_view(request):
    if request.method == 'GET':
        return render(request, 'list.html')
    if request.method == 'POST':
        file = request.FILES.get('files[]', None)
        try:
            print("In view wird handle uploaded File gestartet")
            filename = handle_uploaded_file(file)
            if filename:
                download_file = f'/media/validated_Documents/{filename}'
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

