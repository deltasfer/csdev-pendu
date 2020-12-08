#Header

"""
TP2 version console AIVAZIAN OLIVIER
lien du github : https://github.com/deltasfer/csdev-pendu
"""

#importation des fonction
from random import *
from tkinter import Tk,Button,StringVar,Entry



#Initialisation
meilleurscore=8

L=[]
#recup_mots
def recup_mots():
    global L
    #liste des mots
    fich=open("mots.txt","r")
    L=fich.read()[:-1]
    L=L.split(",")
    print(L)
    fich.close()

    #trie des éléments selon leur ordres alphabétiques
    L.sort()

    #tri des éléments selon leurs tailles
    L.sort(key=lambda element: len(element))

#Le jeu
def jeu():

    M=choice(L)
    essai=0
    reussi=False
    trouve=[M[0]]
    rate = [] # liste des essais ratés
    D=write_devine(M,trouve)
    afficher = ''
    for lettre in D:
        afficher+= ' '+lettre+' '
    print(afficher)
    while essai!=8 and reussi==False:

        A=input("mettre une lettre :")

        if A in trouve:
            print("le lettre à déja été donné")
        else:
            if A in M:
                trouve+=[A]
                D=write_devine(M,trouve)

                if D==M:
                    reussi=True

            elif A in rate:
                print("vous avez deja teste cette lettre")
            else:
                print("la lettre n'est pas dans le mot")
                essai+=1
                rate+=[A]

        afficher = ''
        for lettre in D:
            afficher+= ' '+lettre+' '
        print(afficher,"il vous reste :",8-essai,"essais")

    if reussi==True:
        print("vous avez gagné, le mot était ",M )
        return essai
    else:
        print("vous avez perdu, le mot était ",M )
        return 8

#mettre les lettes non deviné sous forme de _
def write_devine(mot,trouve):
    devine = ''
    for lettre in mot:
        if lettre in trouve:
            devine+=lettre

        else:
            devine+='_'
    return devine

#faire jouer une personne
def jouer():
    global meilleurscore
    score=jeu()

    if score<=meilleurscore:
        meilleurscore=score
    print("votre meilleur score est de ",meilleurscore,"fautes")
    rejouer=input("voulez vous rejouer :")
    if rejouer=="oui":
        jouer()
    else:
        print("Au revoir")


recup_mots()
jouer()
