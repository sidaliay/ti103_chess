import ti103_chess.patricia_trie as pm


def test_pm01(capsys):
    """
    Cas de test Patricia Merkle 01

    Valider l'ajout de noeuds a l'interieur de la base.

    On commence par creer le noeud racine.
    Puis on ajoute un mouvement.
    On verifie que le mouvement est bien dans la base de donnees.
    On ajoute un autre mouvement dans le noeud racine.
    On verifie que les deux mouvements sont bien distincts (non relies) dans la base de donnees.
    """
    racine = pm.PatriciaMerkleTrie('')
    racine.add('e5')
    racine.dump()
    out, _ = capsys.readouterr()  # Ce truc bizarre en fait capture ce qui est affiche a l'ecran.
    assert out == "e5\n"

    racine.add('e4')
    racine.dump()
    out, _ = capsys.readouterr()
    assert out == "e5\ne4\n"


def test_pm02(capsys):
    """
    Cas de test Patricia Merkle 02

    Valider l'ajout de noeuds a l'interieur de la base.

    On commence par creer le noeud racine.
    Puis on ajoute un mouvement.
    On verifie que le mouvement est bien dans la base de donnees.
    On ajoute un mouvement suivant.
    On verifie que les deux mouvements apparaissent bien sur la meme ligne de la base de donnees comme une partie
    distincte.
    On ajoute un autre mouvement dans le noeud racine.
    On verifie que les deux mouvements sont bien distincts (non relies) dans la base de donnees.
    """
    racine = pm.PatriciaMerkleTrie('')
    enfant = racine.add('e5')
    enfant.add('e7')
    racine.dump()
    out, _ = capsys.readouterr()
    assert out == "e5e7\n"

    racine.add('e4')
    racine.dump()
    out, _ = capsys.readouterr()
    assert out == "e5e7\ne4\n"


def test_pm03(capsys):
    """
    Cas de test Patricia Merkle 03

    Valider l'ajout de noeuds existant de la base.

    On commence par creer le noeud racine.
    Puis on ajoute un mouvement.
    On verifie que le mouvement est bien dans la base de donnees.
    On ajoute un meme mouvement a la racine.
    On verifie qu'il n'y a qu'un seul enfant a la racine
    On verifie que la liste des parties ne contient qu'une ligne.
    """
    racine = pm.PatriciaMerkleTrie('')
    enfant1 = racine.add('e5')
    racine.dump()
    out, _ = capsys.readouterr()
    assert out == "e5\n"

    enfant2 = racine.add('e5')
    assert enfant2 == enfant1

    racine.dump()
    out, _ = capsys.readouterr()
    assert out == "e5\n"
