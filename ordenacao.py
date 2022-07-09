from functools import cmp_to_key
from operator import is_
import dados_excel
import variaveis
from datetime import datetime

lista_escolas = variaveis.get_escolas()
ANO_ATUAL = variaveis.get_anoatual()
op = variaveis.get_op()

    
#Verifica se tem ASE [28] e trabalha na área [11,15,19,23,27]
def tem_ase_trabalha(aluno,op):
    ase = aluno[28]
    #Freguesia da Escola da opção
    if (op==1):
        trab_escola = aluno[11]   
    elif (op ==2):
        trab_escola = aluno[15]
    elif (op ==3):
        trab_escola = aluno[19]
    elif (op ==4):
        trab_escola = aluno[23]
    elif (op ==5):
        trab_escola = aluno[27]
        
    if ase != "" and trab_escola == "Sim":
        return 1
    else:
        return 0
    
        
#Verifica residencia [3] e frequentaram anteriormente uma instituicao do agrupamento [7]
def residente(aluno):
    area = aluno[3];  
    cp1 = area[:4]
    cp2 = area[5:]
    
    codigos_postais = dados_excel.dados_codigoPostal()
    for key,value in codigos_postais.items():        
            for cod in value:
                if cod[1]==cp2 and cod[0] == cp1:
                    return 1
    return 0

def reside_e_foi_aluno(aluno):
    if residente(aluno) and freq_creche_agrupamento(aluno):
        return 1
    else:
        return 0
    
    
#Pre-escolar no setor social [6]
def freq_creche(aluno):
    if aluno[6]=="Sim":
        return 1
    else:
        return 0
    
        
#Verifica trabalha na área [11,15,19,23,27]
def trabalha_area(aluno,op):
     #Freguesia da Escola da opção
    if (op==1):
        trab_escola = aluno[11]   
    elif (op ==2):
        trab_escola = aluno[15]
    elif (op ==3):
        trab_escola = aluno[19]
    elif (op ==4):
        trab_escola = aluno[23]
    elif (op ==5):
        trab_escola = aluno[27]
        
    if trab_escola == "Sim":
        return 1
    else:
        return 0
    
#idade, ordenado pelos mais velhos [2]
def idade(aluno):
    data_nascimento = aluno[2]
    date_time_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
    data_atual = datetime.today()
    
    dias = data_atual - date_time_obj
    dias = str(dias).split("days,")
    return int(dias[0])
   
    
    
#Verifica se uma dada escola pertence ao agrupamento
def freq_creche_agrupamento(aluno):
    escola = aluno[7];
    if escola in lista_escolas.keys():
        return 1
    else:
        return 0


#Pertence à freguesia da escola de opção Codigo Postal - aluno[3]
def pertence_freguesia_escola(aluno,op):
     
    area = aluno[3];  
    cp2 = area[5:]
    
    codigos_postais = dados_excel.dados_codigoPostal()
    
    #Freguesia da Escola da opção
    if (op==1):
        cod_escola = aluno[8]   
    elif (op ==2):
        cod_escola = aluno[12]
    elif (op ==3):
        cod_escola = aluno[16]
    elif (op ==4):
        cod_escola = aluno[20]
    elif (op ==5):
        cod_escola = aluno[24]
    
    #Verifica a freguesia da escola da opção   
    freg_escola = lista_escolas[cod_escola][1]
    for key,value in codigos_postais.items():
        if key == freg_escola:        
            for cod in value:
                if cod[1]==cp2:
                    return 1
   
    return 0            
    


#Verifica se tem ASE [28] e vive na área [3] (codigo postal 0000-000)
def tem_ase_vive(aluno,op):
    ase = aluno[28];
    if pertence_freguesia_escola(aluno,op) and ase!="":
        return 1
    else:
        return 0 
         
         
#Verifica se tem irmãos na escola de opção [10][14][18][22][26]
def tem_irmao(aluno,op):  
    if (op==1):
        irmao = aluno[10]
        if (irmao == "Sim"):
            return 1
        else:
            return 0
    elif (op ==2):
        irmao = aluno[14]
        if (irmao == "Sim"):
            return 1
        else:
            return 0
    elif (op ==3):
        irmao = aluno[18]
        if (irmao == "Sim"):
            return 1
        else:
            return 0
    elif (op ==4):
        irmao = aluno[22]
        if (irmao == "Sim"):
            return 1
        else:
            return 0
    elif (op ==5):
        irmao = aluno[26]
        if (irmao == "Sim"):
            return 1
        else:
            return 0
         
