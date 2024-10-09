'''1. recept(antal)
3 st ägg
3 dl strösocker
2 tsk vaniljsocker
2 tsk bakpulver
3 dl vetemjöl
75 g smör
1 dl vatten
dela receptet med 4 för att undvika 
return ägg, strösocker, vaniljsocker, bakpulver, vetemjöl, smör, vatten

2. Tidsåtgången ska beräknas som 30 minuter fast tid (oavsett antal personer) samt dessutom ytterligare 3 minuter för varje person kakan är avsedd för.
tidblanda(antal)
tidgradda(antal)

3. sockerkaka(antal)
'''

import math
#antal=7
print("Hur många skall äta kaka?")
antal = int(input())
def recept(antal):
    
    ägg = math.ceil(antal * (3/4))
    strösocker = ((3 / 4) * antal)        #3
    vaniljsocker = ((3 / 4) * antal)      #tsk
    bakpulver = ((2 / 4) * antal)         #tsk
    vetemjöl = ((3 / 4) * antal)          #dl
    smör = ((75 / 4) * antal)             #g
    vatten = ((1 / 4) * antal)            #dl
    
    print(ägg, " st ägg")
    print(strösocker, " tsk strösocker")
    print(vaniljsocker, " tsk vaniljsocker")
    print(bakpulver, " tsk bakpulver")
    print(vetemjöl, " dl vetemjöl")
    print(smör, " g smör")
    print(vatten, " dl vatten")

def tidblanda(antal):
    blanda = 10 + antal
    return blanda

def tidgradda(antal):
    gradda = 30 + (antal * 3)
    return gradda

def sockerkaka(antal):
    print("Recept för ", antal, " personer")
    print( "Tillagnings tid för sockerkakan är ", tidblanda(antal) + tidgradda(antal) )
    recept(antal)

sockerkaka(antal)
#sockerkaka(antal=4)