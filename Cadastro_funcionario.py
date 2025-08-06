def coletar_informacoes_colaborador():
    """
    Coleta diversas informações do usuário, incluindo dados pessoais, endereço
    e informações relacionadas ao trabalho, e as armazena em um dicionário.
    Para campos de documentos, aceita links. Para seleções, apresenta menus.
    """
    dados_colaborador = {}

    print("="*40)
    print("   COLETA DE INFORMAÇÕES DO COLABORADOR")
    print("="*40)

    # 1. Informações Pessoais e Endereço
    dados_colaborador['nome_completo'] = str(input('Qual seu nome completo?: '))
    dados_colaborador['nome_social'] = str(input('Digite seu nome social, se tiver: '))
    dados_colaborador['logradouro'] = str(input('Digite seu endereço: '))
    dados_colaborador['numero_logradouro'] = str(input('Digite o número do endereço: '))
    dados_colaborador['complemento'] = str(input('Digite o complemento do seu endereço: '))

    while True:
        try:
            dados_colaborador['cpf'] = int(input('Digite seu CPF (apenas números): '))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números para o CPF.")

    print("\n--- Links para Documentos ---")
    print("Por favor, insira o LINK de acesso para cada documento:")
    dados_colaborador['link_certidao_casamento_nascimento'] = str(input('Link da certidão de casamento ou nascimento: '))
    dados_colaborador['link_comprovante_residencia'] = str(input('Link do comprovante de residência: '))
    dados_colaborador['link_comprovante_cpf_rg'] = str(input('Link do comprovante de CPF/RG: '))
    dados_colaborador['link_titulo_eleitor'] = str(input('Link do título de eleitor: '))

    print("\n--- Seleção da Sede da Empresa ---")
    opcoes_sede_empresa = ["Curitiba (MATRIZ)", "Bahia", "São Paulo", "Minas Gerais"]
    dados_colaborador['sede_empresa'] = selecionar_opcao(opcoes_sede_empresa, "sede da empresa")

    print("\n--- Seleção de Departamento ---")
    opcoes_departamento = [
        "Administrativo / Facilities", "Jurídico", "Tecnologia da Informação", "Financeiro", "Recursos Humanos", "Vendas",
        "Logística / Cadeia de Suprimentos", "Operações / Produção", "Engenharia", "Pesquisa e Desenvolvimento",
        "Qualidade", "Sustentabilidade / ESG", "Comercial", "Marketing", "Comunicação Corporativa / Relações Públicas",
        "Serviços ao Cliente / Atendimento ao Cliente", "Compliance", "Auditoria", "Planejamento Estratégico",
        "Gestão de Projetos", "Inteligência de Mercado", "Relações com Investidores", "Comércio Exterior / Internacional",
        "Compras / Suprimentos"
    ]
    dados_colaborador['departamento'] = selecionar_opcao(opcoes_departamento, "departamento")

    print("\n--- Seleção de Cargo ---")
    opcoes_cargo = [
        # Administrativo / Facilities
        "Assistente Administrativo", "Analista Administrativo Júnior", "Analista Administrativo Pleno", "Analista Administrativo Sênior",
        "Supervisor Administrativo", "Coordenador Administrativo", "Gerente Administrativo",

        # Jurídico
        "Assistente Jurídico", "Analista Jurídico Júnior", "Analista Jurídico Pleno", "Analista Jurídico Sênior",
        "Supervisor Jurídico", "Coordenador Jurídico", "Gerente Jurídico",

        # Tecnologia da Informação
        "Analista de Sistemas", "Desenvolvedor Full Stack", "Analista de TI Júnior", "Analista de TI Pleno", "Analista de TI Sênior",
        "Supervisor de TI", "Coordenador de Tecnologia", "Gerente de TI",

        # Financeiro
        "Assistente Financeiro", "Analista Financeiro Júnior", "Analista Financeiro Pleno", "Analista Financeiro Sênior",
        "Supervisor Financeiro", "Coordenador Financeiro", "Gerente Financeiro",

        # Recursos Humanos
        "Assistente de RH", "Analista de RH Júnior", "Analista de RH Pleno", "Analista de RH Sênior",
        "Supervisor de RH", "Coordenador de RH", "Gerente de RH",

        # Vendas
        "Consultor de Vendas", "Executivo de Contas", "Analista Comercial Júnior", "Analista Comercial Pleno", "Analista Comercial Sênior",
        "Supervisor de Vendas", "Coordenador de Vendas", "Gerente de Vendas",

        # Logística / Suprimentos
        "Assistente de Logística", "Analista de Logística Júnior", "Analista de Logística Pleno", "Analista de Logística Sênior",
        "Supervisor de Logística", "Coordenador de Logística", "Gerente de Logística",

        # Operações / Produção
        "Assistente de Produção", "Analista de Produção Júnior", "Analista de Produção Pleno", "Analista de Produção Sênior",
        "Supervisor de Produção", "Coordenador de Produção", "Gerente de Produção",

        # Engenharia
        "Engenheiro Júnior", "Engenheiro Pleno", "Engenheiro Sênior", "Supervisor de Engenharia", "Coordenador de Engenharia", "Gerente de Engenharia",

        # Pesquisa e Desenvolvimento
        "Assistente de P&D", "Analista de P&D Júnior", "Analista de P&D Pleno", "Analista de P&D Sênior",
        "Supervisor de P&D", "Coordenador de P&D", "Gerente de P&D",

        # Qualidade
        "Assistente da Qualidade", "Analista da Qualidade Júnior", "Analista da Qualidade Pleno", "Analista da Qualidade Sênior",
        "Supervisor de Qualidade", "Coordenador de Qualidade", "Gerente de Qualidade",

        # Sustentabilidade / ESG
        "Analista de ESG Júnior", "Analista de ESG Pleno", "Analista de ESG Sênior",
        "Supervisor de Sustentabilidade", "Coordenador de Sustentabilidade", "Gerente de Sustentabilidade",

        # Comercial
        "Assistente Comercial", "Analista Comercial Júnior", "Analista Comercial Pleno", "Analista Comercial Sênior",
        "Supervisor Comercial", "Coordenador Comercial", "Gerente Comercial",

        # Marketing
        "Assistente de Marketing", "Analista de Marketing Júnior", "Analista de Marketing Pleno", "Analista de Marketing Sênior",
        "Supervisor de Marketing", "Coordenador de Marketing", "Gerente de Marketing",

        # Comunicação Corporativa
        "Assistente de Comunicação", "Analista de Comunicação Júnior", "Analista de Comunicação Pleno", "Analista de Comunicação Sênior",
        "Supervisor de Comunicação", "Coordenador de Comunicação", "Gerente de Comunicação",

        # Atendimento ao Cliente
        "Atendente", "Analista de Atendimento Júnior", "Analista de Atendimento Pleno", "Analista de Atendimento Sênior",
        "Supervisor de Atendimento", "Coordenador de Atendimento", "Gerente de Atendimento",

        # Compliance
        "Assistente de Compliance", "Analista de Compliance Júnior", "Analista de Compliance Pleno", "Analista de Compliance Sênior",
        "Supervisor de Compliance", "Coordenador de Compliance", "Gerente de Compliance",

        # Auditoria
        "Assistente de Auditoria", "Analista de Auditoria Júnior", "Analista de Auditoria Pleno", "Analista de Auditoria Sênior",
        "Supervisor de Auditoria", "Coordenador de Auditoria", "Gerente de Auditoria",

        # Planejamento Estratégico
        "Assistente de Planejamento", "Analista de Estratégia Júnior", "Analista de Estratégia Pleno", "Analista de Estratégia Sênior",
        "Supervisor de Planejamento", "Coordenador de Planejamento", "Gerente de Planejamento Estratégico",

        # Gestão de Projetos
        "Assistente de Projetos", "Analista de Projetos Júnior", "Analista de Projetos Pleno", "Analista de Projetos Sênior",
        "Supervisor de Projetos", "Coordenador de Projetos", "Gerente de Projetos",

        # Inteligência de Mercado
        "Assistente de Inteligência", "Analista de Inteligência Júnior", "Analista de Inteligência Pleno", "Analista de Inteligência Sênior",
        "Supervisor de Inteligência", "Coordenador de Inteligência de Mercado", "Gerente de Inteligência de Mercado",

        # Relações com Investidores
        "Assistente de RI", "Analista de RI Júnior", "Analista de RI Pleno", "Analista de RI Sênior",
        "Supervisor de Relações com Investidores", "Coordenador de Relações com Investidores", "Gerente de Relações com Investidores",

        # Comércio Exterior / Internacional
        "Assistente de Comércio Exterior", "Analista de Comércio Exterior Júnior", "Analista de Comércio Exterior Pleno", "Analista de Comércio Exterior Sênior",
        "Supervisor de Comércio Exterior", "Coordenador de Comércio Exterior", "Gerente de Comércio Exterior",

        # Compras / Suprimentos
        "Assistente de Compras", "Analista de Compras Júnior", "Analista de Compras Pleno", "Analista de Compras Sênior",
        "Supervisor de Compras", "Coordenador de Compras", "Gerente de Compras"
    ]
    dados_colaborador['cargo'] = selecionar_opcao(opcoes_cargo, "cargo")

    dados_colaborador['central_de_custo'] = str(input('\nDigite a Central de Custo: '))

    return dados_colaborador

def selecionar_opcao(opcoes, tipo_selecao):
    """
    Função auxiliar para exibir um menu numerado e permitir ao usuário selecionar uma opção.
    """
    while True:
        for i, opcao in enumerate(opcoes):
            print(f"{i + 1}. {opcao}")
        try:
            escolha = int(input(f"Digite o NÚMERO da sua escolha para {tipo_selecao}: "))
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
            else:
                print(f"Opção inválida. Por favor, digite um número entre 1 e {len(opcoes)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

# --- Execução do Código ---
if __name__ == "__main__":
    dados_pessoais_completos = coletar_informacoes_colaborador()

    print("\n" + "="*40)
    print("   INFORMAÇÕES COLETADAS")
    print("="*40)

    for chave, valor in dados_pessoais_completos.items():
        nome_campo = chave.replace('_', ' ').capitalize()
        print(f"{nome_campo}: {valor}")

    print("="*40)
    print("Coleta de dados finalizada. Os dados estão armazenados.")
