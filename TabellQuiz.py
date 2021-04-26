import random
print(" Ciao Matematici!!! \n Per ogni risposta esatta riceverai 1 Punto \n")
file= open("tabelline.txt", "r")
righe= file.readlines()
file.close()
partite= 0
n= []
punteggio= 0
fatte= []
valido= True
for prova in range(1, int((len(righe)/2) + 1)):
    n.append(prova)
while valido:
    try:
        partite=int((input(" Quanti round vuoi fare?  Digita un numero compreso tra 1 e " + str(int(len(righe)/2)) + " ---> ")))
        rounde= partite
        if(partite not in n):
            valido= True
            print("Riprova, non è un numero compreso tra 1 e " + str(int(len(righe)/2)))
        else:
            valido= False
    except ValueError:
            print("Hai digitato anche lettere, riprova")
while (partite > 0):
    pippo= random.randrange(0, len(righe), 2)
    if (pippo not in fatte):
        risposta= input("Quanto fà " + (righe[pippo][:-1]) + "?   ---> ")
        if risposta == righe[pippo+1][:-1]:
            print(":-D Risposta Esatta!!!\n")
            punteggio+=1
        else:
            print(":-( Hai sbagliato...La risposta corretta era " + (righe[pippo + 1][:-1]) + "\n")
            if punteggio >= 1:
                punteggio-=1
            else:
                punteggio= 0
        partite-=1
        fatte.append(pippo)
print("Hai totalizzato " + str(punteggio) + " come punteggio")
percentuale= punteggio / rounde
if percentuale < 0.25:
    print("mmm... bisogna allenarci di più! Ci vediamo alla prossima partita ;-)")
elif percentuale >= 0.25 and percentuale < 0.50:
    print("Buono...ma sono sicuro sai fare meglio! Ci vediamo alla prossima partita ;-)")
elif percentuale >= 0.50 and percentuale < 0.75:
    print("Bene! Stiamo migliorando! Ci vediamo alla prossima partita :-)")
elif percentuale >= 0.75 and percentuale < 1:
    print("Ottimo, hai quasi la stoffa del campione! Ci vediamo alla prossima partita ;-)")
else:
    print("Ma sei un campione! Ci vediamo alla prossima partita ;-)")


