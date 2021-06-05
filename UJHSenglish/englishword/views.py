from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from englishword.src.word.making import Making

# Create your views here.

K=None
K_E=None
T=None
E="False"
Score=list()

def index(request):
    global K, K_E, T, E, Score
    content={'question': None, 'trueorfalse': None, 'estimation': "False", "score": str(), "state":None}
    if K==list():
        content['state']="complete"
        content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
    elif K!=None:
        content['question']=K[0]
        content['trueorfalse']=T
        content['estimation']=E
    E=False
    return render(request, 'englishword/index.html', content)

def select(request):
    global K, K_E, Score
    pt = request.POST['part']
    ln = request.POST['lng']
    tp = request.POST['type']
    print("hello",pt,ln,tp)
    (K,K_E)=Making(pt)
    Score=[0,len(K)]
    return HttpResponseRedirect(reverse('index'))

def input(request):
    global K, K_E, T, E, Score
    A = request.POST['answer']
    if A == "SKIP":
        return HttpResponseRedirect(reverse('skip'))
    print(K_E[K[0]])
    print(A)
    if A == K_E[K[0]]:
        T="True"
        Score[0]+=1
        del K[0]
    else:
        T="False"
    E="True"
    return HttpResponseRedirect(reverse('index'))

def skip(request):
    T="False"
    del K[0]
    return HttpResponseRedirect(reverse('index'))


