class Exercice3:
    def __init__(self, capacite):
        # Implémenter la logique d'initialisation
        self.dico = {}
        self.capacite = capacite
        pass

    def get(self, cle):
        # Implémenter la logique de récupération
        return self.dico[cle]

    def put(self, cle, valeur):
        # Implémenter la logique d'insertion
        self.dico[cle] = valeur

    def free(self):
        # Implémenter la logique de libération
        self.dico = {}
        pass
