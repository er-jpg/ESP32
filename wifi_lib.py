import urequests
import network
import time

# Função que realiza e retorna uma conexão de WiFi
def wifiConnect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    for tick in range(50):
        if (station.isconnected()):
            break
        time.sleep(0.1)
    return station

# Função para enviar dados ao ThingSpeak
def sendThingSpeak(API_KEY, field1, field2, field3):  
    response = urequests.get("http://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}".format(API_KEY, field1, field2, field3))
    
    if(response.text == '0'):
        print('Error sending data, trying again...')
        time.sleep(60)
        sendThingSpeak(API_KEY, field1, field2, field3)        
    
    return True