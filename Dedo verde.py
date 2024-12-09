vegetais = []
frutas = []
flores = []
plantas = []


def trava(operacao, tipo, texto, condicoes):
    match operacao:
        case 1: 
            while True:
                try:
                    a = tipo(input(texto))
                    return a
                except Exception:
                    pass
        case 2:
            while True:
                a = input(texto)
                if a in condicoes:
                    a = tipo(a)
                    return a

def _pesquisar(operacao, lista, atributo, exibir, tipo):
    cont = 0   
    if operacao == 1:
        compara = input(f"Insira o {tipo} que deseja pesquisar: ")
    elif operacao == 2:
        compara = True
    else:
        compara = False
    for i in range(len(lista)):
        if compara == getattr(lista[i], atributo):
            getattr(lista[i], exibir)()
        else:
            cont += 1

    if compara == True or compara == False:
        mensagem = tipo
    else:
        mensagem = tipo + " " + compara           
    if cont == len(lista):
        print(f"""
    {mensagem} não cadastrado!""")

        
class _fruta():
    def __init__ (self, a):
        self.nome_fruta = input("Insira o nome da fruta: ")
        self.sabor_fruta = input(f"Insira o sabor da fruta {self.nome_fruta}: ")
        self.tamanho_fruta = str(trava(1,int, f"Insira o tamanho, em centrímetros, da fruta {self.nome_fruta}: ", 0))
        self.cor_fruta = input(f"Insira a cor da fruta {self.nome_fruta}: ")
        self.formato_fruta = input(f"Insira o formato da fruta {self.nome_fruta}: ")
        self.estacao_fruta = str(trava(2,str, f"Insira a estação em que a fruta {self.nome_fruta} fica madura: ", ["Verão", "VERÃO", "Verao" ,"verão", "v", "verao", "i", "inve", "inverno", "Inverno", "INVERNO", "o", "outono", "OUTONO", "Outono",  "p", "Primavera", "PRIMAVERA", "primavera"]))
        if a != 1:
            print(f"""
        Fruta {self.nome_fruta} cadastrada com sucesso!!!""")


    def exibir_frutas(self):
        print(f"""
        Nome da fruta: {self.nome_fruta} 
        Sabor da fruta: {self.sabor_fruta} 
        Tamanho da fruta: {self.tamanho_fruta} centrímetros
        Cor da fruta: {self.cor_fruta} 
        Formato da fruta: {self.formato_fruta} 
        Estação em que amadurece: {self.estacao_fruta}""")

class _flor():
    def __init__ (self, a):
        self.nome_flor = input("Insira o nome da flor: ")
        self.aroma_flor = input(f"Insira o aroma da flor {self.nome_flor}: ")
        self.tamanho_flor = str(trava(1,int, f"Insira o tamanho, em centrímetros, da flor {self.nome_flor}: ", 0))
        self.cor_flor = input(f"Insira a cor da flor {self.nome_flor}: ")
        self.formato_flor = input(f"Insira o formato da flor {self.nome_flor}: ")
        self.estacao_flor = str(trava(2,str, f"Insira a estação em que a flor {self.nome_flor} flosrece: ", ["Verão", "VERÃO", "Verao" ,"verão", "v", "verao", "i", "inve", "inverno", "Inverno", "INVERNO", "o", "outono", "OUTONO", "Outono",  "p", "Primavera", "PRIMAVERA", "primavera"]))
        if self.estacao_flor in ["Verão", "VERÃO", "Verao" ,"verão", "v", "verao"]:
            self.estacao_flor = "Verão"
        elif self.estacao_flor in ["i", "inve", "inverno", "Inverno", "INVERNO"]:
            self.estacao_flor = "Inverno"
        elif self.estacao_flor in ["o", "outono", "OUTONO", "Outono"]:
            self.estacao_flor = "Outuno"
        elif self.estacao_flor in ["o", "outono", "OUTONO", "Outono"]:
            self.estacao_flor = "Primavera"
        if a != 1:
            print(f"""
        Flor {self.nome_flor} cadastrada com sucesso!!!""")


    def exibir_flores(self):
        print(f"""
        Nome da flor: {self.nome_flor} 
        Aroma da flor: {self.aroma_flor} 
        Tamanho da flor: {self.tamanho_flor} centrímetros 
        Cor da flor: {self.cor_flor} 
        Formato da flor: {self.formato_flor} 
        Estação em que floresce: {self.estacao_flor}""")
    
