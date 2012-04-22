from datetime import datetime

from django.shortcuts import render


tweets = [
    {'user_name':'jorgebastida', 'message': 'Hello world!', 'timestamp': datetime.now()},
    {'user_name':'jaimeirurzun', 'message': 'I like ponies! http://djangopony.com', 'timestamp': datetime.now()},
    {'user_name':'jorgebastida', 'message': 'Django RULEZZZZZZ', 'timestamp': datetime.now()}
]


def timeline(request):
    return render(request, 'website/index.html', {'tweets': tweets})