#Verifica se tem pais menores a estudar aluno[4]    
def pais_menores(aluno):
    if aluno[4] == 'Sim':
        return 1
    else:
        return 0

#Verifica se é nee - aluno[5]                  
def is_nee(aluno):
    nee = aluno[5]
    if nee == 'Sim':
        return 1
    else:
        return 0

def ordena_escola(lista_alunos_escola):
    my_list_ordenado = lista_alunos_escola
    
    my_list_ordenado = sorted(lista_alunos_escola, key=cmp_to_key(comparador_especial))
    
    return my_list_ordenado


def ordena_colocados(lista_colocados):
    
    for key,value in lista_colocados.items():
        #Vai ordenar cada escola
        
        if key != 'fora':
            lista_colocados[key] = ordena_escola(lista_colocados[key])
    
    return lista_colocados


           
   
def condicoes_desempate(aluno1,aluno2):
    
    #1ºcondição: NEE
    if is_nee(aluno1) and is_nee(aluno2)==0:
        return -1
    elif is_nee(aluno1)==0 and is_nee(aluno2):
        return 1
    elif is_nee(aluno1) == is_nee(aluno2): 
        #ambos iguais, passa para a 2ºcondição
        #2ºcondição: Pré-escolar
        if pais_menores(aluno1) and pais_menores(aluno2)==0:
            return -1
        elif pais_menores(aluno1)==0 and pais_menores(aluno2):
            return 1
        elif pais_menores(aluno1)==pais_menores(aluno2):
            #ambos estão empatados, tem de passar para o critério 3
            #3ºcondição: Tem irmãos na escola da opção
            if tem_irmao(aluno1,op) and tem_irmao(aluno2,op)==0:
                return -1
            elif tem_irmao(aluno1,op)==0 and tem_irmao(aluno2,op):
                return 1
            elif tem_irmao(aluno1,op) == tem_irmao(aluno2,op):
                #ambos não têm irmãos ou ambos têm irmão, passa para o próximo critério
                #4ºcondição: ASE + Residência
                if tem_ase_vive(aluno1,op) and tem_ase_vive(aluno2,op) == 0:
                    return -1
                elif tem_ase_vive(aluno1,op)==0 and tem_ase_vive(aluno2,op):
                    return 1
                elif tem_ase_vive(aluno1,op)==tem_ase_vive(aluno2,op):
                    #ambos ou não têm ASE e vivem ou ambos têm ASE e vivem, passa para o próximo
                    #5ºcondição: ASE + Profissão
                    if tem_ase_trabalha(aluno1,op) and tem_ase_trabalha(aluno2,op) ==0:
                        return -1
                    elif tem_ase_trabalha(aluno1,op)==0 and tem_ase_trabalha(aluno2,op):
                        return 1
                    elif tem_ase_trabalha(aluno1,op)==tem_ase_trabalha(aluno2,op):
                        #ambos estão iguais, passa para a póxima
                        #6ºcondição: Residência e freq o agrupamento
                        if reside_e_foi_aluno(aluno1) and reside_e_foi_aluno(aluno2)==0:
                            return -1 
                        elif reside_e_foi_aluno(aluno1)==0 and reside_e_foi_aluno(aluno2):
                            return 1
                        elif reside_e_foi_aluno(aluno1)==reside_e_foi_aluno(aluno2):
                            #ambos estão iguais
                            #7ºcondicao: Idade
                            if idade(aluno1)>idade(aluno2):
                                return -1 
                            elif idade(aluno1)<idade(aluno2):
                                return 1    
                            else:
                                 #ambos estão iguais
                                 #8ºcondição: Profissão na área
                                if trabalha_area(aluno1,op) and trabalha_area(aluno2,op)==0:
                                    return -1 
                                elif trabalha_area(aluno1,op)==0 and trabalha_area(aluno2,op):
                                    return 1    
                                elif trabalha_area(aluno1,op)==trabalha_area(aluno2,op):
                                    return -1

