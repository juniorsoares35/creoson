import creopyson

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

# remove din_912 da busca
for part in parts:
    if "912" in part:
        part.remove(part)
    if c.file_exists(part) == False:
        c.file_open(file_=part, display=False)
        print(f"abriu {part}")
    else:
        print(part)

    coord = creopyson.geometry.bound_box(c, file_=part)

    x = coord["xmax"], abs(coord["xmin"])
    x = x[0] + x[1]
    print(x)

    y = coord["ymax"], abs(coord["ymin"])
    y = y[0] + y[1]
    print(y)

    z = coord["zmax"], abs(coord["zmin"])
    z = z[0] + z[1]
    print(z)

    relation = 'X = "{}"\nY="{}"\nZ="{}"'.format(x, y, z)

    # Altera as relations da peca com a variavel relation
    c.file_relations_set(file_=part, relations=relation)
