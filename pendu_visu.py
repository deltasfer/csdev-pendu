#Header

"""
TP2 version Tkinter AIVAZIAN OLIVIER
lien du github : https://github.com/deltasfer/csdev-pendu
"""

#importation des fonction
from random import *
from tkinter import Tk,Button,Entry,Label,Frame,Canvas,PhotoImage
from time import strftime,gmtime



#recup_mots
def recup_mots():
    #liste des mots
    fich=open("mots.txt","r")
    L=fich.read()
    L=L.split(",")
    L[-1] = L[-1][:-1]
    fich.close()

    #trie des éléments selon leur ordres alphabétiques
    L.sort()

    #tri des éléments selon leurs tailles
    L.sort(key=lambda element: len(element))
    return L

#affiche le mot avec _ et des ' '
def write_devine_avec_espaces(M,trouve):
    devine = ''
    for lettre in mot:
        if lettre in trouve:
            devine+=' '+lettre+' '

        else:
            devine+=' _ '
    return devine

#mettre les lettes non deviné sous forme de _ sans ' '
def write_devine(mot,trouve):
    devine = ''
    for lettre in mot:
        if lettre in trouve:
            devine+=lettre

        else:
            devine+='_'
    return devine

#Initialisation du jeu
meilleurscore=8
L=recup_mots()
reussi = False
mot = choice(L)
trouve = [mot[0]] # liste des lettres contenant les lettres valides qu'on a trouvé
rate = [] # liste des essais ratés
essai = 0
secondes = 120

def btn_press():

    if btn_propose['text'] == 'Proposer lettre':
        verify_lettre()
    elif btn_propose['text'] == 'Recommencer':
        try_again()

def maj():
    global secondes
    if secondes > 0 and (not reussi):
        secondes -=1
        label_secondes['text'] = 'Temps restant : '+strftime('%Mmin %Ssec',gmtime(secondes))
    elif not reussi:
        game_over()
    fen.after(1000,maj)


### INITIALISATION FENETRE

couleur = "#3c3e43"

# fenetre
fen = Tk()
fen.title("Pendu")
fen.geometry('600x300')
fen.configure(bg=couleur)


# mot à trouver
mot_affiche = Label(fen,text=write_devine_avec_espaces(mot,trouve),bg=couleur,fg="white",width=35)
mot_affiche.config(font=("Courier", 10))
#mot_affiche.pack(side="left")
mot_affiche.grid(row=1,column=1)

# cadre gauche
Cadre=Frame(fen,relief="groove", bg=couleur)
Cadre.grid(row=2,column=1)

# indications
indices = Label(fen,text="Entrez une lettre et appuyez sur Proposer",bg=couleur,fg="cyan")
indices.grid(row=3,column=1)


# nb d'essais restants
nb_essais = Label(fen,text="Essais restants : 7",bg=couleur,fg="cyan")
nb_essais.grid(row=3,column=1,sticky="S")

# listes lettres
lettres_testes = Label(fen,text='Lettres testées '+str(rate),bg=couleur,fg="white")
lettres_testes.grid(row=1,column=1,sticky='S')

# pour entrer la lettre
entry = Entry(Cadre)
entry.grid(row=1,column=1)

# pour valider la lettre
btn_propose = Button(Cadre,text='Proposer lettre',command=btn_press)
btn_propose.grid(row=1,column=2)

#bouton quitter
btnQuit = Button(fen,text="Quitter le pendu",fg='red',command=fen.destroy)
btnQuit.grid(row=4,column=1)

# temps restant
label_secondes = Label(fen,text='Temps restant : '+strftime('%Mmin %Ssec',gmtime(secondes)),bg=couleur,fg="cyan")
label_secondes.grid(row=4,column=1,sticky="S")


#imagependu
hauteur=280
largeur=280
Canevas = Canvas(fen,width=largeur,height=hauteur,bg=couleur,highlightthickness=0)

images = []
for i in range(1,9):
    # on crée toutes les images du pendu
    images.append(PhotoImage(file="gif//bonhomme"+str(i)+".gif"))

# on affecte la première image
imagependu= Canevas.create_image(hauteur/2,largeur/2,image=images[0])
Canevas.grid(row=1,column=2,rowspan=4,padx=10,pady=10,sticky="E")

maj()


def verify_lettre():
    global reussi,mot,trouve,essai,rate

    if secondes > 0:

        lettre = entry.get()[0]

        if lettre in trouve:
            indices['text'] = "la lettre à déja été donné"
        else:
            if lettre in mot:
                indices['text'] = "bien joué tu as trouvé une lettre !"
                trouve+=[lettre]

                if mot==write_devine(mot,trouve):
                    reussi=True

            elif lettre in rate:
                indices['text'] = "vous avez deja teste cette lettre !"
            else:
                indices['text'] = "la lettre n'est pas dans le mot"
                essai+=1
                rate+=[lettre]
                lettres_testes['text'] = 'Lettres testées '+str(rate)

        mot_affiche['text'] = write_devine_avec_espaces(mot,trouve)

        if reussi :
            you_win()
        else:
            change_bonhomme(essai)
            if essai >= 7:
                game_over()
    else:
        game_over()

def change_bonhomme(essai):
    Canevas.itemconfig(imagependu, image=images[essai])
    nb_essais['text'] = "Essais restants : "+ str(7-essai)

def game_over():
    btn_propose["text"] = 'Recommencer'
    indices['text'] = "GAME OVER, le mot était "+mot

def you_win():
    btn_propose["text"] = 'Recommencer'
    indices['text'] = "Bravo !"

def try_again():
    global mot,reussi,trouve,essai,rate,secondes
    reussi = False
    mot = choice(L)
    trouve = [mot[0]]
    rate = []
    essai = 0
    btn_propose["text"] = 'Proposer lettre'
    mot_affiche['text'] = write_devine_avec_espaces(mot,trouve)
    indices['text'] = "Entrez une lettre et appuyez sur Proposer"
    lettres_testes['text'] = 'Lettres testées '+str(rate)
    secondes = 120



fen.mainloop()
