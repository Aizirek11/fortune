import random
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Option, SpinHistory

def index(request):
    options = Option.objects.all()
    history = SpinHistory.objects.order_by('-created_at')[:20]
    return render(request, 'wheel/index.html', {'options': options, 'history': history})

@api_view(['GET','POST'])
def options_api(request):
    if request.method=='POST':
        text = request.data.get('text')
        if text:
            Option.objects.create(text=text, source='api')
            return Response({'status':'ok'})
        return Response({'error':'empty'})
    options = Option.objects.all()
    return Response([{'id': o.id, 'text': o.text} for o in options])

@api_view(['DELETE'])
def delete_all_options(request):
    Option.objects.all().delete()
    SpinHistory.objects.all().delete()  # очищаем историю, чтобы новые спины не смешивались
    return Response({'status':'all deleted'})

@api_view(['POST'])
def spin_api(request):
    options = list(Option.objects.all())
    if not options:
        return Response({'error':'no options'})
    result_option = random.choice(options)
    options_text = ", ".join([o.text for o in options])
    SpinHistory.objects.create(options_snapshot=options_text, result=result_option.text)
    return Response({'result': result_option.text})




# Create your views here.
