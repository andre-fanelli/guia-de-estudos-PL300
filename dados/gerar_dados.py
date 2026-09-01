import csv
import random
import datetime
import os

random.seed(42)

# Define o diretório de saída como a mesma pasta onde o script está localizado
output_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(output_dir, exist_ok=True)

# 1. LOJAS
lojas_data = [
    (1, "Loja Centro SP", "São Paulo", "SP", "Sudeste", "Loja Física"),
    (2, "Loja Paulista", "São Paulo", "SP", "Sudeste", "Loja Física"),
    (3, "Loja Campinas", "Campinas", "SP", "Sudeste", "Loja Física"),
    (4, "Loja Copacabana", "Rio de Janeiro", "RJ", "Sudeste", "Loja Física"),
    (5, "Loja Barra", "Rio de Janeiro", "RJ", "Sudeste", "Loja Física"),
    (6, "Loja Savassi", "Belo Horizonte", "MG", "Sudeste", "Loja Física"),
    (7, "Loja Curitiba Batel", "Curitiba", "PR", "Sul", "Loja Física"),
    (8, "Loja Porto Alegre", "Porto Alegre", "RS", "Sul", "Loja Física"),
    (9, "Loja Florianópolis", "Florianópolis", "SC", "Sul", "Loja Física"),
    (10, "Loja Salvador Barra", "Salvador", "BA", "Nordeste", "Loja Física"),
    (11, "Loja Recife Boa Viagem", "Recife", "PE", "Nordeste", "Loja Física"),
    (12, "Loja Fortaleza Aldeota", "Fortaleza", "CE", "Nordeste", "Loja Física"),
    (13, "Loja Brasília Asa Sul", "Brasília", "DF", "Centro-Oeste", "Loja Física"),
    (14, "Loja Goiânia Bueno", "Goiânia", "GO", "Centro-Oeste", "Loja Física"),
    (15, "E-Commerce Brasil", "São Paulo", "SP", "Nacional", "Online"),
]

# 2. VENDEDORES (com email para RLS dinâmico)
vendedores_data = [
    (1, "Carlos Drummond", "carlos.drummond@empresa.com.br", 1, "Vendedor Senior"),
    (2, "Mariana Rios", "mariana.rios@empresa.com.br", 1, "Vendedor Pleno"),
    (3, "Roberto Shinyashiki", "roberto.s@empresa.com.br", 2, "Vendedor Senior"),
    (4, "Fernanda Montenegro", "fernanda.m@empresa.com.br", 2, "Vendedor Pleno"),
    (5, "Lucas Lucco", "lucas.lucco@empresa.com.br", 3, "Vendedor Junior"),
    (6, "Camila Pitanga", "camila.p@empresa.com.br", 4, "Vendedor Senior"),
    (7, "Rodrigo Santoro", "rodrigo.s@empresa.com.br", 4, "Vendedor Pleno"),
    (8, "Juliana Paes", "juliana.p@empresa.com.br", 5, "Vendedor Senior"),
    (9, "Cauã Reymond", "caua.r@empresa.com.br", 6, "Vendedor Pleno"),
    (10, "Leticia Sabatella", "leticia.s@empresa.com.br", 6, "Vendedor Senior"),
    (11, "Wagner Moura", "wagner.m@empresa.com.br", 7, "Vendedor Senior"),
    (12, "Alice Braga", "alice.b@empresa.com.br", 7, "Vendedor Pleno"),
    (13, "Selton Mello", "selton.m@empresa.com.br", 8, "Vendedor Senior"),
    (14, "Deborah Secco", "deborah.s@empresa.com.br", 8, "Vendedor Junior"),
    (15, "Bruno Gagliasso", "bruno.g@empresa.com.br", 9, "Vendedor Pleno"),
    (16, "Lazaro Ramos", "lazaro.r@empresa.com.br", 10, "Vendedor Senior"),
    (17, "Tais Araujo", "tais.a@empresa.com.br", 10, "Vendedor Senior"),
    (18, "Fabio Assunção", "fabio.a@empresa.com.br", 11, "Vendedor Pleno"),
    (19, "Grazi Massafera", "grazi.m@empresa.com.br", 12, "Vendedor Pleno"),
    (20, "Alexandre Nero", "alexandre.n@empresa.com.br", 13, "Vendedor Senior"),
    (21, "Paolla Oliveira", "paolla.o@empresa.com.br", 14, "Vendedor Pleno"),
    (22, "Canal Digital 1", "digital1@empresa.com.br", 15, "Consultor Digital"),
    (23, "Canal Digital 2", "digital2@empresa.com.br", 15, "Consultor Digital"),
    (24, "Canal Digital 3", "digital3@empresa.com.br", 15, "Consultor Digital"),
    (25, "Canal Marketplace", "marketplace@empresa.com.br", 15, "Gestor Marketplace"),
]