class _planta(_flor, _fruta):
    def __init__ (self, a):
        
        self.nome = input("Insira o nome da planta: ")
        self.ambiente = input(f"Insira o tipo de ambiente da palnta {self.nome}: ")
        self.vegetacao = input(f"Insira a vegetação da planta {self.nome}: ")
        self.cor = input(f"Insira a cor da planta {self.nome}: ")
        self.tamanho = str(trava(1,int, f"Insira o tamanho, em centrímetros, da planta {self.nome}: ", 0))
        self.regar = str(trava(1,int, f"Insira quantas vezes têm que regar a planta {self.nome} na semana: ", 0))
        self.flor = trava(2,str, f"Insira se a planta {self.nome} possui flor: ", ["não", "n", "noa", "na", "no", "sim", "si", "s", "sm"])
        if self.flor.lower() in ["sim", "si", "s", "sm"]:
            _flor.__init__(self, 1)
            self.flor = True
            self.fruto = trava(2,str, f"Insira se a planta {self.nome} possui fruto: ", ["não", "n", "noa", "na", "no", "sim", "si", "s", "sm"])
            if self.fruto.lower() in ["sim", "si", "s", "sm"]:
                _fruta.__init__(self, 1)
                self.fruto = True
            else:
                self.fruto = False
        else:
            self.flor = False
            self.fruto = False
        if a != 1:
            print(f"""
        Planta {self.nome} cadastrada com sucesso!!!""")


    def exibir_plantas(self):
        print(f"""
        Nome: {self.nome} 
        Ambiente: {self.ambiente} 
        Vegetação: {self.vegetacao} 
        Cor: {self.cor} 
        Tamanho: {self.tamanho} centrímetros
        Regar: {self.regar} na semana""")
        if self.flor:
            print(f"""
                    Flor da planta {self.nome}

        Nome da flor: {self.nome_flor} 
        Aroma da flor: {self.aroma_flor} 
        Tamanho da flor: {self.tamanho_flor} centrímetros
        Cor da flor: {self.cor_flor} 
        Formato da flor: {self.formato_flor} 
        Estação em que floresce: {self.estacao_flor}""")
            if self.fruto:
                    print(f"""
                    Fruto da planta {self.nome}

        Nome da fruta: {self.nome_fruta} 
        Sabor da fruta: {self.sabor_fruta} 
        Tamanho da fruta: {self.tamanho_fruta} centrímetros
        Cor da fruta: {self.cor_fruta} 
        Formato da fruta: {self.formato_fruta} 
        Estação em que amadurece: {self.estacao_fruta}""")
            else:
                print("        Não tem fruto")
        
        else:
            print("        Não tem flor")
            print("        Não tem fruto")
        print("""
        """)

class _vegetal(_planta):
    def __init__ (self):
        super().__init__(1)
        self.comestivel = input("Insira a parte comestível do vegetal: ")
        self.sabor = input("Insira o sabor do vegetal: ")
        print(f"""
        O vegetal {self.nome} foi cadastrada com sucesso!!""") 

    def exibir_vegetais(self):
        print(f"""
        Nome: {self.nome} 
        Ambiente: {self.ambiente} 
        Vegetação: {self.vegetacao} 
        Cor: {self.cor} 
        Tamanho: {self.tamanho} centrímetros
        Regar: {self.regar} na semana
        Parte comestível: {self.comestivel}
        Sabor: {self.sabor}""")
        if self.flor:
            print(f"""
                    Flor do vegetal {self.nome}

        Nome da flor: {self.nome_flor} 
        Aroma da flor: {self.aroma_flor} 
        Tamanho da flor: {self.tamanho_flor} centrímetros
        Cor da flor: {self.cor_flor} 
        Formato da flor: {self.formato_flor} 
        Estação em que floresce: {self.estacao_flor}""")
            if self.fruto:
                print(f"""
                    Fruto do vegetal {self.nome}

        Nome da fruta: {self.nome_fruta} 
        Aroma da fruta: {self.sabor_fruta} 
        Tamanho da fruta: {self.tamanho_fruta} centrímetros
        Cor da fruta: {self.cor_fruta} 
        Formato da fruta: {self.formato_fruta} 
        Estação em que amadurece: {self.estacao_fruta}""")
            else:
                print("        Não tem fruto")
        
        else:
            print("        Não tem flor")
            print("        Não tem fruto")
        print("""
        """)




