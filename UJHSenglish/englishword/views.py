from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from englishword.src.word.word_making import Making as Word_Making
from englishword.src.sentence.sentence_making import Making as Sentence_Making
import os, json

# Create your views here.
K=None
K_E=None
E_S=None
Content={
    'K': K,
    'K_E':K_E,
    'E_S':E_S,
    'request': str(),
    'part': int(),
    'lng': str(),
    'type': str(),
    'type_ans': str(),
    'message': str(),
    }


def index(request):
    global K, K_E, T, E, Score, Content
    content=dict(Content)
    print(content)
    Content['request']=str()
    Content['message']=str()
    return render(request, 'englishword/index.html', content)

def select(request):
    global Question, Answer, K, K_E, Score, Content,pt,tp,test
    pt = request.POST['part']
    ln = request.POST['lng']
    tp = [request.POST['type'], request.POST['type_ans']]
    if tp[0] == "word":
        if tp[1] == "subjective":
            init_path=os.path.dirname(__file__)
            if int(pt)<10:
                src="PartⅠ 0"+pt+".txt"
            else:
                src="PartⅠ "+pt+".txt"
            file = os.path.join(init_path,'src','word', src)
            print("bab3o")
            if os.path.isfile(file) == False:
                Content['message']="아직 업로드되지 않았습니다."
                return HttpResponseRedirect(reverse('index'))
    elif tp[0] == "sentence":
        if tp[1] == "subjective":
            init_path=os.path.dirname(__file__)
            if int(pt)<10:
                src="PartⅠ 0"+pt+".txt"
            else:
                src="PartⅠ "+pt+".txt"
            file = os.path.join(init_path,'src','sentence', src)
            print("babo")
            if os.path.isfile(file) == False:
                Content['message']="아직 업로드되지 않았습니다."
                return HttpResponseRedirect(reverse('index'))
    Content['request']='true'
    Content['part']=pt
    Content['lng']=ln
    Content['type']=tp[0]
    Content['type_ans']=tp[1]
    (K,K_E)=Word_Making(pt)
    Content['K']=json.dumps(K)
    Content['K_E']=json.dumps(K_E)
    if tp[0] == "sentence":
        E_S=Sentence_Making(pt)
        Content['E_S']=json.dumps(E_S)
    return HttpResponseRedirect(reverse('index'))



