import os, docx
from englishword.src.word.making import Making as making

ReL=[]
def F(Li,deep,S):
    global ReL
    if deep==len(Li):
        ReL.append(S)
        return
    for s in Li[deep]:
        if S!=str():
            F(Li,deep+1,S+' '+s)
        else:
            F(Li,deep+1,s)
def Making(Pt, E):
    global ReL
    print(E)
    L=list(E.split())
    Li=[]
    for li in L:
        if li[-1] == 'e':
            List=[
                li,
                li+'s',
                li+'d',
                li[:-1]+'ing'
                ]
        elif li[-1] == 'y':
            List=[
                li,
                li[:-1]+'ies',
                li[:-1]+'ied',
                li+'ing'
                ]
        else:
            List=[
                li,
                li+'s',
                li+'ed',
                li[:-1]+'ing'
                ]
        Li.append(List)
    F(Li,0,str())
    Rl=list(ReL)
    ReL=[]
    print(ReL)
    print(Rl)
    init_path=os.path.dirname(__file__)
    if int(Pt)<10:
        src="PartⅠ 0"+Pt+".docx"
    else:
        src="PartⅠ "+Pt+".docx"
    path = os.path.join(init_path, src)
    doc = docx.Document(path)
    for sentence in doc.paragraphs:
        T=False
        for R in Rl:
            i=0
            while True:
                if i+len(R) >= len(sentence.text):
                    break
                if sentence.text[i:i+len(R)] == R and (i+len(R)+1 == len(sentence.text) or sentence.text[i+len(R)] == ' '):
                    St = sentence.text[:i+1]+'__________'+sentence.text[i+len(R):]
                    As = R
                    T=True
                    break
                i+=1
        if T==True:
            print(St,As)
            return St, As
    return None, None
