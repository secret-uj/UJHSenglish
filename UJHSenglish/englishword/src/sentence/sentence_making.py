import random, os

def Making(Pt):
    Q=dict()
    init_path=os.path.dirname(__file__)
    if int(Pt)<10:
        src="PartⅠ 0"+Pt+".txt"
    else:
        src="PartⅠ "+Pt+".txt"
    path = os.path.join(init_path, src)
    with open(path, 'r', encoding='UTF8') as f:
        while True:
            F0=f.readline()
            if F0==str():
                break
            F1=f.readline()
            F2=f.readline()
            F3=f.readline()
            Q[F0[:-1]]=[F1[:-1],F2[:-1],F3[:-1]]
    return Q

