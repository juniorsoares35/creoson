import creopyson
import glob

# Conectar ao Creo
c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()

base_dir = r"c:\users\pichau\desktop\projeto_teste"
arquivos = glob.glob(f"{base_dir}\\*.*")

print("Arquivos encontrados:", arquivos)