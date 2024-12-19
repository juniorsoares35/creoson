import os
import creopyson

# Conectar ao Creo
c = creopyson.Client()
c.connect()

if not c.is_creo_running():
    print("Creo não foi aberto corretamente.")
    input("Aperte Enter para sair...")
    exit()

# Configurar diretório base e entradas do usuário
base_dir = r"c:\users\pichau\desktop\projeto_teste"
os_atual = input("OS atual: ")
os_nova = input("OS nova: ")

# Listar arquivos no diretório
arquivos = os.listdir(base_dir)

# Filtrar arquivos que começam com `os_atual` e possuem as extensões específicas
parts = [f for f in arquivos if f.startswith(os_atual) and f.endswith(".prt")]
draws = [f for f in arquivos if f.startswith(os_atual) and f.endswith(".drw")]

if not parts and not draws:
    print(f"Nenhum arquivo encontrado com a OS '{os_atual}'.")
    exit()

print("Parts encontrados:", parts)
print("Draws encontrados:", draws)

# Renomear os arquivos
for part in parts:
    novo_nome_part = part.replace(os_atual, os_nova, 1)  # Substitui apenas a primeira ocorrência
    draw = part.replace(".prt", ".drw")  # Nome do desenho correspondente
    novo_nome_draw = draw.replace(os_atual, os_nova, 1)  # Substitui apenas a primeira ocorrência

    try:
        # Renomear e salvar a parte
        c.file_open(file_=os.path.join(base_dir, part), display=False)
        c.file_rename(new_name=novo_nome_part, file_=part, onlysession=False)
        c.file_save(file_=novo_nome_part)

        # Renomear e salvar o desenho correspondente (se existir)
        if draw in draws:
            c.file_open(file_=os.path.join(base_dir, draw), display=False)
            c.file_rename(new_name=novo_nome_draw, file_=draw, onlysession=False)
            c.file_save(file_=novo_nome_draw)

        print(f"Renomeado: {part} -> {novo_nome_part}")
    except Exception as e:
        print(f"Erro ao processar {part}: {e}")
