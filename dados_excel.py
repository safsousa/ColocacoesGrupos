import processamento_excel


# Dicionário cuja chave é a freguesia e o value é uma lista de tuplos da forma:
#   posição 0 - 4 digitos do Código Postal
#   posição 1 - 3 digitos do Código Postal
def dados_codigoPostal():
    cod_postal = processamento_excel.open_excel_reading_codPostal()
    
    doc_dict = {}
    has_doc = True
    i = 2
    while has_doc:
        
        if cod_postal["C"+str(i)].value:
            if  cod_postal["C"+str(i)].value in doc_dict.keys():
                doc_dict[cod_postal["C"+str(i)].value] =  doc_dict[cod_postal["C"+str(i)].value] + [(str(cod_postal["A"+str(i)].value), str(cod_postal["B"+str(i)].value))]     
            else:
                doc_dict.update({
                str(cod_postal["C"+str(i)].value):[               
                (str(cod_postal["A"+str(i)].value),
		        str(cod_postal["B"+str(i)].value))
                ]})
            i=i+1
        else:
            has_doc = False
            
   
    
    return doc_dict


# Dicionário cuja chave é o número de processo de matricula e o value é um tuplo da forma:
    # 1 - alunos["AA"] - Nome do aluno
    # 2 - alunos["AE"] - Data Nascimento
    # 3 - alunos["AG"] - Código Postal do Aluno
    # 4 - alunos["AM"] - Pais Menores Estudantes
    # 5 - alunos["AO"] - PEI
    # 6 - alunos["AW"] - Freq Creche (Sim/Não)
    # 7 - alunos["BC"] - Misi Escola Anterior
    # 8 - alunos["BH"] - Cód Escola 1ºopção
    # 9 - alunos["BI"] - Nome Escola 1ºopção
    # 10- alunos["BO"] - Tem Irmão 1ºopção
    # 11- alunos["BQ"] - Morada de Emprego 1ºopção
    # 12- alunos["CK"] - Cód Escola 2ºopção
    # 13- alunos["CL"] - Nome Escola 2ºopção
    # 14- alunos["CR"] - Tem Irmão 2ºopção
    # 15- alunos["CT"] - Morada de Emprego 2ºopção
    # 16- alunos["DN"] - Cód Escola 3ºopção
    # 17- alunos["DO"] - Nome Escola 3ºopção
    # 18- alunos["DU"] - Tem Irmão 3ºopção
    # 19- alunos["DW"] - Morada de Emprego 3ºopção
    # 20- alunos["EQ"] - Cód Escola 4ºopção
    # 21- alunos["ER"] - Nome Escola 4ºopção
    # 22- alunos["EX"] - Tem Irmão 4ºopção
    # 23- alunos["EZ"] - Morada de Emprego 4ºopção
    # 24- alunos["FT"] - Cód Escola 5ºopção
    # 25- alunos["FU"] - Nome Escola 5ºopção
    # 26- alunos["GA"] - Tem Irmão 5ºopção
    # 27- alunos["GC"] - Morada de Emprego 5ºopção
    # 28- alunos["AJ"] - Escalão
    # 29- alunos["GV"] - Reduz Turma
def dados_alunos():
    alunos = processamento_excel.open_excel_reading_matriculas()
    doc_dict = {}
    has_doc = True
    i = 2
    while has_doc:
        if alunos["B"+str(i)].value:
            doc_dict.update({
                str(alunos["B"+str(i)].value):(               
                str(alunos["AA"+str(i)].value),
		        str(alunos["AE"+str(i)].value),
                str(alunos["AG"+str(i)].value),
                str(alunos["AM"+str(i)].value),
                str(alunos["AO"+str(i)].value),
                str(alunos["AW"+str(i)].value),
                str(alunos["BC"+str(i)].value),
                str(alunos["BH"+str(i)].value),
                str(alunos["BI"+str(i)].value),
                str(alunos["BO"+str(i)].value),
                str(alunos["BQ"+str(i)].value),
                str(alunos["CK"+str(i)].value),
                str(alunos["CL"+str(i)].value),
                str(alunos["CR"+str(i)].value),
                str(alunos["CT"+str(i)].value),
                str(alunos["DN"+str(i)].value),
                str(alunos["DO"+str(i)].value),
                str(alunos["DU"+str(i)].value),
                str(alunos["DW"+str(i)].value),
                str(alunos["EQ"+str(i)].value),
                str(alunos["ER"+str(i)].value),
                str(alunos["EX"+str(i)].value),
                str(alunos["EZ"+str(i)].value),
                str(alunos["FT"+str(i)].value),
                str(alunos["FU"+str(i)].value),
                str(alunos["GA"+str(i)].value),
                str(alunos["GC"+str(i)].value),
                str(alunos["AJ"+str(i)].value),
                str(alunos["GV"+str(i)].value)
                )})
            i=i+1
        else:
            has_doc = False
            
   
    
    return doc_dict


def dados_escolas():
    escolas = processamento_excel.open_excel_reading_escolas()
    doc_dict = {}
    
    i = 2
    while str(escolas["A"+str(i)].value) != 'None':
            
            doc_dict.update({
                str(escolas["A"+str(i)].value):(               
                str(escolas["B"+str(i)].value),
		        str(escolas["C"+str(i)].value),
                str(escolas["D"+str(i)].value),
                str(escolas["E"+str(i)].value)
                
                )})
            i=i+1
   
    return doc_dict
