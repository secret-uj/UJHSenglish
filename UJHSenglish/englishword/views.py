from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from englishword.src.word.making import Making

# Create your views here.

K=None
K_E=None
T=None

def index(request):
    global K, K_E, T
    content={'question':str(), 'T': T}
    if K!=None:
        content={'question': K[0], 'T': T}
    return render(request, 'englishword/index.html', content)

def select(request):
    global K, K_E
    pt = request.POST['part']
    ln = request.POST['lng']
    tp = request.POST['type']
    print("hello",pt,ln,tp)
    (K,K_E)=Making(pt)
    return HttpResponseRedirect(reverse('index'))

def input(request):
    global K, K_E, T
    A = request.POST['answer']
    print(K_E[K[0]])
    print(A)
    if A == K_E[K[0]]:
        T="True"
        del K[0]
    else:
        T="False"
    return HttpResponseRedirect(reverse('index'))


