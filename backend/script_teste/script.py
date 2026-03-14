import requests
import time

API_URL = "http://localhost:3000/api/sensor"

def simular(vaga, placa, evento):
    data = {
        "vaga_id": vaga,
        "placa": placa,
        "evento": evento,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    requests.post(API_URL, json=data)
    print(f" Enviado: {evento} | Vaga: {vaga} | Placa: {placa}")

# Teste manual rápido:
simular("V-101", "BRA2E19", "ARRIVAL")