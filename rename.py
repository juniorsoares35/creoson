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
print(parts)
for part in parts:
    if c.file_exists(part) == False:
        c.file_open(file_=part, display=False)
        print(part)
        print(part.replace(os_atual,os_nova))
    else:
        novo_nome = part.replace(os_atual,os_nova)
        print(novo_nome)
        novo_nome = novo_nome.replace(".prt","")
        print(novo_nome)
        c.file_rename(new_name = novo_nome, file_=part,onlysession=True )