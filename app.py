from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/educacion")
def educacion():
    return render_template("educacion.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

@app.route("/experiencia")
def experiencia():
    return render_template("experiencia.html")

@app.route("/intereses")
def intereses():
    return render_template("intereses.html")

if __name__ == "__main__":
    app.run(debug=True)
