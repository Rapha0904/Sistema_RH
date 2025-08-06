import datetime
from datetime import datetime, timedelta

# --- Banco de Dados em Memória (Dicionários Globais) ---
USUARIOS = {
    "RH101706": {"senha": "1017069892", "tipo": "RH"},
    "224581": {"senha": "122362", "tipo": "FUNCIONARIO", "nome": "Funcionário Teste", "cpf": "224581"},
    "Gerente": {"senha": "ADM123456", "tipo": "COORDENADOR"}
}

FUNCIONARIOS = {
    "224581": {"nome": "Funcionário Teste", "departamento": "TI", "central_custos": "CC-004 (Desenvolvimento)"}
}

REGISTROS_PONTO = {
    "224581": {
        (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y'): [
            {
                'entrada1': datetime.combine(datetime.now().date() - timedelta(days=1), datetime.min.time().replace(hour=8, minute=0)),
                'saida1': datetime.combine(datetime.now().date() - timedelta(days=1), datetime.min.time().replace(hour=12, minute=0)),
                'entrada2': datetime.combine(datetime.now().date() - timedelta(days=1), datetime.min.time().replace(hour=13, minute=0)),
                'saida2': datetime.combine(datetime.now().date() - timedelta(days=1), datetime.min.time().replace(hour=17, minute=0))
            }
        ],
        datetime.now().strftime('%d-%m-%Y'): [
            {
                'entrada1': datetime.combine(datetime.now().date(), datetime.min.time().replace(hour=9, minute=0)),
                'saida1': datetime.combine(datetime.now().date(), datetime.min.time().replace(hour=13, minute=0)),
                'entrada2': None,
                'saida2': None
            }
        ]
    }
}

# --- Listas de Opções (ENUMs) ---
OPCOES_DEPARTAMENTO = [
    "Administrativo / Facilities", "Jurídico", "Tecnologia da Informação", "Financeiro", "Recursos Humanos",
    "Vendas", "Logística / Suprimentos", "Operações / Produção", "Engenharia", "Pesquisa e Desenvolvimento",
    "Qualidade", "Sustentabilidade / ESG", "Comercial", "Marketing", "Comunicação Corporativa",
    "Atendimento ao Cliente", "Compliance", "Auditoria", "Planejamento Estratégico", "Gestão de Projetos",
    "Inteligência de Mercado", "Relações com Investidores", "Comércio Exterior / Internacional", "Compras / Suprimentos"
]

OPCOES_CENTRAL_CUSTOS = {
    "Administrativo / Facilities": "CC-153 (Administrativo)",
    "Jurídico": "CC-374 (Compliance)",
    "Tecnologia da Informação": "CC-805 (TI)",
    "Financeiro": "CC-390 (Financeiro)",
    "Recursos Humanos": "CC-247 (Recursos Humanos)",
    "Vendas": "CC-618 (Vendas)",
    "Logística / Suprimentos": "CC-927 (Logística)",
    "Operações / Produção": "CC-690 (Produção)",
    "Engenharia": "CC-011 (Engenharia)",
    "Pesquisa e Desenvolvimento": "CC-271 (Pesquisa)",
    "Qualidade": "CC-495 (Qualidade)",
    "Sustentabilidade / ESG": "CC-549 (Sustentabilidade)",
    "Comercial": "CC-106 (Comercial)",
    "Marketing": "CC-277 (Marketing)",
    "Comunicação Corporativa": "CC-667 (Comunicação)",
    "Atendimento ao Cliente": "CC-802 (Atendimento)",
    "Compliance": "CC-190 (Compliance)",
    "Auditoria": "CC-431 (Auditoria)",
    "Planejamento Estratégico": "CC-344 (Planejamento)",
    "Gestão de Projetos": "CC-123 (Projetos)",
    "Inteligência de Mercado": "CC-277 (Inteligência)",
    "Relações com Investidores": "CC-393 (Investidores)",
    "Comércio Exterior / Internacional": "CC-727 (Internacional)",
    "Compras / Suprimentos": "CC-093 (Compras)"
}

