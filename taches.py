"""
Module taches
Contient deux classes relatives à la gestion de todolist
"""

class Tache:
    """ Classe Tache. Représente une tâche qui peut être faite ou pas """

    def __init__(self,nomDeLaTache):
        """ Constructeur de Tache avec un nom donné et l'état à non fait """
        self.nom = nomDeLaTache
        self.etat = False

    def finir(self):
        """ Marque la tâche comme faite """
        self.etat = True

    def toString(self):
        """ Renvoie la tâche sous forme de chaine de caractères """
        if self.etat:
            return "[X] " + self.nom
        else:
            return "[ ] " + self.nom

    def estFaite(self):
        """ Renvoie True si la tâche est faite False sinon """
        return self.etat


class TODOList:
    """ Représente une liste de tache. """
    def __init__(self, nomDeLaListe):
        self.nom = nomDeLaListe
        self.listeDeTaches = []

    def ajouterTache(self,nomTache):
        """ Ajoute une nouvelle tâche qui a le nom passé en paramètre à la liste """
        tache = Tache(nomTache)
        self.listeDeTaches.append(tache)

    def recupererToutesLesTaches(self):
        return self.listeDeTaches

    def recupererTachesAFaire(self):
        listeTacheAFaire = []
        # Boucle sur toutes les taches et ajoute dans la liste celles qui sont faites
        for tache in self.listeDeTaches:
            if not tache.estFaite(): listeTacheAFaire.append(tache)
        return listeTacheAFaire

    def recupererTachesFaites(self):
        listeTacheFaites = []
        # Boucle sur toutes les taches et ajoute dans la liste celles qui sont faites
        for tache in self.listeDeTaches:
            if tache.estFaite(): listeTacheFaites.append(tache)
        return listeTacheFaites

    def recupererTache(self, index):
        """ Renvoie la tache positionné à l'index passé, déclenche un IndexError si l'index n'est pas valide """
        if index < 0: raise ValueError()
        return self.listeDeTaches[index]
