import config
import telepot
import time
from telepot.loop import MessageLoop
from calc import *

bot = telepot.Bot(config.TOKEN)

def mensaje(notas):
    if examen(notas) < 10:
        return "¿Ah?"
    if examen_segunda(notas) <= 70:
        tu_promedio = "Tu promedio es " + str(promedio(notas)) + "."
        nota_examen = "Necesitas un " + str(examen(notas)) + " en el examen"
        segundo_examen = "Y un " + str(examen_segunda(notas)) + " en el examen de segunda."
        return tu_promedio + " \n " + nota_examen + " \n " + segundo_examen
    else:
        return "Fuiste buena persona, lo siento."

def handle(msg):
    chat_id = msg['chat']['id']
    mensaje = msg['text']
    notas = []
    list = mensaje.split(' ')
    for i in list:
        notas.append(int(i))
    bot.sendMessage(chat_id, mensaje(notas))


MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)
