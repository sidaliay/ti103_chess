import flask

import blockchain as bc


app = flask.Flask("Echaines")   # flask.Flask(__name__)
b = None                        # BAD PRACTICE GUILLAUME... Ne faites pas ca seuls a la maison les amis...


@app.route('/')
def nouvelle_chaine():
    """
    Une nouvelle chaine est creee
    """
    global b
    b = bc.BlockChain()
    return "<h1>New Blockchain</h1><p>Successfully created new blockchain</p>"


@app.route('/new')
def nouveau_bloc():
    """
    On ajoute un nouveau bloc a la chaine (si necessaire).
    """
    if b is None:
        return "<h1>New Block</h1><p>Error - No blockchain available</p>"

    b.new()
    return "<h1>New Block</h1><p>Succesfully created new block</p>"


@app.route('/head')
def head():
    """
    Retourne le bloc le plus recent de la chaine.
    """
    if b is None:
        return "<h1>New Block</h1><p>Error - No blockchain available</p>"

    return f"<h1>Head</h1><p>Hash of last block: {b.head().hash()}</p>"


@app.route('/add/<mouvement>')
def add(mouvement):
    """
    On dit au serveur qu'un nouveau mouvement a ete effectue.
    """
    global b
    if b is None:
        b = bc.BlockChain()

    b.head().transactions.add("e4")
    return f"<h1>Ajout d'un mouvement</h1><p>Succesfully added new move {mouvement}</p>"


if __name__ == "__main__":
    app.run("0.0.0.0", 8000)
