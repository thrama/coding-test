import smtplib

def postino():
    """
    Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
    Server: smtp.gmail.com
    Porta: 587
    Si richiedono: Username, Password, Destinatario, Oggetto e Contenuto
    """

    user_mittente = input("Inserisci l'Username --> ")
    password = input("Inserisci la Password --> ")
    destinatario = input("A chi stiamo spedendo questa Mail? ")
    oggetto = "Subject: " + input("Inserisci l'oggetto della Mail, quindi premi invio: ")
    contenuto = "\n\n" + input("Ora puoi inserire il contenuto Mail: ") #\n\n fa si che il contenuto venga separato dall'oggetto
    messaggio = oggetto + contenuto
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo() #effettuo l'hello col Server
    email.starttls() #avvio il canale TLS
    email.login(user_mittente,password) #effettuo il login
    print("Sto inviando...")
    email.sendmail(user_mittente,destinatario,messaggio)
    email.quit()
    print("Messaggio Inviato!")