# 3. PRODUTOS (Categorias, Subcategorias, Preço Custo, Preço Venda Sugerido)
produtos_base = [
    # Categoria: Tecnologia
    ("Notebook Pro 15", "Tecnologia", "Computadores", 2800.0, 4499.0),
    ("Notebook Ultra Slim 13", "Tecnologia", "Computadores", 2200.0, 3599.0),
    ("Desktop Gamer Core i7", "Tecnologia", "Computadores", 3500.0, 5799.0),
    ("Monitor Ultrawide 29", "Tecnologia", "Monitores", 750.0, 1299.0),
    ("Monitor Gamer 144Hz 24", "Tecnologia", "Monitores", 620.0, 1099.0),
    ("Teclado Mecânico RGB", "Tecnologia", "Acessórios", 110.0, 249.9),
    ("Mouse Sem Fio Ergonômico", "Tecnologia", "Acessórios", 55.0, 139.9),
    ("Headset Gamer 7.1", "Tecnologia", "Áudio", 140.0, 319.9),
    ("Smartphone Galaxy Note", "Tecnologia", "Smartphones", 1900.0, 3299.0),
    ("Smartphone Pro Max", "Tecnologia", "Smartphones", 3800.0, 6199.0),
    ("Tablet 10 Polegadas", "Tecnologia", "Tablets", 850.0, 1599.0),
    ("Smartwatch Fit Pro", "Tecnologia", "Wearables", 220.0, 499.0),
    
    # Categoria: Eletrodomésticos
    ("Geladeira Frost Free 450L", "Eletrodomésticos", "Refrigeração", 1800.0, 3199.0),
    ("Geladeira Side by Side 520L", "Eletrodomésticos", "Refrigeração", 3200.0, 5499.0),
    ("Micro-ondas 32L Inox", "Eletrodomésticos", "Cozinha", 310.0, 599.0),
    ("Fritadeira Air Fryer 4L", "Eletrodomésticos", "Cozinha", 160.0, 349.9),
    ("Cafeteira Expresso Automática", "Eletrodomésticos", "Cozinha", 290.0, 589.0),
    ("Lava e Seca 11kg", "Eletrodomésticos", "Lavanderia", 2100.0, 3699.0),
    ("Aspirador Robô Inteligente", "Eletrodomésticos", "Limpeza", 580.0, 1199.0),
    ("Ar-Condicionado Inverter 12000 BTUs", "Eletrodomésticos", "Climatização", 1100.0, 2199.0),
    
    # Categoria: Móveis & Decoração
    ("Cadeira de Escritório Ergonômica", "Móveis", "Escritório", 380.0, 799.0),
    ("Mesa Gamer em L", "Móveis", "Escritório", 290.0, 649.0),
    ("Sofá 3 Lugares Retrátil", "Móveis", "Sala de Estar", 950.0, 1899.0),
    ("Poltrona Reclinável Veludo", "Móveis", "Sala de Estar", 420.0, 899.0),
    ("Estante para Livros 5 Prateleiras", "Móveis", "Sala de Estar", 180.0, 399.0),
    ("Mesa de Jantar 6 Lugares", "Móveis", "Sala de Jantar", 700.0, 1499.0),
    ("Guarda-Roupa Casal 6 Portas", "Móveis", "Quarto", 890.0, 1799.0),
    ("Cama Box Queen com Colchão", "Móveis", "Quarto", 1100.0, 2299.0),

    # Categoria: Casa & Utilidades
    ("Conjunto Panelas Antiaderente 5 Pçs", "Casa", "Cozinha", 140.0, 299.0),
    ("Faqueiro Inox 42 Peças", "Casa", "Cozinha", 85.0, 189.0),
    ("Aparelho de Jantar Porcelana 20 Pçs", "Casa", "Mesa", 160.0, 369.0),
    ("Jogo de Toalhas Banho 4 Pçs Algodão", "Casa", "Banho", 65.0, 149.0),
    ("Kit Edredom Casal Dupla Face", "Casa", "Cama", 110.0, 239.0),
    ("Luminária de Mesa LED Articulável", "Casa", "Iluminação", 40.0, 99.0),
]

