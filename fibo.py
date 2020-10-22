import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

cont=0;
numero = 2;

while (cont < 100):
	primo = False;
	for i in range (2, numero):
		if (numero%i == 0):
			primo = True;
			break;

	if (not primo):
		cont += 1;
		print(numero);

	numero += 1;


    return numero

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
