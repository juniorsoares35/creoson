import creopyson

# inicia o servidor creoson
c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()

# Detecta se o creo esta aberto , caso contrario fecha o servidor
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()

# Lê todos os arquivos .prt do projeto
parts = c.creo_list_files("*prt")
menu = "-"*20




for part in parts:
    coord = creopyson.geometry.bound_box(c, file_=part)
    print(f"{menu}\n{part}")
    print(f"{coord}\n{menu}")
#    print(menu+"\n"+part+"\n")
 #   lista = creopyson.dimension.list_detail(c, file_=part, dim_type=None)
 #   for l in range(0, 3):
 #       if lista[l]['dim_type'] == 'diameter':
 #           print("Diametro")
 #           break
#