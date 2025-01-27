# Automacao de Cadastro de Produtos

Este script foi desenvolvido para automatizar o cadastro de produtos em uma plataforma online. Utilizando a biblioteca PyAutoGUI, o programa simula interações humanas para abrir o navegador, acessar a página de login, preencher credenciais e cadastrar produtos com base em uma planilha CSV.

## Funcionalidades
- Abre o navegador e acessa o site desejado
- Realiza login automaticamente
- Importa uma planilha CSV com dados dos produtos
- Preenche os campos do formulário e cadastra os produtos um a um

## Tecnologias Utilizadas
- Python
- PyAutoGUI
- Pandas

## Como Usar
1. Instale as dependências com:
   ```sh
   pip install pyautogui pandas
   ```
2. Certifique-se de ter um arquivo `produtos.csv` contendo as informações dos produtos.
3. Execute o script em um ambiente Windows com o Chrome instalado.


## Observações
- O script pode precisar de ajustes nas coordenadas de clique, dependendo da resolução da tela.
- Há um tempo de espera (`time.sleep`) para garantir que as ações ocorram corretamente, e assim como as coordenadas de clique, isso pode mudar de computador para computador.
- Certifique-se de que o navegador e o site estão acessíveis no momento da execução.

## Autor
Este script foi criado como um exercício de automação para praticar manipulação de dados e interação com interfaces gráficas usando Python.

