import speech_recognition as sr
import serial
from flask import Flask, render_template

# Configuração da porta serial e Flask
ser = serial.Serial('/dev/ttyACM0', 9600)  # Substitua pela porta correta
app = Flask(__name__)

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # ... (código similar ao fornecido anteriormente)

# Rota para o dashboard
@app.route('/')
def index():
    # Lógica para obter o valor do brilho atual (opcional)
    return render_template('index.html', brilho=valor_brilho)

# Loop principal
while True:
    frase = ouvir_microfone()

    if "ligar a luz" in frase:
        ser.write('L'.encode())
    elif "desligar a luz" in frase:
        ser.write('D'.encode())
    elif "aumentar o brilho" in frase:
        ser.write('B'.encode())
    elif "diminuir o brilho" in frase:
        ser.write('B'.encode())

    # Atualizar o dashboard a cada iteração (opcional)

if __name__ == '__main__':
    app.run(debug=True)
