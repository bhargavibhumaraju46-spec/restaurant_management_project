from datetime import datetime
def current_year(request):
    return{'current_year':datetime.now().year} 
    TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors': [
                    'your_app.context_processors.current_year',
                ],
            },
        },
    ]