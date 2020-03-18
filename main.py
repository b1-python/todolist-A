# Méthode d'import 1 : importer tout le module => le contenu du module est disponible dans la variable 'taches'
import taches
# Méthode d'import 2 : importer uniquement une classe du module => la classe est alors disponible dans le scope global
from afficheurtaches import Afficheur

todoList = taches.TODOList("La liste du jour")
afficheur = Afficheur(todoList)
while True:
    print("------------------")
    afficheur.afficherListeDeTaches()
    choix = afficheur.choixMenu()
    afficheur.traiterChoix(choix)

