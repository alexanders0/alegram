""" Post views """

#Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Alexander Sánchez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Vía Láctea',
        'user': 'Matt',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Neil deGrasse Tyson',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    },
    
]


def list_posts(request):
    """ List existing posts """
    content = []
    for post in posts:
        content.append(""" 
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(content))
