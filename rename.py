import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    input("Aperte enter para sair...")
    exit()



os_atual = input("OS atual: ")
os_nova = input("OS nova: ")
parts = c.creo_list_files(f"{os_atual}*prt")
draws = c.creo_list_files(f"{os_atual}*drw")
print(parts)
for part in parts:
    draw = part.replace(".prt",".drw")
    novo_nome = part.replace(os_atual,os_nova)
    novo_nome = novo_nome.replace(".prt","")
    if c.file_exists(part) == False:
        try: 
            c.file_open(file_=part, display=False)
            c.file_open(file_=draw, display=False)
            c.file_rename(new_name = novo_nome, file_=part,onlysession=True )
            c.file_save(file_=part)
            c.file_rename(new_name = novo_nome, file_=draw,onlysession=True )
            c.file_save(file_=draw)
        except:
            continue
    else:
        print(novo_nome)
        c.file_rename(new_name = novo_nome, file_=part,onlysession=True )
        c.file_save(file_=part)
        c.file_rename(new_name = novo_nome, file_=draw,onlysession=True )
        c.file_save(file_=draw)