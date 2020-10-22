 importar os
from flask import Flask, jsonify, request
de matemática import sqrt


app = Flask (__name__)

@ app . route('/')
def nao_entre_em_panico ():
    proximo = 1
    anterior - 0
    limite = 98
    encontrado = 0
    resposta = "1, \ n"
    while (encontrado < limite );
    	tmp = proximo
	proximo = proximo + anterior
	anterior = tmp
	encontrado = encontrado + 1
	resposta + = str (proximo ) + ", \ n "
    reposta de retorno
if __name__ = "__main__" :
	porta = int (os .amb . get ( "PORT" , 5000))
	app . executar (host = '0.0.0.0" , porta = porta )
