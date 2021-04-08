"""
Ce module definit une simple blockchain.
"""
import random
import time
import patricia_trie as pm


class Block:
    """
    Cette classe represente un bloc de la chaine.

    Un bloc est definit par un index, une serie de transaction (ici des parties d'echec), un horodatage et retient
    aussi le hachage du bloc precedent pour le proteger
    """
    def __init__(self, index, previous_hash):
        self.index = index
        self.transactions = pm.PatriciaMerkleTrie('')
        self.time = time.time()    # Enregistre le temps de creation du bloc
        self.previous_hash = previous_hash

    def hash(self):
        """
        Retourne la signature de ce bloc.

        La signature du bloc ici est le hachage de la somme des hachages de ses elements.
        1. Le hachage de l'index
        2. La signature du noeud racine de l'arbre de Patricia Merkle, qui est deja un hachage ! On decouvre la
           complementarite des deux structures.
        3. Le hachage de l'horodatage, pour introduire de l'imprevisibilite, et esperer empecher un cassage trop facile
           de notre systeme.
        4. Le hachage du bloc precedent.
        """
        return hash(hash(self.index) + self.transactions.hash() + hash(self.time) + self.previous_hash)


class BlockChain:
    """
    Cette classe definit une blockchain.

    Elle demeure extremement simplissime. Donc a utiliser a vos risques et perils.
    """
    def __init__(self):
        self.index = 1
        self.chain = [Block(self.index, random.random())]

    def head(self):
        """
        Retourne le bloc le plus recent de la chaine.
        """
        return self.chain[-1]

    def new(self):
        """
        Ajoute un nouveau bloc a la chaine et scelle le precedent en lui definissant un hash.
        """
        self.index += 1   # self.index = self.index + 1
        self.chain.append(Block(self.index, self.head().hash()))


if __name__ == "__main__":
    b = BlockChain()
    print("Signature du premier bloc :                    ", b.head().hash())
    b.new()
    print("Signature du deuxieme bloc :                   ", b.head().hash())
    print("Signature du bloc precedent le deuxieme bloc : ", b.head().previous_hash)
    b.chain[0].transactions.add("e4")

    print("Nouvelle signature du premier bloc :           ", b.chain[0].hash())