while True:
    menu = trava(2, int, """
        1 - Cadastrar
        2 - Exibir 
        3 - Pesquisar
        4 - Sair
        
Insira o número da opção: """, ["1", "2", "3", "4"])
    match menu:
        case 1:
            escolha = trava(2, int, """
        1 - Planta
        2 - Fruta
        3 - Flor
        4 - Vegetal
        
Insira o número da opção: """, ["1", "2", "3", "4"])
            match escolha:
                case 1:
                    plantas.append(_planta(0))

                case 2:
                    frutas.append(_fruta(0))

                case 3:
                    flores.append(_flor(0))

                case 4:
                    vegetais.append(_vegetal())

        case 2:
            escolha = trava(2, int, """
        1 - Planta
        2 - Fruta
        3 - Flor
        4 - Vegetal
        
Insira o número da opção que deseja exibir: """, ["1", "2", "3", "4"])
            match escolha:
                case 1:
                    if len(plantas) == 0:
                        print("""
        Nenhuma planta cadastrada!""")
                    for i in range(len(plantas)):
                        plantas[i].exibir_plantas()

                case 2:
                    if len(frutas) == 0:
                        print("""
        Nenhuma fruta cadastrada!""")
                    for i in range(len(frutas)):
                        frutas[i].exibir_frutas()

                case 3:
                    if len(flores) == 0:
                        print("""
        Nenhuma flor cadastrada!""")
                    for i in range(len(flores)):
                        flores[i].exibir_flores()

                case 4:
                    if len(vegetais) == 0:
                        print("""
        Nenhum vegetal cadastrada!""")
                    for i in range(len(vegetais)):
                        vegetais[i].exibir_vegetais()

        case 3:
            pesquisa = trava(2, int, """
        1 - Planta
        2 - Fruta 
        3 - Flor
        4 - Vegetal
        
Insira o número da opção que você quer pesquisar: """, ["1", "2", "3", "4"])
            match pesquisa:
                case 1:
                    com = trava(2, int, """
        1 - Nome
        2 - Ambiente 
        3 - Vegetação
        4 - Tamanho
        5 - Quantas vezes é regado
        6 - Flor (tem ou não)
        7 - Fruto (tem ou não)
        
Insira o número da opção que você quer pesquisar: """, ["1", "2", "3", "4", "5", "6", "7"])
                    match com:
                        case 1:
                            _pesquisar(1, plantas, "nome", "exibir_plantas", "Nome")

                        case 2:
                            _pesquisar(1, plantas, "ambiente", "exibir_plantas", "Ambiente")

                        case 3:
                            _pesquisar(1, plantas, "vegetacao", "exibir_plantas", "Vegetação")

                        case 4:
                            _pesquisar(1, plantas, "tamanho", "exibir_plantas", "Tamanho")

                        case 5:
                            _pesquisar(1, plantas, "regar", "exibir_plantas", "Vezes que é regado")

                        case 6:
                            tem_flor = trava(2, int, """
        1 - Tem
        2 - Não tem
        
Insira o número da opção que você quer pesquisar: """, ["1", "2"])
                            match tem_flor:
                                case 1:
                                    _pesquisar(2, plantas, "flor", "exibir_plantas", "Planta com flor")

                                case 2:
                                    _pesquisar(3, plantas, "flor", "exibir_plantas", "Planta sem flor")
                            
                        case 7:
                            tem_fruto = trava(2, int, """
        1 - Tem
        2 - Não tem
        
Insira o número da opção que você quer pesquisar: """, ["1", "2"])
                            match tem_fruto:
                                case 1:
                                    _pesquisar(2, plantas, "fruto", "exibir_plantas", "Planta com fruto")

                                case 2:
                                    _pesquisar(3, plantas, "fruto", "exibir_plantas", "Planta sem fruto")



                case 2:
                    com = trava(2, int, """
        1 - Nome
        2 - Sabor 
        3 - Tamanho
        4 - Cor
        5 - Formato
        6 - Estação
        
Insira o número da opção que você quer pesquisar: """, ["1", "2", "3", "4", "5", "6"])
                    match com:
                        case 1:
                            _pesquisar(1, frutas, "nome_fruta", "exibir_frutas", "Nome")

                        case 2:
                            _pesquisar(1, frutas, "sabor_fruta", "exibir_frutas", "Sabor")

                        case 3:
                            _pesquisar(1, frutas, "tamanho_fruta", "exibir_frutas", "Tamanho")

                        case 4:
                            _pesquisar(1, frutas, "cor_fruta", "exibir_frutas", "Cor")

                        case 5:
                            _pesquisar(1, frutas, "formato_fruta", "exibir_frutas", "Formato")

                        case 6:
                            _pesquisar(1, frutas, "estacao_fruta", "exibir_frutas", "Estação")

                case 3:
                    com = trava(2, int, """
        1 - Nome
        2 - Aroma 
        3 - Tamanho
        4 - Cor
        5 - Formato
        6 - Estação
        
Insira o número da opção que você quer pesquisar: """, ["1", "2", "3", "4", "5", "6"])
                    match com:
                        case 1:
                            _pesquisar(1, flores, "nome_flor", "exibir_flores", "Nome")

                        case 2:
                            _pesquisar(1, flores, "aroma_flor", "exibir_flores", "Aroma")

                        case 3:
                            _pesquisar(1, flores, "tamanho_flor", "exibir_flores", "Tamanho")
                        
                        case 4:
                            _pesquisar(1, flores, "cor_flor", "exibir_flores", "Cor")

                        case 5:
                            _pesquisar(1, flores, "formato_flor", "exibir_flores", "Formato")

                        case 6:
                            _pesquisar(1, flores, "estacao_flor", "exibir_flores", "Estação")


                case 4:

                    com = trava(2, int, """
    1 - Nome
    2 - Ambiente 
    3 - Vegetação
    4 - Tamanho
    5 - Quantas vezes é regado
    6 - Flor (tem ou não)
    7 - Fruto (tem ou não)
    8 - Comestível (é ou não)
    9 - Sabor
    
Insira o número da opção que você quer pesquisar: """, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                    match com:
                        case 1:
                            _pesquisar(1, vegetais, "nome", "exibir_vegetais", "Nome")

                        case 2:
                            _pesquisar(1, vegetais, "ambiente", "exibir_vegetais", "Ambiente")

                        case 3:
                            _pesquisar(1, vegetais, "vegetacao", "exibir_vegetais", "Vegetação")

                        case 4:
                            _pesquisar(1, vegetais, "tamanho", "exibir_vegetais", "Tamanho")

                        case 5:
                            _pesquisar(1, vegetais, "regar", "exibir_vegetais", "Vezes que é regado")

                        case 6:
                            tem_flor = trava(2, int, """
        1 - Tem
        2 - Não tem
        
Insira o número da opção que você quer pesquisar: """, ["1", "2"])
                            match tem_flor:
                                case 1:
                                    _pesquisar(2, plantas, "flor", "exibir_plantas", "Planta com flor")

                                case 2:
                                    _pesquisar(3, plantas, "flor", "exibir_plantas", "Planta sem flor")
                            
                        case 7:
                            tem_fruto = trava(2, int, """
        1 - Tem
        2 - Não tem
        
Insira o número da opção que você quer pesquisar: """, ["1", "2"])
                            match tem_fruto:
                                case 1:
                                    _pesquisar(2, plantas, "fruto", "exibir_plantas", "Planta com fruto")

                                case 2:
                                    _pesquisar(3, plantas, "fruto", "exibir_plantas", "Planta sem fruto")
                        
                        case 7:
                            comestivel = trava(2, int, """
        1 - É comestível
        2 - Não é comestível
        
Insira o número da opção que você quer pesquisar: """, ["1", "2"])
                            match comestivel:
                                case 1:
                                    _pesquisar(2, vegetais, "comestivel", "exibir_vegetais", "Vegetais comestíveis")

                                case 2:
                                    _pesquisar(3, plantas, "comestivel", "exibir_vegetais", "Vegetais não comestíveis")

                        case 8:
                            _pesquisar(1, vegetais, "sabor", "exibir_vegetais", "Sabor")


        case 4:
            break
    
    input("\nInsira ENTER para continuar: ")



