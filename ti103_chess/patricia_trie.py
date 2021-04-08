"""
Ce module represente un arbre de Patricia Merkle

L'arbre de Patricia Merkle enregistre a chaque noeud un mouvement d'une partie du jeu d'echec. Cet arbre en outre
retourne une signature (le hash, un hachage) de son contenu. La signature est publique, et le contenu peut etre garde
secret.
"""

class PatriciaMerkleTrie:
    """
    Un arbre de Patricia Merkle.

    L'arbre enregistre une suite de mouvements tout en restant compact pour une efficacite de lecture ulterieure.
    L'arbre peut aussi retourner sa valeur de hachage.
    """
    __slots__ = ['mouvement', 'children']   # Reduit la consommation memoire de chaque mot

    def __init__(self, mouvement):
        self.mouvement = mouvement
        self.children = []

    def __contains__(self, item):
        """
        Verifie qu'un mouvement se trouve bien parmi la liste directe des mouvements suivants enregistres dans l'arbre.
        """
        for c in self.children:
            if c.mouvement == item:
                return True

        return False

    def __eq__(self, other):
        """
        Verifie que le mouvement propose correspond bien a celui enregistre dans ce noeud particulier.
        """
        return other == self.mouvement

    def __len__(self):
        """
        Retourne le nombre de mouvements suivant directement enregistres apres ce noeud.
        """
        return len(self.children)

    def __str__(self):
        """
        Retourne le mouvement correspondant a ce noeud.
        """
        return self.mouvement

    def is_leaf(self):
        """
        Ce noeud dans l'arbre est-il terminal ?
        """
        if len(self.children) == 0:
            return True

        else:
            return False

    def add(self, mouvement):
        """
        On enregistre un nouveau mouvement dans la structure actuelle
        """
        # Condition ou le mouvement existe deja. Par exemple une partie du passe possedait la meme ouverture.
        # Dans ce cas, on ne cree pas de nouveau noeud, simplement on retourne celui existant.
        for child in self.children:
            if child.mouvement == mouvement:
                return child

        # Condition ou le mouvement n'existe pas, l'arbre considere le mouvement comme inedit, ou original
        obj = PatriciaMerkleTrie(mouvement)  # On cree un nouveau mouvement
        self.children.append(obj)            # On l'ajoute aux enfants du mouvement en cours
        return obj                           # On le retourne pour etre utilise comme mouvement courant

    def get(self, mouvement):
        """
        Retourne le noeud correspondant a un mouvement particulier s'il existe dans la base de donnees.
        """
        # Condition ou le mouvement existe deja, donc on le retourne
        for child in self.children:
            if child.mouvement == mouvement:
                return child

        # Il n'y a pas de sous entree dans notre base. Donc bah rien a retourner.
        return None

    def dump(self, r=''):
        """
        Affiche le contenu de la base de donnees.

        Chaque ligne doit correspondre a une partie jouee dans le passe
        """
        if self.is_leaf():
            print(r + self.mouvement)

        else:
            for child in self.children:
                child.dump(r + self.mouvement)

    def hash(self):
        """
        Retourne la signature de ce noeud.

        La signature correspond au hachage du mouvement plus le hachage de tous les noeuds enfants si ce noeud n'est
        pas terminal.
        """
        if self.is_leaf():
            return hash(self.mouvement)

        else:
            h = hash(self.mouvement)
            for c in self.children:
                h += c.hash()
            return hash(h)


if __name__ == "__main__":
    racine = PatriciaMerkleTrie('')
    enfant = racine.add('e4')
    print(f"'{racine}'")
    racine.dump()

    enfant.add('e7')
    racine.dump()
