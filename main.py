import dados
import menu
from datetime import datetime

dados = dados.ler()
stream = list(dados.keys())
opcao = menu.mostrar_menu(stream)
stream_escolhida = stream[opcao - 1]

print("Dia e hora: ", datetime.now())
print("Você escolheu: ", stream_escolhida)
print("Preço: ", dados[stream_escolhida])