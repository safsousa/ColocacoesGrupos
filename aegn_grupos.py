
import dados_excel
import processamento_excel
import ordenacao
import variaveis
from datetime import datetime


N_ALUNOS_GRUPO_REDUZIDA = 20
N_ALUNOS_GRUPO = 25

op = variaveis.get_op()
lista_escolas = variaveis.get_escolas()
lista_colocados = variaveis.get_listaColocados()


#Imprime a lista de alunos colocados
def imprime_colocados(lista_colocados):
    for key,value in lista_colocados.items():
        print(str(lista_escolas[key][0])+ " - " +key )
        print(value)

  
    

#Verifica se há alunos que não cabem na turma    
def ha_alunos_extra(lista_colocados):
    lista_escolas = variaveis.get_escolas()
    
    lista_alunos_extra = []
    
    #Constroi a lista de alunos extra
    #Apaga os alunos que estão a amis
    for key,value in lista_colocados.items():
        if key != 'fora':  
            n_alunos = int(lista_escolas[key][3])
            y = list(value)
            lista_alunos_extra = lista_alunos_extra + y[n_alunos:]
            y = y[:n_alunos]
            lista_colocados[key] = tuple(y)
    
    
    return lista_alunos_extra

def coloca_opcao(lista_alunos_extra,op):
    for aluno in lista_alunos_extra:
        #vai buscar a 2ºopção do alunos e as sucessivas
        if op==2:
            opcao_aluno = aluno[12]
        elif op == 3:
            opcao_aluno = aluno[16]
        elif op == 4:
            opcao_aluno = aluno[20]
        elif op == 5:
            opcao_aluno = aluno[24]
        else: 
            opcao_aluno = ""
        
        if lista_colocados.get(opcao_aluno) != None:
            #o aluno quer uma escola do agrupamento
            y = list(lista_colocados[opcao_aluno])            
            y.append(aluno)
            lista_colocados[opcao_aluno] = tuple(y)
                
        else:
            # o aluno quer sair do agrupamento ou já não tem opcoes
            y = list(lista_colocados["fora"])
            y.append(aluno)
            lista_colocados["fora"] = tuple(y)
            
        
#Coloca os alunos na primeira opção
def coloca_1opcao(lista_alunos):
    
    lista_colocados = variaveis.get_listaColocados()
    
    for key,value in lista_alunos.items():
              
        if lista_colocados.get(value[7]) != None: 
            #o aluno vai ser colocado na escola que pretende
            y = list(lista_colocados[value[7]])
            matricula = (key,)
            dados_aluno = matricula + (lista_alunos.get(key))
            y.append( dados_aluno)
            lista_colocados[value[7]] = tuple(y)
        else:
            # o aluno quer sair do agrupamento
            y = list(lista_colocados["fora"])
            y.append(key)
            lista_colocados["fora"] = tuple(y)   
    
    return lista_colocados
      
#Função principal que coloca dos alunos
def coloca_alunos(lista_alunos):
    
    #Coloca todos os alunos na 1 opção
    lista_colocados = coloca_1opcao(lista_alunos) 
    #Ordena os alunos
    lista_colocados = ordenacao.ordena_colocados(lista_colocados)
    print("Ordenamos os alunos na 1ºopção")
    
    
    #Verifica se há alunos extra e coloca nas opções seguintes os alunos
    print("Verifica se há alunos que não cabem na turma")
    lista_alunos_extra = ha_alunos_extra(lista_colocados)   
    op = 2
    while (lista_alunos_extra != []):
         coloca_opcao(lista_alunos_extra,op)
         print("Coloca esses alunos na opção ",op)
         lista_colocados = ordenacao.ordena_colocados(lista_colocados)
         print("Volta a ordenar ",op)
         lista_alunos_extra = ha_alunos_extra(lista_colocados)   
         print("Verifica se há alunos que não cabem na turma")
         op = op + 1
            

    print("Vou criar a excel com os alunos distribuídos no ficheiro Distribuicao_Final.xlsx")
    processamento_excel.escreve_excel_final(lista_colocados)  


def menu():
    
    print ("Vamos iniciar a constituição dos grupos do ficheiro exportacao_portal_seriacao.xlsx")
    lista_alunos = dados_excel.dados_alunos()
    lista_escolas = dados_excel.dados_escolas()
    print ("Vamos ler os dados das escolas do ficheiro escolas.xlsx")
    variaveis.put_escolas(lista_escolas)
    print ("Vamos criar um ficheiro de excel, com os dados essenciais ListaAlunosMatriculas.xlsx ")
    nome_folha = "ListaAlunosMatriculas_Pre.xlsx"    
    processamento_excel.write_result(lista_alunos,nome_folha)
    print ("Vamos colocar os alunos e ordenar")
    
    coloca_alunos(lista_alunos)
    
   
menu()