import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()


drawings = c.creo_list_files("*drw")


if "PDF" not in c.creo_list_dirs():
    c.creo_mkdir("PDF")


for drw in drawings:
    print(drw)
    c.file_open(file_=drw, display=False)
    c.interface_export_pdf(file_=drw, dirname="PDF")
