from tkinter import *
from tkinter import ttk
import numpy as np
from morpion import *



global page
page = Tk()
def display():
    """

    :return: page lobby avec ses attributs
    """
    global page
    page.destroy()
    pageLobby = Tk ()
    pageLobby.geometry("500x500") #dimension de la fenetre
    pageLobby.minsize(500,500)
    pageLobby.title("MORPION") #titre de la fenetre
    #pageLobby.iconbitmap('ggg.avif') #(a changer) pour l'image a cote du titre sur la page
    pageLobby.configure(bg="#5B696B") #background
    pageLobby.resizable(False,False) #empeche l'utilisateur de changeer la taille de la fenetr



    def Morp():
        """

        :return: tout simplement le jeu en lui meme
        """
        mj = np.zeros((3, 3))
        global page
        page = Tk()
        page.geometry("500x500")  # dimension de la fenetre
        page.minsize(500, 500)
        page.title("MORPION")  # titre de la fenetre
        # page.iconbitmap('ggg.avif') #(a changer) pour l'image a cote du titre sur la page
        page.configure(bg="#5B696B")  # background
        page.resizable(False, False)  # empeche l'utilisateur de changeer la taille de la fenetre

        buttonExite = Button(page, text="Exit", font=("Courrier", 10), bg="#37463D", fg="#F8FBF1",
                             command=quit, )  # atribut du button
        buttonExite.place(x=10, y=10, width=41)  # position et taille du button
        buttonLobby = Button(page, text="Lobby", font=("Courrier", 10), bg="#585B4C", fg="#F8FBF1",
                             command=display, )  # atribut du button
        buttonLobby.place(x=450, y=10, width=41)  # position et taille du button

        label_title = Label(page, text="MORPION", font=("Courier", 40), bg="#5B696B", fg="#37463D")
        label_title.place(x=100, y=10, width=300)


        def actionegal():
            """

            :return: retourne une fenetre resumant la partie -> egalité dans ce cas la
            """
            pageegal = Tk()
            pageegal.geometry("250x250")  # dimension de la fenetre
            pageegal.configure(bg="#5B696B")
            lbl = Label(pageegal, text="Egalité", font=("Courier", 15), bg="#5B696B")
            lbl.place(x=5, y=45, width=250)

            lbl3 = Label(pageegal, text="DOMAGE", font=("Courier", 30), bg="#5B696B")
            lbl3.place(x=4, y=90, width=250)

            lbl2 = Label(pageegal, text="Pour rejouer appuyez ici !!!", font=("Courier", 10), bg="#5B696B")
            lbl2.place(x=5, y=150, width=250)
            bttn1 = Button(pageegal, text="Relencer", font=("Courrier", 8), bg="#585B4C", fg="#F8FBF1",
                           command=lambda: display())
            bttn1.place(x=100, y=190, width=50)


        def winX():
            """

            :return: retourne une fenetre resumant la partie -> victoire pour X dans ce cas la
            """
            pagewinX = Tk()
            pagewinX.geometry("250x250")  # dimension de la fenetre
            pagewinX.configure(bg="#5B696B")
            lbl_pagewinX = Label(pagewinX, text="Le Joueur X a Gagné", font=("Courier", 15), bg="#5B696B")
            lbl_pagewinX.place(x=5, y=45, width=250)

            lbl_pagewinX1 = Label(pagewinX, text="GG", font=("Courier", 40), bg="#5B696B")
            lbl_pagewinX1.place(x=4, y=90, width=250)

            lbl_pagewinX2 = Label(pagewinX, text="Pour rejouer appuyez ici !!!", font=("Courier", 10), bg="#5B696B")
            lbl_pagewinX2.place(x=5, y=160, width=250)
            bttn = Button(pagewinX, text="Relencer", font=("Courrier", 8), bg="#585B4C", fg="#F8FBF1",
                          command=lambda: display())
            bttn.place(x=100, y=190, width=50)


        def winO():
            """

            :return: retourne une fenetre resumant la partie -> victoire pour 0 dans ce cas la
            """
            pagewinO = Tk()
            pagewinO.geometry("250x250")  # dimension de la fenetre
            pagewinO.configure(bg="#5B696B")
            lbl_pagewinO = Label(pagewinO, text="Le Joueur O a Gagné", font=("Courier", 15), bg="#5B696B")
            lbl_pagewinO.place(x=5, y=45, width=250)

            lbl_pagewinO1 = Label(pagewinO, text="GG", font=("Courier", 40), bg="#5B696B")
            lbl_pagewinO1.place(x=4, y=90, width=250)

            lbl_pagewinO2 = Label(pagewinO, text="Pour rejouer appuyez ici !!!", font=("Courier", 10), bg="#5B696B")
            lbl_pagewinO2.place(x=5, y=150, width=250)
            bttn3 = Button(pagewinO, text="Relencer", font=("Courrier", 8), bg="#585B4C", fg="#F8FBF1",
                           command=lambda: display())
            bttn3.place(x=100, y=190, width=50)


        global compteurTour
        compteurTour = 0



        def action(button, case):
            """

            :param button: le bouton appuyé
            :param case: la position du bouton
            :return:met une x ou un o sur les case + renvoi a la matrice la position du btn
            """
            global compteurTour
            print(case)
            if compteurTour % 2 == 0:
                button.config(text="X")
                button.config(state=DISABLED)
                compteurTour += 1
                majMatrice(case, mj)
                win = vérifWin(mj)
                if win == "le joueur 1 à gagner":
                    print(mj)
                    print(win)  # si joueur 1 à gagner, arrête le jeu et print que le joueur 1 à gagner
                    winX()
                elif win == "Egalité":
                    print(mj)
                    print(win)  # si égalité, arrête le jeu et print égalité
                    actionegal()

            else:
                button.config(text="O")
                button.config(bg="#585B4C")
                button.config(state=DISABLED)
                compteurTour += 1
                majMatrice(case, mj)
                print(mj)
                win = vérifWin(mj)
                if win == "le joueur 2 à gagner":
                    print(mj)
                    print(win)  # si joueur 2 à gagner, arrête le jeu et print que le joueur 2 à gagner
                    winO()
                elif win == "Egalité":
                    print(mj)
                    print(win)  # si égalité, arrête le jeu et print égalité
                    actionegal()


        # creation des buttons
        """
        nom du bouton = Button(page, le texte dans le boutton, la couleur du boutton, sa taille, sa command etc)
        """
        button1 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button1": action(button1, 1))
        button2 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button2": action(button2, 2))
        button3 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button3": action(button3, 3))
        button4 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button4": action(button4, 4))
        button5 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button5": action(button5, 5))
        button6 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button6": action(button6, 6))
        button7 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button7": action(button7, 7))
        button8 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button8": action(button8, 8))
        button9 = Button(page, text="", bg="#37463D", width=90, command=lambda widget="button9": action(button9, 9))

        # creation des collones et lignes
        """
        Ici on créait des colonnes et lignes pour notre page
        """
        page.columnconfigure(0, weight=1)
        page.columnconfigure(1, weight=1)
        page.columnconfigure(2, weight=1)
        page.rowconfigure(0, weight=1)
        page.rowconfigure(1, weight=1)
        page.rowconfigure(2, weight=1)
        page.rowconfigure(3, weight=1)

        # placement des boutons au bon endroit
        """
        Cela sert a placer les bouttons dans des colones et lignes définies a l'avance
        """
        button1.grid(row=1, column=0, sticky='nsew')
        button2.grid(row=1, column=1, sticky='nsew')
        button3.grid(row=1, column=2, sticky='nsew')
        button4.grid(row=2, column=0, sticky='nsew')
        button5.grid(row=2, column=1, sticky='nsew')
        button6.grid(row=2, column=2, sticky='nsew')
        button7.grid(row=3, column=0, sticky='nsew')
        button8.grid(row=3, column=1, sticky='nsew')
        button9.grid(row=3, column=2, sticky='nsew')

        page.mainloop()  # pour laisser la fenetre ouverte



    def M():
        """

        :return: detruis le lobby et lance le jeu (pour le bouton JOUER)
        """
        pageLobby.destroy()
        Morp()

    buttonExite = Button(pageLobby,text="Exit",font=("Courrier",10), bg="#37463D", fg="#F8FBF1", command =quit,) #atribut du button
    buttonExite.place(x=10, y=10, width=41) #position et taille du button

    buttonJouer = Button(pageLobby,text="Jouer",font=("Courrier",60), bg="#37463D", fg="#24D26D", command = lambda :M(),)
    buttonJouer.place(x=125, y=250, width=250,height=100)




    label_title = Label(pageLobby, text="MORPION", font=("Courier", 53), bg="#5B696B", fg="#37463D")
    label_title.place(x=100, y=100, width=300)

    pageLobby.mainloop()   #pour laisser la fenetre ouverte


display()


