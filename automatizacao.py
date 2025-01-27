import pyautogui
import time

pyautogui.PAUSE = 2

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.click(x=149, y=195)

# entrar no link 
time.sleep(8)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)


# fazer login
pyautogui.click(x=460, y=374) # selecionar o campo de email
# escrever o seu email
pyautogui.write("rafasancor@gmail.com")
pyautogui.press("tab")
pyautogui.write("rafael")
pyautogui.click(x=673, y=534) # clique no botao de login
time.sleep(3)

# importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=503, y=259)
    # pegar da tabela o valor do campo que irá preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
