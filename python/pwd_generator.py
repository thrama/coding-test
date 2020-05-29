from random import randint

def pwd_generator(t):
    """
    Scrivi una funzione generatrice di password. La funzione deve generare una 
    stringa alfanumerica di 8 caratteri qualora l'utente voglia una password 
    semplice, o di 20 caratteri ascii qualora desideri una password più 
    complicata.
    """

    complexChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&@#"
    complexLen = 20
    simpleChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    simpleLen = 8
    passwd = ""


    if (t == "s"):
        for _ in range(int(simpleLen)):
            passwd += simpleChar[randint(0, len(simpleChar))]

    elif (t == "c"):
        for _ in range(int(complexLen)):
            passwd += complexChar[randint(0, len(complexChar))]
    else:
        print("Carattere inserito non riconosciuto.")
    
    return passwd

t = input("Inserisci il tipo di password [Simple/Complex]: ")
print ("La passwod generata è: " + pwd_generator(t))
