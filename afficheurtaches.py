"""
Modue afficheurtache
Propose une classe qui permet la gestion d'une TODOList en mode Console
"""
class Afficheur:

    def __init__(self, todoList):
      self.todoList = todoList

    def afficherListeDeTaches(self):
        i = 1
        for tache in self.todoList.recupererToutesLesTaches():
            print(i, tache.toString())
            i += 1

    def choixMenu(self):
        print("""
        1) Ajouter une tâche
        2) Terminer une tâche
        3) Afficher toutes les tâches
        4) Afficher les tâches à faire
        5) Afficher les tâches faites
        """)
        choix = 0
        while not (choix >= 1 and choix <= 5):
            try:
                choix = int(input("> Entrez votre choix:"))
            except ValueError:
                print("Votre entrée n'est pas correcte")

        return choix

    def traiterChoix(self, choix):
        """ Traite un choix, considéré valide """
        if choix == 1:
            # Ajouter une tache
            nom = input("Entrez le nom de la tâche: ")
            self.todoList.ajouterTache(nom)

        elif choix == 2:
            # Terminer une tache

            # Deux types d'erreurs :
            # - ValueError : si l'entrée n'est pas un chiffre
            # - IndexError : si l'index donnée est plus grand que le nombre de tâches
            invalide = True
            while invalide:
                try:
                    numTache = int(input("Quelle tâche terminer ? "))  # ValueError
                    self.todoList.recupererTache(numTache-1).finir()  # IndexError

                    # La ligne ci dessus est équivalent à :
                    # tache = self.todoList.recupererTache(numTache)
                    # tache.finir()

                    # Une fois arrivé ici, pas d'erreur, la tâche a été terminée. On peut sortir de la boucle
                    invalide = False
                except ValueError:
                    print("Votre entrée n'est pas un chiffre")
                    # Si on arrive ici, le 'invalide = False' n'a pas été exécuté
                    # => invalide est toujours égal à True
                except IndexError:
                    print("Aucune tâche n'existe avec cet index")
                    # Si on arrive ici, le 'invalide = False' n'a pas été exécuté
                    # => invalide est toujours égal à True

            # Fin de la boucle

        elif choix == 3:
            # Afficher toutes les taches

            # Boucler sur toutes les tâches de la list
            for tache in self.todoList.recupererToutesLesTaches():
                print(tache.toString())

        elif choix == 4:
            # Afficher les taches à faire
            for tache in self.todoList.recupererTachesAFaire():
                print(tache.toString())

        elif choix == 5:
            # Afficher les taches à faire
            for tache in self.todoList.recupererTachesFaites():
                print(tache.toString())
