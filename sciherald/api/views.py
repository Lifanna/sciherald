from django.http import JsonResponse
from django.http import Http404


def index(request):
    return JsonResponse({
        'info': 'There is Sciherald Backend API. For more information go to "/help" route'
    })

def info(request):
    return JsonResponse({
        'api': 'Main page of Sciherald Backend API',
        'info': 'The list of possible api methods',
        'v1': 'Version of api'
    })

def version(request, version_id):
    if version_id != 1:
        raise Http404('Unknown version of api')
    
    return JsonResponse({
        'info': 'version of api is v1'
    })