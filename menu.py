def mostrar_menu(streams):
    for i, stream in enumerate(streams, start=1):
        print(f"{i} -- {stream}")
    opcao = int(input("Escolha um dos serviços de streaming: "))
    return opcao
