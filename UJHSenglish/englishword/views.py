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
Content={
    'request': str(),
    'part': int(),
    'lng': str(),
    'type': str(),
    'question': None,
    'trueorfalse': None,
    'estimation': "False",
    "score": str(),
    'state': str(),
    'skip_message': str(),
    "hint": str(),
    }
def index(request):
    global K, K_E, T, E, Score, Content
    print(Content)
    return render(request, 'englishword/index.html', Content)

def select(request):
    global K, K_E, Score, Content
    Content['request']='select'
    pt = request.POST['part']
    Content['part']=pt
    ln = request.POST['lng']
    Content['lng']=ln
    tp = request.POST['type']
    Content['type']=tp
    print("hello",pt,ln,tp)
    (K,K_E)=Making(pt)
    Score=[0,len(K)]
    Content['state']="test"
    Content['question']=K[0]
    return HttpResponseRedirect(reverse('index'))

def input(request):
    global K, K_E, T, E, Score, Content
    Content['request']='input'
    A = request.POST['answer']
    if A == "SKIP":
        return HttpResponseRedirect(reverse('skip'))
    elif A == "HINT":
        return HttpResponseRedirect(reverse('hint'))
    print(K_E[K[0]])
    print(A)
    print(K)
    if A == K_E[K[0]]:
        T="True"
        Score[0]+=1
        del K[0]
        Content['hint']=str()
    else:
        T="False"
    if K==list():
        Content['state']="complete"
        Content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
    else:
        Content['question']=K[0]
        Content['trueorfalse']=T
    return HttpResponseRedirect(reverse('index'))

def skip(request):
    Content['request']='skip'
    Content['skip_message']=K_E[K[0]]
    T="False"
    del K[0]
    if K==list():
        Content['state']="complete"
        Content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
    else:
        Content['question']=K[0]
    return HttpResponseRedirect(reverse('index'))

def hint(request):
    Content['request']='hint'
    Content['hint']=K_E[K[0]][:len(Content['hint'])+1]
    return HttpResponseRedirect(reverse('index'))