produtos_data = []
for i, prod in enumerate(produtos_base, 1):
    produtos_data.append((i, prod[0], prod[1], prod[2], prod[3], prod[4]))

# 4. CLIENTES (com propositais sujeiras controladas)
primeiros_nomes = ["Lucas", "Gabriel", "Mateus", "Rodrigo", "Juliana", "Mariana", "Camila", "Fernanda", "Beatriz", "Larissa", "Felipe", "Gustavo", "Thiago", "Pedro", "Rafael", "Ana", "Carla", "Patricia", "Bruna", "Aline", "Marcos", "Eduardo", "Diego", "Leonardo", "Vinicius", "Renata", "Jessica", "Vanessa", "Daniela", "Priscila"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado", "Mendes", "Freitas"]
cidades_estados = [
    ("São Paulo", "SP", "Sudeste"), ("Campinas", "SP", "Sudeste"), ("Santos", "SP", "Sudeste"),
    ("Rio de Janeiro", "RJ", "Sudeste"), ("Niterói", "RJ", "Sudeste"),
    ("Belo Horizonte", "MG", "Sudeste"), ("Uberlândia", "MG", "Sudeste"),
    ("Curitiba", "PR", "Sul"), ("Londrina", "PR", "Sul"),
    ("Porto Alegre", "RS", "Sul"), ("Caxias do Sul", "RS", "Sul"),
    ("Florianópolis", "SC", "Sul"), ("Joinville", "SC", "Sul"),
    ("Salvador", "BA", "Nordeste"), ("Feira de Santana", "BA", "Nordeste"),
    ("Recife", "PE", "Nordeste"), ("Fortaleza", "CE", "Nordeste"),
    ("Brasília", "DF", "Centro-Oeste"), ("Goiânia", "GO", "Centro-Oeste")
]
generos = ["M", "F"]
segmentos = ["Consumidor Final", "Corporativo", "Pequenas Empresas"]

clientes_data = []
num_clientes = 1200
for cid in range(1, num_clientes + 1):
    fn = random.choice(primeiros_nomes)
    sn = random.choice(sobrenomes)
    nome = f"{fn} {sn}"
    # Sujeira proposital em ~5% dos clientes: espaços extras ou maiúsculas
    r_dirt = random.random()
    if r_dirt < 0.03:
        nome = f"  {fn.upper()}  {sn.lower()} "
    elif r_dirt < 0.06:
        nome = f"{fn.lower()} {sn.lower()}"
    
    cid_est = random.choice(cidades_estados)
    cidade = cid_est[0]
    estado = cid_est[1]
    regiao = cid_est[2]
    
    genero = random.choice(generos)
    segmento = random.choice(segmentos)
    idade = random.randint(18, 72)
    email = f"{fn.lower()}.{sn.lower()}{cid}@exemplo.com.br".replace(" ", "")
    renda_estimada = round(random.uniform(2200.0, 18500.0), 2)
    
    clientes_data.append((cid, nome, email, genero, idade, segmento, cidade, estado, regiao, renda_estimada))

# 5. CALENDÁRIO (2023-01-01 a 2025-12-31)
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2025, 12, 31)
curr = start_date
calendario_data = []
dias_semana_pt = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
meses_pt = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
meses_curto_pt = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

