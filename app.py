from flask import Flask


app = Flask(__name__)

@app.get("/") #root
def pokemon_list():
    return "Bulbasaur, Charmander, Pikachu, Eevee, Diglett"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is Bulbasaur, a Gen I Pokemon who looks like a little dinosaur!"


@app.get("/charmander")
def charmander_data():
    return "This is Charmander, a Gen I Pokemon who looks like a little red newt!"


@app.get("/pikachu")
def pikachu_data():
    return "This is Pikachu, a Gen I Pokemon who looks like a little rodent!"


@app.get("/eevee")
def eevee_data():
    return "This is Eevee, a Gen I Pokemon who looks like a little fox!"


@app.get("/diglett")
def diglett_data():
    return "This is Diglett, a Gen I Pokemon who looks like a little worm-mole!"






if __name__ == "__main__":
    app.run()

