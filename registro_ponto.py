import datetime
from datetime import datetime

# Dicionário para armazenar os registros de ponto
registros_ponto = {}

def registrar_ponto():
    """
    Automatiza o registro de ponto para a data atual, preenchendo o próximo campo disponível.
    """
    print("\n--- REGISTRAR PONTO ---")

    # Usa a data e hora atual
    data_registro = datetime.now().date()
    data_chave = data_registro.strftime('%d-%m-%Y')
    horario_atual = datetime.now()

    # Inicializa o registro do dia, se necessário
    if data_chave not in registros_ponto:
        registros_ponto[data_chave] = [{
            'entrada1': None,
            'saida1': None,
            'entrada2': None,
            'saida2': None
        }]

    # Usa o último registro do dia
    ultimo_registro = registros_ponto[data_chave][-1]

    # Preenche o próximo campo disponível
    for campo in ['entrada1', 'saida1', 'entrada2', 'saida2']:
        if ultimo_registro[campo] is None:
            ultimo_registro[campo] = horario_atual
            print(f"{campo.capitalize()} registrada às {horario_atual.strftime('%H:%M:%S')} para o dia {data_chave}.")
            break
    else:
        # Todos os campos preenchidos: inicia novo registro
        novo_registro = {
            'entrada1': horario_atual,
            'saida1': None,
            'entrada2': None,
            'saida2': None
        }
        registros_ponto[data_chave].append(novo_registro)
        print(f"Todos os campos do último registro estavam preenchidos.")
        print(f"Novo registro iniciado com Entrada1 às {horario_atual.strftime('%H:%M:%S')}.")

def buscar_registros():
    """
    Permite ao usuário buscar e exibir os registros de ponto por uma data específica.
    """
    print("\n--- BUSCAR REGISTROS DE PONTO ---")

    while True:
        data_busca_str = input("Digite a data para buscar os registros (DD-MM-AAAA, ex: 04-07-2025): ")
        try:
            data_busca = datetime.strptime(data_busca_str, '%d-%m-%Y').date()
            break
        except ValueError:
            print("Formato de data inválido. Por favor, use DD-MM-AAAA.")

    data_chave_busca = data_busca.strftime('%d-%m-%Y')

    if data_chave_busca in registros_ponto:
        print(f"\nRegistros de ponto para {data_chave_busca}:")
        for i, registro in enumerate(registros_ponto[data_chave_busca]):
            print(f"  Registro {i + 1}:")
            for campo in ['entrada1', 'saida1', 'entrada2', 'saida2']:
                valor = registro[campo]
                print(f"    {campo.capitalize()}: {valor.strftime('%H:%M:%S') if valor else 'Não registrado'}")
    else:
        print(f"Nenhum registro encontrado para a data: {data_chave_busca}.")

def menu_principal():
    """
    Exibe o menu principal e gerencia as opções do usuário.
    """
    while True:
        print("\n" + "="*30)
        print("   Registre seu Ponto!!!")
        print("="*30)
        print("1. Registrar Ponto")
        print("2. Buscar Registros por Data")
        print("3. Sair")
        print("="*30)

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            registrar_ponto()
        elif escolha == '2':
            buscar_registros()
        elif escolha == '3':
            print("Saindo do sistema de ponto. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")

# --- Execução do Programa ---
if __name__ == "__main__":
    menu_principal()
