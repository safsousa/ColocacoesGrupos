
ANO_ATUAL = 2022

lista_escolas = {
        "247560":("Escola Básica de Freixieiro","OLIVEIRA DO DOURO",1,23), #Não altera
        "273946":("Escola Básica de Sardão", "OLIVEIRA DO DOURO",1,36), #Reduz de 24 para 20, de 16 a 12
        "284646":("Escola Básica de Vilar", "VILAR DE ANDORINHO", 1,10), #Não Reduz, é mantido a capacidade da sala 22
        "297148":("Escola Básica Dr. Fernando Guedes","AVINTES",2,50), #Reduz turma 
        "237279":("Escola Básica de Cabanões", "AVINTES",1,23), #Não altera
        "201844":("Escola Básica de Aldeia Nova", "AVINTES",1,33), #Não altera, já tinha um aluno que reduz
        "231514":("Escola Básica de Mariz","VILAR DE ANDORINHO",1,21), #Não altera
        "fora": ("Fora do agrupamento")
}

lista_colocados = {
        "247560":(""),
        "273946":(""),
        "284646":(""),
        "297148":(""),
        "237279":(""),
        "201844":(""),
        "231514":(""),
        "fora":("")
}

op = 1

def get_anoatual():
    return ANO_ATUAL

def get_nturmas(key):
    return lista_escolas[key][2]
    
def get_listaColocados():
    return lista_colocados

def get_op():
    return op

def get_escolas():
    
    return lista_escolas

def put_escolas(nova_lista):
    global lista_escolas
    lista_escolas = nova_lista
    for key,value in lista_escolas.items():
        print("A escola "+key+" - "+value[0]+" tem "+str(value[3])+ " vagas")
