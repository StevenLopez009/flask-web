from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/entrada")
def entrada():
    return render_template("entrada.html")

if __name__ == "__main__":
    app.run(debug=True)
