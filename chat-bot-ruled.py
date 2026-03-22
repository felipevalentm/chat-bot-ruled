
informacoes = {
    "financeiro" : ["financas@gmail.com", "24993956585"],
    "rh" : ["recursos@gmail.com", "24993956589"],
    "vendas" : ["comercial@gmail.com", "24993956589"],
    }

interacoes = {
    "saudacao": [
    "oi", "olá", "ola", "oie", "oii",
    "eai", "eaí", "eaí", "fala", "falae",
    "salve", "opa", "opa tudo bem",
    "bom dia", "boa tarde", "boa noite",
    "tudo bem", "td bem", "blz", "beleza",
    "como vai", "como vc tá", "como você tá",
    "tranquilo", "suave",
    "hello", "hi", "hey"],

    "despedida": [
    "tchau", "tchau tchau", "até mais", "até logo", "até",
    "falou", "fui", "flw", "vlw", "valeu",
    "encerrar", "finalizar", "terminar", "fim",
    "já resolveu", "resolvido", "era isso", "só isso",
    "obrigado era isso", "valeu era isso",
    "até breve", "nos vemos"],

    "ajuda": [
    "ajuda", "socorro", "help", "preciso de ajuda",
    "pode ajudar", "me ajuda", "me ajude",
    "como funciona", "como faz", "como fazer",
    "não entendi", "nao entendi", "não sei", "nao sei",
    "dúvida", "duvida", "tenho uma dúvida", "tenho duvida",
    "explica", "explicar", "pode explicar",
    "quero saber", "me informa", "informação", "informacoes",
    "o que fazer", "como resolver", "resolver isso",
    "não consigo", "nao consigo", "deu erro", "erro",
    "problema", "tá dando erro", "ta dando erro"]

    }

contexto = None
mensagem = input("Usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower()

def definindo_intencao():
    for tipo, palavras in interacoes.items():
        for termo in palavras:
            if termo in mensagem:
                return tipo
    return "desconhecido"

intencao_definida = definindo_intencao()
contexto = intencao_definida

if contexto == "saudacao" or contexto == "ajuda":
        nome = input("bot: qual seu nome? \n"
             "usuário: ")
        print(f"{nome}, qual area deseja contatar? ")
        area = input("usuário: ").replace(".", "").replace("?", "").replace("!", "").replace(",", "").lower()
        if area == "rh":
            print(f"email: {informacoes['rh'][0]}")
            print(f"contato: {informacoes['rh'][1]}")
        elif area == "financeiro":
            print(f"email: {informacoes['financeiro'][0]}")
            print(f"contato: {informacoes['financeiro'][1]}")
        elif area == "comercial":
            print(f"email: {informacoes['vendas'][0]}")
            print(f"contato: {informacoes['vendas'][1]}")
        else:
            print("não entendemos.. encerrando chat")
elif contexto == "despedida":
        print("encerrando.. tchau")
     

    