def idade_5(aluno):
    
    data_nascimento = aluno[2]
    date_time_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
    ano = date_time_obj.year
    mes = date_time_obj.month
    dia = date_time_obj.day
    
    idade = ANO_ATUAL - ano
    
    if idade >=5:
        return 1
    else:
        return 0

        
def idade_4(aluno):
    
    data_nascimento = aluno[2]
    date_time_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
    ano = date_time_obj.year
    mes = date_time_obj.month
    dia = date_time_obj.day
    
    idade = ANO_ATUAL - ano
    
    if idade >=4:
        return 1
    else:
        return 0


def idade_3(aluno):
    data_nascimento = aluno[2]
    date_time_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
    ano = date_time_obj.year
    mes = date_time_obj.month
    dia = date_time_obj.day
    
    idade = ANO_ATUAL - ano
    
    if idade == 3 and mes < 9 :
        return 1
    elif idade == 3 and mes == 9 and dia <= 15:
        return 1
    else:
        return 0

def idade_2(aluno):
    data_nascimento = aluno[2]
    date_time_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
    ano = date_time_obj.year
    mes = date_time_obj.month
    dia = date_time_obj.day
    
    idade = ANO_ATUAL - ano
    
    if idade == 3 and mes > 9 :
        return 1
    elif idade == 3 and mes == 9 and dia > 15:
        return 1
    else:
        return 0
       
def comparador_especial(aluno1,aluno2):
    # Com comparadores "customizados" existem as seguintes regras:
    # Dados 'a' e 'b' a comparar retornar:
    # -1 se 'a' deve ficar antes de 'b'
    #  1  se 'a' deve ficar depois de 'b'
    #  0 se ambos são iguais
    print(".")
    op = variaveis.get_op()
    
    #1ºcondição:Frequenta no ano anterior
    #if freq_creche(aluno1) and freq_creche(aluno2)==0:
    #    return -1 
    #elif freq_creche(aluno1)==0 and freq_creche(aluno2):
    #    return 1
    #elif freq_creche(aluno1) and freq_creche(aluno2):
        #são ambos da mesma idade
        #aplica critérios de desempate
    #    return condicoes_desempate(aluno1,aluno2)
    #elif freq_creche(aluno1)==0 and freq_creche(aluno2)==0:      
        #ambos estão iguais
        #2ºcondição: Idade 1º 5/4 anos até 31 dez
        
    if idade_5(aluno1) and idade_5(aluno2)==0:
        return -1
    elif idade_5(aluno1)==0 and idade_5(aluno2):
        return 1
    elif idade_5(aluno1) and idade_5(aluno2):
            #são ambos da mesma idade
            #aplica critérios de desempate
        return condicoes_desempate(aluno1,aluno2)        
    elif idade_5(aluno1)==0 and idade_5(aluno2)==0:
        if idade_4(aluno1) and idade_4(aluno2)==0:
             return -1
        elif idade_4(aluno1)==0 and idade_4(aluno2):
            return 1
        elif idade_4(aluno1) and idade_4(aluno2):
            #são ambos da mesma idade
            #aplica critérios de desempate
            return condicoes_desempate(aluno1,aluno2)           
        elif idade_4(aluno1)==0 and idade_4(aluno2)==0:
            #ambos estão iguais e não têm 5 ou 4 anos
            #2ºcondição: Idade 3 anos até 15 set
            if idade_3(aluno1) and idade_3(aluno2)==0:
                return -1
            elif idade_3(aluno1)==0 and idade_3(aluno2):
                return 1
            elif idade_3(aluno1) and idade_3(aluno2):
                #são ambos da mesma idade
                #aplica critérios de desempate
                return condicoes_desempate(aluno1,aluno2)  
            elif idade_3(aluno1)==0 and idade_3(aluno2)==0:
                #ambos estão iguais e não têm idade
                #3ºcondição: Idade 3 anos até 16 set a 31 dez
                if idade_2(aluno1) and idade_2(aluno2)==0:
                    return -1
                elif idade_2(aluno1)==0 and idade_2(aluno2):
                    return 1
                elif idade_2(aluno1) and idade_2(aluno2):
                    #são ambos da mesma idade
                    #aplica critérios de desempate
                    return condicoes_desempate(aluno1,aluno2) 
            
            
            
            
     
  
    


  