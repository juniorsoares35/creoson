import creopyson
from time import sleep
import keyboard

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()

drawings = c.creo_list_files("*drw")

for drw in drawings:
    sleep(3)
    try:
        c.file_open(file_=drw, display=True)
        keyboard.send("d")
        keyboard.send("w")
        keyboard.send("g")
        print(f"\033[32m{drw} - exportado com sucesso!\033[32m")
    except:
        print(f"\033[31m{drw} - Não abriu\033[31mdwgdwg")