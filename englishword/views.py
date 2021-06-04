from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from englishword.src.word.making import Making

# Create your views here.

K=None
K_E=None

def index(request):
    content={'question':str()}
    if K!=None:
        content={'question': K[0]}
    return render(request, 'englishword/index.html', content)

def select(request):
    global K, K_E
    pt = request.POST['part']
    ln = request.POST['lng']
    tp = request.POST['type']
    print("hello",pt,ln,tp)
    (K,K_E)=Making(pt)
    return HttpResponseRedirect(reverse('index'))

