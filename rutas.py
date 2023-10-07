from flask import render_template, Blueprint

educacion = Blueprint("educacion", __name__)

@educacion.route("/educacion")
def educacion():
    return render_template("educacion.html")

habilidades = Blueprint("habilidades", __name__)

@habilidades.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

experiencia = Blueprint("experiencia", __name__)

@experiencia.route("/experiencia")
def experiencia():
    return render_template("experiencia.html")

intereses = Blueprint("intereses", __name__)

@intereses.route("/intereses")
def intereses():
    return render_template("intereses.html")
