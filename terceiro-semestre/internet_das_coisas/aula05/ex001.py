import os;

def limparTela():
    os.system("cls || clear");

def listaCandidatos():
    limparTela()
    print("=== Lista de Candidatos ===");
    print("1. Candidato 1");
    print("2. Candidato 2");
    print("3. Candidato 3");
    
def eleitores():
    numTotalDeEleitores = int(input("Digite a quantidade total de eleitores: "));
    
    for i in range(numTotalDeEleitores):
        listaCandidatos();
        voto = int(input(f"Voto do {i + 1}º eleitor: "));
        definirVotos(voto)
        
    mostrarNumeroDeVotos()

def definirVotos(voto):
    canditado1 = 0;
    canditado2 = 0;
    canditado3 = 0;
    
    if(voto == 1):
        canditado1 += 1;
    elif(voto == 2):
        canditado2 += 1;
    else:
        canditado3 += 1;
    
    return [canditado1, canditado2, canditado3];

def mostrarNumeroDeVotos():
    candidatos = definirVotos()
    
    print(f"O candidato 1 possui {canditado1} votos");
    print(f"O candidato 2 possui {canditado2} votos");
    print(f"O candidato 3 possui {canditado3} votos");
    
eleitores()