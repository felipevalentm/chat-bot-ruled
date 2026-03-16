# Chatbot de Atendimento com Gestão de Contexto

Este projeto consiste em um sistema de atendimento automatizado desenvolvido em Python. Ele utiliza uma estrutura de **máquina de estados** para gerenciar o contexto da conversa, permitindo que o bot guie o usuário através de um fluxo lógico de coleta de dados e fornecimento de informações.

##  Funcionalidades

- **Fluxo Linear de Diálogo:** O bot segue uma sequência lógica: Saudação -> Identificação do Usuário -> Seleção de Departamento -> Entrega de Informação.
- **Base de Dados Estruturada:** Utiliza dicionários para armazenar contatos de setores como RH, Financeiro e Vendas.
- **Tratamento de Entrada:** Limpeza de caracteres especiais e normalização de texto para evitar erros de leitura.
- **Memória de Contexto:** A variável `contexto` controla em qual etapa o usuário está, permitindo respostas personalizadas (como usar o nome do usuário na frase).

##  Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Conceitos:** Dicionários, Loops (`while`), Condicionais (`if/elif`), Manipulação de Strings e Gerenciamento de Estado.

