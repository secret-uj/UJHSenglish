from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from englishword.src.word.making import Making as Word_Making
from englishword.src.sentence.making import Making as Sentence_Making

# Create your views here.
pt=str()
tp=str()
Question=str()
Answer=str()
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
def Select_Q_A():
    global Content, Question, Answer, K, K_E, Score, pt, tp
    if tp=="subjective":
        Question=K[0]
        Answer=K_E[K[0]]
    elif tp=="sentence":
        while True:
            (Question, Answer) = Sentence_Making(pt, K_E[K[0]])
            if Question!=None:
                break
            else:
                del K[0]
                Score[1]-=1
                if K==list():
                    Content['state']="complete"
                    Content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
                    break


def index(request):
    global K, K_E, T, E, Score, Content
    print(Content)
    return render(request, 'englishword/index.html', Content)

def select(request):
    global Question, Answer, K, K_E, Score, Content,pt,tp
    Content['request']='select'
    pt = request.POST['part']
    Content['part']=pt
    ln = request.POST['lng']
    Content['lng']=ln
    tp = request.POST['type']
    Content['type']=tp
    print("hello",pt,ln,tp)
    (K,K_E)=Word_Making(pt)
    Score=[0,len(K)]
    Content['state']="test"
    Select_Q_A()
    Content['question']=Question

    return HttpResponseRedirect(reverse('index'))

def input(request):
    global Question, Answer, K, K_E, T, E, Score, Content, pt, tp
    Content['request']='input'
    A = request.POST['answer']
    if A == "SKIP":
        return HttpResponseRedirect(reverse('skip'))
    elif A == "HINT":
        return HttpResponseRedirect(reverse('hint'))
    print(K_E[K[0]])
    print(A)
    if A == Answer:
        T="True"
        Score[0]+=1
        del K[0]
        Content['hint']=str()
        if K==list():
            Content['state']="complete"
            Content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
        else:
            Select_Q_A()
            Content['question']=Question
    else:
        T="False"
    Content['question']=Question
    Content['trueorfalse']=T
    return HttpResponseRedirect(reverse('index'))

def skip(request):
    global Question, Answer
    Content['request']='skip'
    Content['skip_message']=Answer
    T="False"
    del K[0]
    Content['hint']=str()
    if K==list():
        Content['state']="complete"
        Content['score']="%d 중 %d 정답 " % (Score[1], Score[0])
    else:
        Select_Q_A()
        Content['question']=Question
    return HttpResponseRedirect(reverse('index'))

def hint(request):
    global Question, Answer
    Content['request']='hint'
    Content['hint']=Answer[:len(Content['hint'])+1]
    return HttpResponseRedirect(reverse('index'))


