class Linhas:#cada letra que será substituida por uma palavra é salva aqui
    def __init__(self,letra,palavra,primeiro,valor):
        self.letra = letra
        self.palavra = palavra
        self.primeiro = primeiro
        self.valor  = valor
#Função de Soma 
def Soma(vetor,letrinha):
    soma = 0 #valor da soma
    achou = False #caso seja um char registrado na classe Linhas
    for i in range(len(vetor)):#verifica todas as letras registradas
        if(vetor[i].letra==letrinha):#quando encontra a letra
            if vetor[i].valor == 0:#verifica se o valor dela ainda não foi descoberta
                achou=True #informa que o esse char foi encontrado
                for j in range(len(vetor[i].palavra)):# verifica o tamanho da palavra
                    soma+=Soma(vetor,vetor[i].palavra[j])#Descobre o valor total do char
                vetor[i].valor=soma#adiciona o valor no char
                i=len(vetor)#encerra a verificação das letras
            else:#caso o valor do char já tenha sido registrado
                achou=True  #informa que o esse char foi encontrado 
                soma=vetor[i].valor #adiciona seu valor na soma
    if (achou==False and letrinha!= '\n'):#caso a letra não estaja registrada, será adicionada a soma
        soma=1
    return soma
#Função para analizar o caso
def Caso(caso):
    
    #Guarda as letras e as palavras em um vetor
    with open(caso,'r')as arquivo:#abre o respectivo arquivo
        vetor = []#vetor que será o vetor para a classe linhas
        for line in arquivo:#para cada linha do arquivo
            if (line[2]) != '\n':#quando a linha tiver a palavra de substituição
                vetor.append((Linhas(line[0],line[2:], True,0)))#registra a linha no vetor
                
    #Demarca qual é o inicial
    for i in range(len(vetor)):#vetor das palavras
        for x in range(len(vetor)):#vetor das letras
            for j in range(len(vetor[i].palavra)):#vetor dos chars da palavra
                if vetor[x].letra==(vetor[i].palavra[j]):#caso essa letra for encontrada
                    vetor[x].primeiro=False#é registrada como não sendo a primária
                    
    #Encontra o primeiro char da linha inicial
    soma = 0#valor da soma dos chars finais
    happen = False #Para casos que não tenham palavras iniciais (todas as frases se chamam)
    for i in range(len(vetor)):#passa por todas as letras
        if vetor[i].primeiro==True:#encontra a respectiva primeira linha que tem que ser lida
            for j in range(len(vetor[i].palavra)):#passa por todos os chars da palavra
                soma+=Soma(vetor,vetor[i].palavra[j])#salvando o valor de cada char na soma total
                happen = True
                
    if happen == False: #Não tem palavra inicial (todas as frases se chamam)
        for j in range(len(vetor[0].palavra)):#passa por todos os chars da palavra primeira palavras
                soma+=Soma(vetor,vetor[0].palavra[j])#salvando o valor de cada char na soma total
                
    print(" ",caso," tem o valor de:",soma)#resposta final
#main
caso ='';
for i in range(10):
    match i:
        case 0:
            caso='caso01'
        case 1:
            caso='caso02'
        case 2:
            caso='caso03'
        case 3:
            caso='caso04'
        case 4:
            caso='caso05'
        case 5:
            caso='caso06'
        case 6:
            caso='caso07'
        case 7:
            caso='caso08'         
        case 8:
            caso='caso09'
        case 9:
            caso='caso10'
    Caso(caso)    