while curr <= end_date:
    d_str = curr.strftime("%Y-%m-%d")
    ano = curr.year
    mes_num = curr.month
    mes_nome = meses_pt[mes_num - 1]
    mes_curto = meses_curto_pt[mes_num - 1]
    ano_mes = f"{ano}-{mes_num:02d}"
    ano_mes_num = ano * 100 + mes_num
    trimestre = (mes_num - 1) // 3 + 1
    trimestre_nome = f"T{trimestre}"
    ano_trimestre = f"{ano}-T{trimestre}"
    dia_mes = curr.day
    dia_semana_num = curr.weekday() + 1 # 1=Segunda ... 7=Domingo
    dia_semana_nome = dias_semana_pt[curr.weekday()]
    eh_fim_semana = "Sim" if dia_semana_num in [6, 7] else "Não"
    semana_ano = int(curr.strftime("%W")) + 1
    
    calendario_data.append((
        d_str, ano, mes_num, mes_nome, mes_curto, ano_mes, ano_mes_num,
        trimestre, trimestre_nome, ano_trimestre, dia_mes, dia_semana_num,
        dia_semana_nome, eh_fim_semana, semana_ano
    ))
    curr += datetime.timedelta(days=1)

# 6. FATO VENDAS (Gerar ~65.000 linhas)
# Com sazonalidade: Black Friday (Nov), Natal (Dez), Dia das Mães (Mai) e crescimento anual
fato_vendas = []
venda_id = 1
total_days = (end_date - start_date).days + 1

status_list = ["Entregue", "Entregue", "Entregue", "Entregue", "Em Trânsito", "Cancelado", "Devolvido"]
meios_pagamento = ["Cartão de Crédito", "PIX", "Boleto Bancário", "Cartão de Débito"]

curr = start_date
while curr <= end_date:
    ano = curr.year
    mes = curr.month
    
    # Fatores sazonais
    mult = 1.0
    if ano == 2023:
        mult *= 1.0
    elif ano == 2024:
        mult *= 1.2
    elif ano == 2025:
        mult *= 1.45
        
    if mes == 11: # Black Friday
        mult *= 1.8
    elif mes == 12: # Natal
        mult *= 2.1
    elif mes == 5: # Mães
        mult *= 1.3
    elif mes == 1: # Ressaca Jan
        mult *= 0.75
        
    # Número de vendas no dia
    base_vendas = int(random.gauss(55, 12) * mult)
    base_vendas = max(15, base_vendas)
    
    for _ in range(base_vendas):
        d_venda_str = curr.strftime("%Y-%m-%d")
        
        # Data envio (role-playing dimension) entre 1 e 7 dias depois
        d_envio = curr + datetime.timedelta(days=random.randint(1, 6))
        d_envio_str = d_envio.strftime("%Y-%m-%d")
        
        id_cliente = random.randint(1, num_clientes)
        prod = random.choice(produtos_data)
        id_produto = prod[0]
        custo_unit = prod[4]
        preco_unit_tabela = prod[5]
        
        # Loja e vendedor
        id_vendedor = random.randint(1, len(vendedores_data))
        vendedor_info = vendedores_data[id_vendedor - 1]
        id_loja = vendedor_info[3]
        
        qtd = random.choices([1, 2, 3, 4, 5, 8, 10], weights=[70, 18, 6, 3, 2, 0.5, 0.5])[0]
        
        # Desconto de 0% a 20%
        desconto_pct = random.choices([0.0, 0.05, 0.10, 0.15, 0.20], weights=[50, 20, 15, 10, 5])[0]
        
        # Preço praticado com leve variação
        preco_praticado = preco_unit_tabela
        
        # Sujeiras propositais:
        # 1. Nulo em desconto_pct em ~2% dos casos
        # 2. Status com inconsistência em ~3% dos casos (minúscula / nulo)
        # 3. Preço praticado zero em raros casos
        dirt_roll = random.random()
        desconto_val = round(preco_praticado * qtd * desconto_pct, 2)
        valor_bruto = round(preco_praticado * qtd, 2)
        valor_liquido = round(valor_bruto - desconto_val, 2)
        custo_total = round(custo_unit * qtd, 2)
        
        status = random.choice(status_list)
        meio_pgto = random.choice(meios_pagamento)
        
        if dirt_roll < 0.015:
            desconto_str = ""  # para simular null no CSV
        else:
            desconto_str = str(desconto_pct)
            
        if dirt_roll < 0.01:
            status_limpo = status.lower() # inconsistência
        elif dirt_roll < 0.02:
            status_limpo = "" # nulo
        else:
            status_limpo = status
            
        fato_vendas.append((
            venda_id, d_venda_str, d_envio_str, id_cliente, id_produto,
            id_vendedor, id_loja, qtd, preco_praticado, desconto_str,
            desconto_val, valor_bruto, valor_liquido, custo_total,
            status_limpo, meio_pgto
        ))
        venda_id += 1
        
    curr += datetime.timedelta(days=1)

