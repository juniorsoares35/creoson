import creopyson

# Conectar no creoson
c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()

# Checar se foi conectado corretamente
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    input("Aperte enter para sair...")
    exit()


# Obter nomes de OS (ordem de serviço) antigos e novos
os_atual = input("OS atual: ")
os_nova = input("OS nova: ")

# Listar arquivos a serem renomeados
parts = c.creo_list_files(f"{os_atual}*prt")
draws = c.creo_list_files(f"{os_atual}*drw")

print("Partes encontradas:", parts)

i = 0
for part in parts:
    i += 1
    draw = part.replace(".prt", ".drw")
    novo_nome_part = part.replace(os_atual, os_nova)
    novo_nome_draw = draw.replace(os_atual, os_nova)

    try:
        # Abrir arquivos, se necessário
        if not c.file_exists(part):
            c.file_open(file_=part, display=False)
        if not c.file_exists(draw):
            c.file_open(file_=draw, display=False)

        # Renomear e salvar arquivos
        if c.file_exists(part):
            c.file_rename(new_name=novo_nome_part,
                          file_=part, onlysession=False)
            c.file_save(file_=novo_nome_part)

        if c.file_exists(draw):
            c.file_rename(new_name=novo_nome_draw,
                          file_=draw, onlysession=False)
            c.file_save(file_=novo_nome_draw)

        print(
            f"{i} - Arquivos renomeados: {part} -> {novo_nome_part}, {draw} -> {novo_nome_draw}")

    except Exception as e:
        print(f"{i} - Erro ao renomear {part} ou {draw}: {e}")
