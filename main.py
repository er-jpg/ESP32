# Programa principal para execução no ESP32
# Requerimentos: Módulo de relé ligado no pino 2
#                Módulo DHT11 ligado ao pino 4

# Lembrete que deve existir um arquivo chamado config.py
# com as sequintes variáveis: API_KEY, WIFI_SSID, WIFI_PASSWORD
import config

import machine
import time
import dht
import network
import wifi_lib

def atpPuc():
    # Variáveis para configuração de rede
    #WIFI_SSID = ""
    #WIFI_PASSWORD = ""
    
    # Variável para a chave de API do ThingSpeak
    #API_KEY = ""
    
    # Variável de deplay de comunicação em segundos
    DELAY_TIME = 60

    # Configuração de pinos
    relePin = machine.Pin(2, machine.Pin.OUT)
    dhtPin = dht.DHT11(machine.Pin(4))

    # Inicializa a conexão WiFi
    wifi = wifi_lib.wifiConnect(config.WIFI_SSID, config.WIFI_PASSWORD)
    #print(wifi.isconnected())

    while (True):
        dhtPin.measure()
        temperatura = dhtPin.temperature()
        umidade = dhtPin.humidity()

        if(temperatura > 31 or umidade > 70):
            statusRele = 1
            relePin.value(statusRele)
        else:
            statusRele = 0
            relePin.value(statusRele)

        print("Temp = {}; Umidade = {}".format(temperatura, umidade))
        wifi_lib.sendThingSpeak(config.API_KEY, temperatura, umidade, statusRele)
        time.sleep(DELAY_TIME)
    
    return True
