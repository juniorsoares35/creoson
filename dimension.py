import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()


parts = c.creo_list_files("*prt")
dim = c.dimension_list(file_="PRT0001.prt", dim_type="linear")

print(dim)
