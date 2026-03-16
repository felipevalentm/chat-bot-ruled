
informacoes = {
    "financeiro" : ["financas@gmail.com", "24993956585"],
    "rh" : ["recursos@gmail.com", "24993956589"],
    "vendas" : ["comercial@gmail.com", "24993956589"],
    }

interacao = {
    "saudacao": ["oi", "olá", "bom", "dia", "boa", "tarde", "tudo", "bem"],
    "despedida": ["tchau", "fim", "encerrar"]
    }

contexto = None
frase_inicial = input("Usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower().split()

while True:
    for x in frase_inicial:
        if x in interacao["saudacao"]:
            contexto = 1
            print("Bot: ", "bom dia! qual seu nome?")            
            if contexto == 1:
                resposta_nome = input("Usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower()
                contexto = 2
                if contexto == 2:
                    print("Bot: " , f"{resposta_nome}, qual área deseja contatar? ")
                    resposta_area = input("Usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower()
                    if resposta_area in informacoes:
                        print(", ".join(informacoes[resposta_area]))
                    else:
                        print("área inválida!")
        elif x in interacao["despedida"]:    
            contexto = 0
            print("conversa encerrada...")
    break