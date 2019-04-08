"""
@ GREGÓRIO HONORATO
PROGRAMA DESENVOLVIDO PARA DEXTRA 05/04/2017
"""
try: from flask import Flask, render_template, request
except: print("INSTALE O PACOTE Flask")

app = Flask(__name__)

#A seguir, apresentamos a lista de ingredientes disponíveis:
igredientes = {"Alface":0.4, "Bacon":2, "Hamburger de Carne":3, "Ovo":0.8,
               "Queijo":1.50}

"""
O valor de cada opção do cardápio é dado pela soma dos ingredientes que compõe o lanche.
Além destas opções, o cliente pode personalizar seu lanche e escolher os ingredientes que desejar.
Nesse caso, o preço do lanche também será calculado pela soma dos ingredientes.
"""

cardapio = {"X-Bacon": igredientes["Bacon"] + igredientes["Hamburger de Carne"] + igredientes["Ovo"],
            "X-Burge": igredientes["Hamburger de Carne"] + igredientes["Queijo"],
            "X-Egg": igredientes["Ovo"] + igredientes["Hamburger de Carne"] + igredientes["Queijo"],
            "X-Egg Bacon": igredientes["Ovo"] + igredientes["Bacon"] + igredientes["Queijo"]}

#CHAMA A PASTA TEMPLATES COM O INDEX.HTML
@app.route("/")
def carregar_pagina():
    return render_template("index.html", cardapio=cardapio,
                                         igredientes=igredientes), 200

app.run(use_reloader=True, host='0.0.0.0')
