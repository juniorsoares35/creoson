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

if "PDF" not in c.creo_list_dirs():
    c.creo_mkdir("PDF")

for drw in drawings:
    sleep(3)
    print(drw)
    c.file_open(file_=drw, display=True)
    keyboard.send("d")
    keyboard.send("w")
    keyboard.send("g")