import creopyson

c = creopyson.Client()
c.connect()
id = c.sessionId
creo_open = c.is_creo_running()
if creo_open == False:
    input(print("creo nao foi aberto corretamente"))
    exit()

pos = input("Posição da peça: ")
part_pos = "PART_POS = '{}'".format(pos)

dd = input("Desenhista: ")
draw_designer = "DRAW_DESIGNER = '{}'".format(dd)

td = input("Projetista: ")
tool_designer = "TOOL_DESIGNER = '{}'".format(td)

relations = ["{},{},{}"].format(part_pos, draw_designer, tool_designer)

parts = c.creo_list_files("*prt")


for part in parts:
    if c.file_exists(part) == False:
        c.file_open(file_=part, display=False)
    else:
        print(part)
    c.file_relations_set(file_=part, relations=relations)
    # c.file_regenerate(part)