# --- Funções Auxiliares Comuns ---
def selecionar_opcao(opcoes, tipo_selecao):
    """Exibe um menu numerado e permite ao usuário selecionar uma opção."""
    while True:
        print(f"\nSelecione o {tipo_selecao}:")
        if isinstance(opcoes, dict):
            lista_opcoes = list(opcoes.keys())
        else:
            lista_opcoes = opcoes
        for i, opcao in enumerate(lista_opcoes):
            print(f"{i + 1}. {opcao}")
        try:
            escolha = int(input(f"Digite o NÚMERO da sua escolha para {tipo_selecao}: "))
            if 1 <= escolha <= len(lista_opcoes):
                selecionado = lista_opcoes[escolha - 1]
                if isinstance(opcoes, dict):
                    return opcoes[selecionado]
                else:
                    return selecionado
            else:
                print(f"Opção inválida. Por favor, digite um número entre 1 e {len(lista_opcoes)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def coletar_horario(prompt, data_base):
    """
    Coleta um horário (HH:MM) e o combina com uma data.
    Retorna um objeto datetime ou None se o input for vazio.
    """
    while True:
        hora_str = input(prompt)
        if not hora_str:
            return None
        try:
            h, m = map(int, hora_str.split(':'))
            return datetime.combine(data_base, datetime.min.time().replace(hour=h, minute=m))
        except ValueError:
            print("Formato de horário inválido. Por favor, use HH:MM ou deixe em branco.")

def formatar_ponto(ponto_datetime):
    """Formata um objeto datetime de ponto para HH:MM:SS ou 'Não registrado'."""
    return ponto_datetime.strftime('%H:%M:%S') if ponto_datetime else 'Não registrado'

def exibir_registros_dia(registros_do_dia, data_chave):
    """Exibe os registros de ponto para um dia específico."""
    if registros_do_dia:
        print(f"\nRegistros para {data_chave}:")
        for i, registro in enumerate(registros_do_dia):
            print(f"  Registro {i + 1}:")
            print(f"    Entrada 1: {formatar_ponto(registro['entrada1'])}")
            print(f"    Saída 1:   {formatar_ponto(registro['saida1'])}")
            print(f"    Entrada 2: {formatar_ponto(registro['entrada2'])}")
            print(f"    Saída 2:   {formatar_ponto(registro['saida2'])}")
    else:
        print(f"Nenhum registro encontrado para {data_chave}.")

# --- Funções Específicas do RH ---
def registrar_funcionario():
    print("\n--- REGISTRAR NOVO FUNCIONÁRIO ---")
    while True:
        nome = input("Nome completo do funcionário: ").strip()
        if nome:
            break
        print("Nome não pode ser vazio.")

    while True:
        cpf = input("CPF do funcionário (apenas números): ").strip()
        if not cpf.isdigit():
            print("CPF deve conter apenas números.")
        elif cpf in FUNCIONARIOS:
            print("Funcionário com este CPF já cadastrado.")
        else:
            break

    departamento = selecionar_opcao(OPCOES_DEPARTAMENTO, "departamento")
    central_custo = selecionar_opcao(OPCOES_CENTRAL_CUSTOS, "central de custos")

    FUNC_SENHA = cpf[-6:]  # Sugestão: últimos 6 dígitos do CPF como senha inicial

    # Adiciona o funcionário
    FUNCIONARIOS[cpf] = {
        "nome": nome,
        "departamento": departamento,
        "central_custos": central_custo
    }
    # Cria uma entrada de usuário para o funcionário
    USUARIOS[cpf] = {"senha": FUNC_SENHA, "tipo": "FUNCIONARIO", "nome": nome, "cpf": cpf}
    REGISTROS_PONTO[cpf] = {}  # Inicializa a entrada de ponto para o novo funcionário

    print(f"\nFuncionário '{nome}' (CPF: {cpf}) registrado com sucesso!")
    print(f"Usuário de Ponto: {cpf}, Senha Inicial: {FUNC_SENHA}")

def consultar_funcionarios_rh():
    print("\n--- CONSULTAR FUNCIONÁRIOS ---")
    print("1. Por Nome")
    print("2. Por Departamento")
    print("3. Por Central de Custos")
    print("4. Ver Todos")
    escolha = input("Digite o número da opção de consulta: ")

    resultados = []
    if escolha == '1':
        termo = input("Digite parte do nome do funcionário: ").lower()
        resultados = [f for f_cpf, f in FUNCIONARIOS.items() if termo in f['nome'].lower()]
    elif escolha == '2':
        departamento_escolhido = selecionar_opcao(OPCOES_DEPARTAMENTO, "departamento para consulta")
        resultados = [f for f_cpf, f in FUNCIONARIOS.items() if f['departamento'] == departamento_escolhido]
    elif escolha == '3':
        central_escolhida = selecionar_opcao(OPCOES_CENTRAL_CUSTOS, "central de custos para consulta")
        resultados = [f for f_cpf, f in FUNCIONARIOS.items() if f['central_custos'] == central_escolhida]
    elif escolha == '4':
        resultados = list(FUNCIONARIOS.values())
    else:
        print("Opção inválida.")
        return

    if resultados:
        print("\n--- RESULTADOS DA CONSULTA ---")
        for func in resultados:
            cpf_func = func_cpf(func['nome'])
            print(f"Nome: {func['nome']}, CPF: {cpf_func}, Depto: {func['departamento']}, CC: {func['central_custos']}")
    else:
        print("Nenhum funcionário encontrado com os critérios fornecidos.")

def func_cpf(nome):
    """Função auxiliar para encontrar o CPF de um funcionário pelo nome (se único)."""
    for cpf, dados in FUNCIONARIOS.items():
        if dados['nome'] == nome:
            return cpf
    return "N/A"

# --- Menu RH ---
def menu_rh():
    while True:
        print("\n" + "="*30)
        print("   MENU RH")
        print("="*30)
        print("1. Registrar/Incluir Funcionário")
        print("2. Consultar Funcionários")
        print("3. Logout")
        print("="*30)

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            registrar_funcionario()
        elif escolha == '2':
            consultar_funcionarios_rh()
        elif escolha == '3':
            print("Saindo do Menu RH.")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")

# --- Funções Específicas do Funcionário ---
def registrar_ponto_funcionario(cpf_funcionario_logado):
    print("\n--- REGISTRAR MEU PONTO ---")

    while True:
        data_str = input("Digite a data do registro (DD-MM-AAAA, ex: 04-07-2025 ou 'hoje' para a data atual): ").lower()
        if data_str == 'hoje':
            data_registro = datetime.now().date()
        else:
            try:
                data_registro = datetime.strptime(data_str, '%d-%m-%Y').date()
            except ValueError:
                print("Formato de data inválido. Por favor, use DD-MM-AAAA ou 'hoje'.")
                continue
        break

    data_chave = data_registro.strftime('%d-%m-%Y')

    if cpf_funcionario_logado not in REGISTROS_PONTO:
        REGISTROS_PONTO[cpf_funcionario_logado] = {}
    if data_chave not in REGISTROS_PONTO[cpf_funcionario_logado]:
        REGISTROS_PONTO[cpf_funcionario_logado][data_chave] = []

    novo_registro = {'entrada1': None, 'saida1': None, 'entrada2': None, 'saida2': None}

    print(f"\nRegistrando ponto para {data_chave} (seu ponto).")
    print("Por favor, digite os horários no formato HH:MM (ou deixe em branco se não houver).")

    novo_registro['entrada1'] = coletar_horario("Entrada 1 (HH:MM): ", data_registro)
    novo_registro['saida1'] = coletar_horario("Saída 1 (HH:MM): ", data_registro)
    novo_registro['entrada2'] = coletar_horario("Entrada 2 (HH:MM): ", data_registro)
    novo_registro['saida2'] = coletar_horario("Saída 2 (HH:MM): ", data_registro)

    REGISTROS_PONTO[cpf_funcionario_logado][data_chave].append(novo_registro)
    print(f"Ponto para {data_chave} registrado com sucesso!")

def consultar_meus_pontos(cpf_funcionario_logado):
    print("\n--- CONSULTAR MEUS REGISTROS DE PONTO ---")

    while True:
        data_busca_str = input("Digite a data para buscar (DD-MM-AAAA ou 'hoje'): ").lower()
        if data_busca_str == 'hoje':
            data_busca = datetime.now().date()
        else:
            try:
                data_busca = datetime.strptime(data_busca_str, '%d-%m-%Y').date()
            except ValueError:
                print("Formato de data inválido. Por favor, use DD-MM-AAAA ou 'hoje'.")
                continue
        break

    data_chave_busca = data_busca.strftime('%d-%m-%Y')

    if cpf_funcionario_logado in REGISTROS_PONTO and data_chave_busca in REGISTROS_PONTO[cpf_funcionario_logado]:
        exibir_registros_dia(REGISTROS_PONTO[cpf_funcionario_logado][data_chave_busca], data_chave_busca)
    else:
        print(f"Nenhum registro encontrado para {data_chave_busca}.")

# --- Menu Funcionário ---
def menu_funcionario(cpf_funcionario_logado):
    while True:
        print("\n" + "="*30)
        print(f"   MENU FUNCIONÁRIO ({cpf_funcionario_logado})")
        print("="*30)
        print("1. Registrar Ponto")
        print("2. Consultar Meus Pontos")
        print("3. Editar Ponto (funcionalidade básica)")
        print("4. Logout")
        print("="*30)

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            registrar_ponto_funcionario(cpf_funcionario_logado)
        elif escolha == '2':
            consultar_meus_pontos(cpf_funcionario_logado)
        elif escolha == '3':
            print("\nFuncionalidade de edição básica. Entre em contato com seu gestor para edições complexas.")
            registrar_ponto_funcionario(cpf_funcionario_logado)
        elif escolha == '4':
            print("Saindo do Menu Funcionário.")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.")

# --- Funções Específicas do Coordenador/Gestor/Diretor ---
def consultar_ponto_geral(filtro_tipo):
    print(f"\n--- CONSULTAR PONTOS POR {filtro_tipo.upper()} ---")

    funcionarios_filtrados = []
    if filtro_tipo == "CENTRAL DE CUSTOS":
        central_escolhida = selecionar_opcao(OPCOES_CENTRAL_CUSTOS, "central de custos para consulta")
        funcionarios_filtrados = [
            f_cpf for f_cpf, f_data in FUNCIONARIOS.items()
            if f_data['central_custos'] == central_escolhida
        ]
    elif filtro_tipo == "DEPARTAMENTO":
        departamento_escolhido = selecionar_opcao(OPCOES_DEPARTAMENTO, "departamento para consulta")
        funcionarios_filtrados = [
            f_cpf for f_cpf, f_data in FUNCIONARIOS.items()
            if f_data['departamento'] == departamento_escolhido
        ]
    elif filtro_tipo == "PERÍODO":
        while True:
            data_inicio_str = input("Data de início do período (DD-MM-AAAA): ")
            data_fim_str = input("Data de fim do período (DD-MM-AAAA): ")
            try:
                data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
                data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()
                if data_inicio > data_fim:
                    print("Data de início não pode ser posterior à data de fim.")
                    continue
                break
            except ValueError:
                print("Formato de data inválido. Use DD-MM-AAAA.")
        funcionarios_filtrados = list(FUNCIONARIOS.keys())

    if not funcionarios_filtrados:
        print("Nenhum funcionário encontrado para o filtro.")
        return

    print("\n--- RESULTADOS DA CONSULTA DE PONTOS ---")
    for cpf_func in funcionarios_filtrados:
        if cpf_func in REGISTROS_PONTO:
            nome_func = FUNCIONARIOS.get(cpf_func, {}).get('nome', 'Desconhecido')
            print(f"\nFuncionário: {nome_func} (CPF: {cpf_func})")
            registros_func = REGISTROS_PONTO[cpf_func]

            datas_para_exibir = []
            if filtro_tipo == "PERÍODO":
                for data_str_reg in registros_func.keys():
                    data_reg = datetime.strptime(data_str_reg, '%d-%m-%Y').date()
                    if data_inicio <= data_reg <= data_fim:
                        datas_para_exibir.append(data_str_reg)
                datas_para_exibir.sort(key=lambda d: datetime.strptime(d, '%d-%m-%Y'))
            else:
                datas_para_exibir = sorted(registros_func.keys(), key=lambda d: datetime.strptime(d, '%d-%m-%Y'))

            if not datas_para_exibir:
                print("  Nenhum registro de ponto encontrado no período/critério para este funcionário.")
                continue

            for data_chave in datas_para_exibir:
                exibir_registros_dia(registros_func[data_chave], data_chave)
        else:
            print(f"\nFuncionário: {FUNCIONARIOS.get(cpf_func, {}).get('nome', 'Desconhecido')} (CPF: {cpf_func}) - Sem registros de ponto.")

def adicionar_editar_ponto_funcionario():
    print("\n--- ADICIONAR/EDITAR PONTO DE FUNCIONÁRIO ---")

    cpf_busca = input("Digite o CPF do funcionário para adicionar/editar ponto: ").strip()

    if cpf_busca not in FUNCIONARIOS:
        print("Funcionário não encontrado.")
        return

    nome_func = FUNCIONARIOS[cpf_busca]['nome']
    print(f"\nEditando ponto para: {nome_func} (CPF: {cpf_busca})")

    while True:
        data_str = input("Digite a data do registro (DD-MM-AAAA, ex: 04-07-2025 ou 'hoje' para a data atual): ").lower()
        if data_str == 'hoje':
            data_registro = datetime.now().date()
        else:
            try:
                data_registro = datetime.strptime(data_str, '%d-%m-%Y').date()
            except ValueError:
                print("Formato de data inválido. Por favor, use DD-MM-AAAA ou 'hoje'.")
                continue
        break

    data_chave = data_registro.strftime('%d-%m-%Y')

    if cpf_busca not in REGISTROS_PONTO:
        REGISTROS_PONTO[cpf_busca] = {}
    if data_chave not in REGISTROS_PONTO[cpf_busca]:
        REGISTROS_PONTO[cpf_busca][data_chave] = []

    exibir_registros_dia(REGISTROS_PONTO[cpf_busca][data_chave], data_chave)

    print("\nPreencha os novos horários (deixe em branco para manter o existente ou não registrar):")
    novo_registro = {'entrada1': None, 'saida1': None, 'entrada2': None, 'saida2': None}

    novo_registro['entrada1'] = coletar_horario("Entrada 1 (HH:MM): ", data_registro)
    novo_registro['saida1'] = coletar_horario("Saída 1 (HH:MM): ", data_registro)
    novo_registro['entrada2'] = coletar_horario("Entrada 2 (HH:MM): ", data_registro)
    novo_registro['saida2'] = coletar_horario("Saída 2 (HH:MM): ", data_registro)

    REGISTROS_PONTO[cpf_busca][data_chave].append(novo_registro)
    print(f"Ponto para {nome_func} em {data_chave} adicionado/editado com sucesso!")

# --- Menu Coordenador ---
def menu_coordenador():
    while True:
        print("\n" + "="*30)
        print("   MENU COORDENADOR/GESTOR/DIRETOR")
        print("="*30)
        print("1. Consultar Pontos por Central de Custos")
        print("2. Consultar Pontos por Departamento")
        print("3. Consultar Pontos por Período")
        print("4. Adicionar/Editar Ponto de Funcionário")
        print("5. Logout")
        print("="*30)

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            consultar_ponto_geral("CENTRAL DE CUSTOS")
        elif escolha == '2':
            consultar_ponto_geral("DEPARTAMENTO")
        elif escolha == '3':
            consultar_ponto_geral("PERÍODO")
        elif escolha == '4':
            adicionar_editar_ponto_funcionario()
        elif escolha == '5':
            print("Saindo do Menu Coordenador.")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3, 4 ou 5.")

# --- Lógica de Login ---
def main_login():
    print("="*40)
    print("   BEM-VINDO AO SISTEMA DE PONTO")
    print("="*40)

    while True:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in USUARIOS and USUARIOS[usuario]["senha"] == senha:
            tipo_usuario = USUARIOS[usuario]["tipo"]
            print(f"\nLogin bem-sucedido! Bem-vindo, {tipo_usuario.upper()}.")

            if tipo_usuario == "RH":
                menu_rh()
            elif tipo_usuario == "FUNCIONARIO":
                menu_funcionario(usuario)
            elif tipo_usuario == "COORDENADOR":
                menu_coordenador()
        else:
            print("Usuário ou senha inválidos. Tente novamente.")

        continuar = input("\n[L] Login novamente ou [S] Sair do programa? ").lower()
        if continuar == 's':
            print("Fechando o sistema. Até mais!")
            break

# --- Execução do Programa ---
if __name__ == "__main__":
    main_login()
