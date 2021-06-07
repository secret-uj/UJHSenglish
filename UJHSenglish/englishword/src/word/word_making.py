import random, os

def Making(Pt):
    K=list()
    E=list()
    init_path=os.path.dirname(__file__)
    if int(Pt)<10:
        src="PartⅠ 0"+Pt+".txt"
    else:
        src="PartⅠ "+Pt+".txt"
    path = os.path.join(init_path, src)
    with open(path, 'r') as f:
        while True:
            F=f.readline()
            if F==str():
                break
            else:
                i=0
                while True:
                    if i+4>len(F):
                        break
                    elif F[i]=='[':
                        if F[i:i+7] in ["[명][동] ", "[명][형] ", "[형][부] ", "[부][형] ", "[전][접] "]:
                            F1,F2=F.split(F[i:i+7])
                            if i!=0:
                                F=F1[:-1]+"; "+F2
                                i-=1
                            else:
                                F=F1+F2
                                i-=6
                        elif F[i:i+4] in ["[명] ","[형] ","[동] ","[부] ","[전] "]:
                            F1,F2=F.split(F[i:i+4])
                            if i!=0:
                                F=F1[:-1]+"; "+F2
                                i-=1
                            else:
                                F=F1+F2
                                i-=3
                    elif F[i]=='《':
                        i1=i
                    elif F[i]=='》':
                        F1=F[:i1]
                        F2=F[i+2:]
                        F=F1+F2
                        i-=i-i1+1
                    i+=1
                K.append(F[:-1])
                F=f.readline()
                if F in E and K[E.index(F)]==K[-1]:
                    K.pop(-1)
                else:
                    E.append(F[:-1])
    n=len(K)
    K_E=dict()
    S=dict()
    for i in range(n):
        if K.count(K[i])>=2:
            if K[i] in S:
                S[K[i]]|={E[i]}
            else:
                S[K[i]]={E[i]}
        else:
            K_E[K[i]]=E[i]
    for i in S:
        t=0
        while True:
            T=set()
            t+=1
            for j in S[i]:
                T|={j[:t]}
            if len(T)==len(S[i]):
                break
        for k in range(n):
            if K[k]==i:
                #K[k]=i+"\n"+E[k][:t]
                K_E[K[k]]=E[k]
    K_list=dict()
    for i in range(len(K)):
        K3=str(K[i])
        K3=K3.split("\n")[0]
        j=0
        while True:
            if j+3>len(K3):
                break
            elif K3[j:j+2] in ["1.","2.","3.","4.","; "]:
                K1=K3[:j]
                K2=K3[j+2:]
                if K1=='':
                    K3=K2
                else:
                    if K3[j:j+2]!="; ":
                        K3=K1[:-1]+'&'+K2
                    else:
                        K3=K1+'&'+K2
            j+=1
        K_list[K[i]]=list(K3.split('&'))
        for j in range(len(K_list[K[i]])):
            k1=str()
            k2=list()
            t=0
            k0=0
            while True:
                if k0==len(K_list[K[i]][j]):
                    break
                k=K_list[K[i]][j][k0]
                if k=='(':
                    t=1
                elif k==')':
                    t=0
                if K_list[K[i]][j][k0:k0+2]==', ' and t==0:
                    k2.append(k1)
                    k1=str()
                    k0+=1
                else:
                    k1+=k
                k0+=1
            k2.append(k1)
            K_list[K[i]][j]=k2
        for k1 in K_list[K[i]]:
            t=0
            while t!=len(k1):
                k2=k1[t]
                if '(' in k2:
                    i=k2.index('(')
                    j=k2.index(')')
                    K1=k2[:i]
                    K2=k2[j+1:]
                    k4=K1+k2[i+1:j]+K2
                    if j+1<len(k2) and k2[j+1]==' ':
                        K2=K2[1:]
                    elif i-1>=0 and k2[i-1]==' ':
                        K1=K1[:-1]
                    k3=K1+K2
                    k1.remove(k2)
                    k1.append(k4)
                    k1.append(k3)
                    t-=1
                elif '[' in k2:
                    i=k2.index('[')
                    while True:
                        i-=1
                        if k2[i]==' ' or i==0:
                            if i==0:
                                i=-1
                            break
                    j=k2.index(']')
                    K1=k2[:i+1]
                    K2=k2[j+1:]
                    k3=K1+k2[i+1:k2.index('[')]+K2
                    k4=K1+k2[k2.index('[')+1:k2.index(']')]+K2
                    k1.remove(k2)
                    k1.append(k3)
                    k1.append(k4)
                    t-=1
                elif '【' in k2:
                    i=k2.index('】')
                    k3=k2[i+2:]
                    k1.remove(k2)
                    k1.append(k3)
                    t-=1
                t+=1
    random.shuffle(K)
    return K, K_E

