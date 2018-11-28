import config
import telepot
import time
from telepot.loop import MessageLoop
from calc import *

bot = telepot.Bot(config.TOKEN)


def handle(msg):
    chat_id = msg['chat']['id']
    mensaje = msg['text']
    notas = []
    list = mensaje.split(' ')
    for i in list:
        notas.append(int(i))
    tu_promedio = "Tu promedio es " + str(promedio(notas)) + "."
    nota_examen = "Necesitas un " + str(examen(notas)) + " en el examen"
    segundo_examen = "Y un " + str(examen_segunda(notas)) + " en el examen de segunda."
    print(nota_examen)
    bot.sendMessage(chat_id,
                    tu_promedio + " \n " + nota_examen + " \n "
                    + segundo_examen)


MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)
