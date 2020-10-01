""" alegram views """
# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """ return a greeting """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {now}')


def sort_integers(request):
    """ Return a JSON response with sorted integers.
        For more information about JsonResponse:
        https://docs.djangoproject.com/es/3.1/ref/request-response/
        request: localhost:8000/sorted/?numbers=13,40,78,27,1,11,19
    """
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully'
    }
    numbers = {'numbers': sorted_numbers}
    # import pdb; pdb.set_trace()
    # breakpoint() -> es un shortcut para import pdb; pdb.set_trace()
    return JsonResponse(data, json_dumps_params={'indent': 2}, safe=False)


def say_hi(request, name, age):
    """ Return a greeting. """
    if age < 12:
        message = f'Sorry {name}, you are not alloowed here'
    else:
        message = f'Hello, {name}! Welcome to Alegram'
    return HttpResponse(message)
