import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()


drawings = c.creo_list_files("*drw")
print(drawings[43:-1])

if "PDF" not in c.creo_list_dirs():
    c.creo_mkdir("PDF")

OS = input("Digite a OS do molde: ")
i=0
for drw in drawings[0:-1]:
    i+=1
    if OS in drw:    
        if c.file_exists(file_=drw) == True:
            try:
                c.interface_export_pdf(file_=drw, dirname="PDF",use_drawing_settings=True)
                print(f"\033[32m{i} - {drw} EXPORTADO COM SUCESSO")
                #drawings.remove(drw)
            except:
                print(f"\033[31m{i} - ARQUIVO {drw} NÃO EXPORTADO")
        else:
            try:
                c.file_open(file_=drw, display=False)
                c.interface_export_pdf(file_=drw, dirname="PDF",use_drawing_settings=True)
                print(f"\033[32m{i} - {drw} EXPORTADO COM SUCESSO")
            except:
                print(f"\033[31m{i} - ARQUIVO {drw} NÃO EXPORTADO")
                continue

input("--"*11 +"\nExportação finalizada\n" + "--"*11)
    
