from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    weekday = datetime.now().strftime("%A")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Today is {weekday}.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
