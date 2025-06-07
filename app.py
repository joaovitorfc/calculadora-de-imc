from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = 'Abaixo do peso'
        elif imc < 25:
            classificacao = 'Peso normal'
        elif imc < 30:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obesidade'

        resultado = {
            'imc': round(imc, 2),
            'classificacao': classificacao
        }

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

