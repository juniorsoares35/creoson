import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()

massa = c.file_massprops()

print(massa['mass'])

c.file_relations_set(relations='massa = {}'.format(massa))
