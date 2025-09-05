def django_powered(request):
    return {'powered_by_django': 'powered by Django'}
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors':[
                ...
                'myapp.context_processors.django_powered',
            ],
        },
    },
]     