print(f"Total de vendas geradas: {len(fato_vendas)}")

# 7. METAS MENSAIS (Fato Metas - granularidade Ano-Mes x Vendedor)
fato_metas = []
meta_id = 1
for v in vendedores_data:
    v_id = v[0]
    for ano in [2023, 2024, 2025]:
        for mes in range(1, 13):
            d_meta = f"{ano}-{mes:02d}-01"
            base_meta = 70000.0 if "Senior" in v[4] else (50000.0 if "Pleno" in v[4] else 35000.0)
            if v_id in [22, 23, 24, 25]: # Digital / Marketplace
                base_meta *= 2.5
            if mes in [11, 12]:
                base_meta *= 1.8
            meta_val = round(base_meta * (1.0 + (ano - 2023) * 0.2) * random.uniform(0.9, 1.15), 2)
            fato_metas.append((meta_id, d_meta, v_id, meta_val))
            meta_id += 1

print(f"Total de metas geradas: {len(fato_metas)}")

# ----------------- GRAVAR CSVs -----------------
def salvar_csv(nome_arquivo, cabecalho, dados):
    caminho = os.path.join(output_dir, nome_arquivo)
    with open(caminho, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(cabecalho)
        writer.writerows(dados)
    print(f"Arquivo CSV salvo: {caminho}")

salvar_csv("dim_lojas.csv", ["id_loja", "nome_loja", "cidade", "estado", "regiao", "tipo_canal"], lojas_data)
salvar_csv("dim_vendedores.csv", ["id_vendedor", "nome_vendedor", "email_vendedor", "id_loja", "cargo"], vendedores_data)
salvar_csv("dim_produtos.csv", ["id_produto", "nome_produto", "categoria", "subcategoria", "preco_custo", "preco_venda_sugerido"], produtos_data)
salvar_csv("dim_clientes.csv", ["id_cliente", "nome_cliente", "email_cliente", "genero", "idade", "segmento", "cidade", "estado", "regiao", "renda_estimada"], clientes_data)
salvar_csv("dim_calendario.csv", ["data", "ano", "num_mes", "nome_mes", "mes_curto", "ano_mes", "ano_mes_num", "num_trimestre", "nome_trimestre", "ano_trimestre", "dia_mes", "dia_semana_num", "dia_semana_nome", "eh_fim_semana", "semana_ano"], calendario_data)
salvar_csv("fato_metas.csv", ["id_meta", "data_meta", "id_vendedor", "valor_meta"], fato_metas)
salvar_csv("fato_vendas.csv", ["id_venda", "data_venda", "data_envio", "id_cliente", "id_produto", "id_vendedor", "id_loja", "quantidade", "preco_unitario", "desconto_pct", "desconto_valor", "valor_bruto", "valor_liquido", "custo_total", "status_entrega", "meio_pagamento"], fato_vendas)

# ----------------- GERAR SCRIPT SQL PARA MYSQL -----------------
sql_file_path = os.path.join(output_dir, "schema_pl300_varejo.sql")
with open(sql_file_path, mode="w", encoding="utf-8") as f:
    f.write("""-- =============================================================
-- BANCO DE DADOS: pl300_varejo (Cenário Varejo Omnichannel PL-300)
-- =============================================================

CREATE DATABASE IF NOT EXISTS pl300_varejo
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE pl300_varejo;

-- 1. DIMENSÃO LOJAS
DROP TABLE IF EXISTS fato_vendas;
DROP TABLE IF EXISTS fato_metas;
DROP TABLE IF EXISTS dim_vendedores;
DROP TABLE IF EXISTS dim_lojas;
DROP TABLE IF EXISTS dim_produtos;
DROP TABLE IF EXISTS dim_clientes;
DROP TABLE IF EXISTS dim_calendario;

CREATE TABLE dim_lojas (
    id_loja INT PRIMARY KEY,
    nome_loja VARCHAR(100) NOT NULL,
    cidade VARCHAR(80) NOT NULL,
    estado CHAR(2) NOT NULL,
    regiao VARCHAR(30) NOT NULL,
    tipo_canal VARCHAR(30) NOT NULL
);

-- 2. DIMENSÃO VENDEDORES
CREATE TABLE dim_vendedores (
    id_vendedor INT PRIMARY KEY,
    nome_vendedor VARCHAR(120) NOT NULL,
    email_vendedor VARCHAR(150) NOT NULL,
    id_loja INT,
    cargo VARCHAR(60),
    FOREIGN KEY (id_loja) REFERENCES dim_lojas(id_loja)
);

-- 3. DIMENSÃO PRODUTOS
CREATE TABLE dim_produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(150) NOT NULL,
    categoria VARCHAR(60) NOT NULL,
    subcategoria VARCHAR(60) NOT NULL,
    preco_custo DECIMAL(10,2) NOT NULL,
    preco_venda_sugerido DECIMAL(10,2) NOT NULL
);

-- 4. DIMENSÃO CLIENTES
CREATE TABLE dim_clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR(150) NOT NULL,
    email_cliente VARCHAR(150),
    genero CHAR(1),
    idade INT,
    segmento VARCHAR(50),
    cidade VARCHAR(80),
    estado CHAR(2),
    regiao VARCHAR(30),
    renda_estimada DECIMAL(10,2)
);

-- 5. DIMENSÃO CALENDÁRIO
CREATE TABLE dim_calendario (
    data DATE PRIMARY KEY,
    ano INT NOT NULL,
    num_mes INT NOT NULL,
    nome_mes VARCHAR(20) NOT NULL,
    mes_curto CHAR(3) NOT NULL,
    ano_mes CHAR(7) NOT NULL,
    ano_mes_num INT NOT NULL,
    num_trimestre INT NOT NULL,
    nome_trimestre CHAR(2) NOT NULL,
    ano_trimestre CHAR(7) NOT NULL,
    dia_mes INT NOT NULL,
    dia_semana_num INT NOT NULL,
    dia_semana_nome VARCHAR(20) NOT NULL,
    eh_fim_semana VARCHAR(3) NOT NULL,
    semana_ano INT NOT NULL
);

-- 6. FATO METAS
CREATE TABLE fato_metas (
    id_meta INT PRIMARY KEY,
    data_meta DATE NOT NULL,
    id_vendedor INT NOT NULL,
    valor_meta DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (id_vendedor) REFERENCES dim_vendedores(id_vendedor)
);

-- 7. FATO VENDAS
CREATE TABLE fato_vendas (
    id_venda INT PRIMARY KEY,
    data_venda DATE NOT NULL,
    data_envio DATE,
    id_cliente INT NOT NULL,
    id_produto INT NOT NULL,
    id_vendedor INT NOT NULL,
    id_loja INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    desconto_pct DECIMAL(5,2),
    desconto_valor DECIMAL(10,2),
    valor_bruto DECIMAL(12,2) NOT NULL,
    valor_liquido DECIMAL(12,2) NOT NULL,
    custo_total DECIMAL(12,2) NOT NULL,
    status_entrega VARCHAR(30),
    meio_pagamento VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES dim_clientes(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES dim_produtos(id_produto),
    FOREIGN KEY (id_vendedor) REFERENCES dim_vendedores(id_vendedor),
    FOREIGN KEY (id_loja) REFERENCES dim_lojas(id_loja)
);

-- Inserindo Dim Lojas
""")
    for row in lojas_data:
        f.write(f"INSERT INTO dim_lojas VALUES ({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}');\n")

    f.write("\n-- Inserindo Dim Vendedores\n")
    for row in vendedores_data:
        f.write(f"INSERT INTO dim_vendedores VALUES ({row[0]}, '{row[1]}', '{row[2]}', {row[3]}, '{row[4]}');\n")

    f.write("\n-- Inserindo Dim Produtos\n")
    for row in produtos_data:
        f.write(f"INSERT INTO dim_produtos VALUES ({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', {row[4]}, {row[5]});\n")

    f.write("\n-- Inserindo Dim Clientes (em lotes)\n")
    batch_size = 200
    for i in range(0, len(clientes_data), batch_size):
        batch = clientes_data[i:i+batch_size]
        f.write("INSERT INTO dim_clientes VALUES\n")
        lines = []
        for c in batch:
            nome_esc = c[1].replace("'", "''")
            email_esc = c[2].replace("'", "''")
            lines.append(f"({c[0]}, '{nome_esc}', '{email_esc}', '{c[3]}', {c[4]}, '{c[5]}', '{c[6]}', '{c[7]}', '{c[8]}', {c[9]})")
        f.write(",\n".join(lines) + ";\n")

    f.write("\n-- Inserindo Dim Calendario (em lotes)\n")
    for i in range(0, len(calendario_data), batch_size):
        batch = calendario_data[i:i+batch_size]
        f.write("INSERT INTO dim_calendario VALUES\n")
        lines = []
        for d in batch:
            lines.append(f"('{d[0]}', {d[1]}, {d[2]}, '{d[3]}', '{d[4]}', '{d[5]}', {d[6]}, {d[7]}, '{d[8]}', '{d[9]}', {d[10]}, {d[11]}, '{d[12]}', '{d[13]}', {d[14]})")
        f.write(",\n".join(lines) + ";\n")

    f.write("\n-- Inserindo Fato Metas (em lotes)\n")
    for i in range(0, len(fato_metas), batch_size):
        batch = fato_metas[i:i+batch_size]
        f.write("INSERT INTO fato_metas VALUES\n")
        lines = []
        for m in batch:
            lines.append(f"({m[0]}, '{m[1]}', {m[2]}, {m[3]})")
        f.write(",\n".join(lines) + ";\n")

    f.write("\n-- Inserindo Fato Vendas (em lotes)\n")
    batch_size_vendas = 500
    for i in range(0, len(fato_vendas), batch_size_vendas):
        batch = fato_vendas[i:i+batch_size_vendas]
        f.write("INSERT INTO fato_vendas VALUES\n")
        lines = []
        for v in batch:
            desc_pct_sql = v[9] if v[9] != "" else "NULL"
            status_sql = f"'{v[14]}'" if v[14] != "" else "NULL"
            lines.append(f"({v[0]}, '{v[1]}', '{v[2]}', {v[3]}, {v[4]}, {v[5]}, {v[6]}, {v[7]}, {v[8]}, {desc_pct_sql}, {v[10]}, {v[11]}, {v[12]}, {v[13]}, {status_sql}, '{v[15]}')")
        f.write(",\n".join(lines) + ";\n")

print(f"Script SQL gerado com sucesso em: {sql_file_path}")
