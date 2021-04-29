import random

print(" Ciao Matematici!!! \n Per ogni risposta esatta riceverai 1 Punto \n")

file= open("tabelline.txt", "r")   # leggo il contenuto del file
righe= file.readlines()
file.close()
# creo variabili
partite= 0   #una come contatore partite
n= []   #una lista che mi mostra tutte le possibili partite
punteggio= 0   #una che conteggia i punti
fatte= []   #una lista che evita la ripetizione della stessa domanda sulla stessa partita
valido= True   #una che convalida l'inizio partita

for prova in range(1, int((len(righe)/2) + 1)):
    n.append(prova)  #riempio la lista n con tutte le possibili partite
    
while valido:   #finchè non verrà digitato un numero corretto non parte il gioco
    try:
        partite=int((input(" Quanti round vuoi fare?  Digita un numero compreso tra 1 e " + str(int(len(righe)/2)) + " ---> ")))
        rounde= partite   #variabile che determinerà la percentuale a fine gioco
        if(partite not in n):
            valido= True
            print("Riprova, non è un numero compreso tra 1 e " + str(int(len(righe)/2)))
        else:
            valido= False
    except ValueError:
            print("Hai digitato anche lettere o simboli, riprova")
            
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
        fatte.append(pippo)   #riempio la lista fatte con la domanda già fatta così da non ripeterla
        
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


