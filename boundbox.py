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
# remove din_912 da busca
for part in parts:
    if "912" in part:
        parts.remove(part)

    # abre a peca caso nao esteja na memória
    if c.file_exists(part) == False:
        c.file_open(file_=part, display=False)
        print(f"abriu {part}")
    else:
        print(f"{menu}\n{part}:\n")

    # pega coordenadas X,Y,Z da peca
    coord = creopyson.geometry.bound_box(c, file_=part)

    x = coord["xmax"], abs(coord["xmin"])
    x = x[0] + x[1]
   #print(f"X = {x}")

    y = coord["ymax"], abs(coord["ymin"])
    y = y[0] + y[1]
    #print(f"Y = {y}")

    z = coord["zmax"], abs(coord["zmin"])
    z = z[0] + z[1]
    #print(f"Z = {z}\n")

    # le as antigas relations e concatena com a nova relation
    lista = creopyson.dimension.list_detail(c, file_=part, dim_type=None)
    d = 0
    for l in range(0, 3):
        try:
            if lista[l]['dim_type'] == 'diameter':
                d = 1
                break
        except:
            break           
    if d == 0:        
        try:
            old_rel = c.file_relations_get(file_=part)
            new_relation = [f'x = "{x}"',
                            f'y = "{y}"',
                            f'z = "{z}"']+old_rel
            print(f" X = {x}\n",
                  f"Y = {y}\n",
                  f"Z = {z}\n")
        except:
            new_relation = [f'x = "{x}"',
                            f'y = "{y}"',
                            f'z = "{z}"']
            print(f" X = {x}\n",
                  f"Y = {y}\n",
                  f"Z = {z}\n")
    else:
        try:
            old_rel = c.file_relations_get(file_=part)
            new_relation = [f'x = "{x}"',
                            f'z = "{z}"']+old_rel
            print(f" X = ø{x}\n",
                  f"Z = {z}\n")
        except:
            new_relation = [f'x = "{x}"',
                            f'z = "{z}"']
            print(f" X = ø{x}\n",
                  f"Z = {z}\n")
        
    # Altera as relations da peca com a variavel new_relation
    c.file_relations_set(file_=part, relations=new_relation)
    c.file_refresh(file_=part)
