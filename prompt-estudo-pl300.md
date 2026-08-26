# Prompt: Plano de Estudos PL-300 com Dados Fictícios (MySQL/Excel + Power BI Desktop)

Copie e cole o texto abaixo em uma conversa (comigo ou com outra IA) para gerar o plano completo.

---

## PROMPT

Você é um instrutor especialista em Power BI e na certificação **PL-300 (Microsoft Power BI Data Analyst Associate)**. Quero um plano de estudos prático, guiado por um projeto único de ponta a ponta, cobrindo todos os tópicos oficiais do exame PL-300:

1. Preparar os dados (Power Query: conectar, transformar, limpar, mesclar, anexar, modelar tipos de dados)
2. Modelar os dados (relacionamentos, modelo estrela, DAX, medidas, colunas calculadas, hierarquias, segurança em nível de linha)
3. Visualizar e analisar os dados (relatórios, KPIs, gráficos, formatação condicional, drill-through, bookmarks)
4. Implantar e manter ativos (Power BI Service, workspaces, atualização de dados, compartilhamento)

### Meus recursos disponíveis
- Banco de dados **MySQL local**
- **Excel**
- **Power BI Desktop**

### O que preciso que você monte

**1. Base de dados fictícia para treino**
- Modele um cenário de negócio realista (ex.: varejo, vendas B2B, ou e-commerce) com volume suficiente para praticar performance (mínimo ~50.000 linhas na tabela fato).
- Desenhe um esquema em **modelo estrela**: 1 tabela fato (ex.: Vendas) + tabelas dimensão (Clientes, Produtos, Data/Calendário, Vendedores, Região/Loja).
- Gere os scripts SQL (CREATE TABLE + INSERT ou stored procedure de geração massiva) para popular no MySQL, **e** uma versão alternativa em Excel (planilhas separadas por tabela), caso eu prefira não usar o banco.
- Inclua "sujeira" proposital nos dados (nulos, duplicatas, formatos inconsistentes de data/texto, outliers) para eu praticar limpeza no Power Query — isso é essencial para o exame.
- Inclua uma tabela calendário completa (com colunas de ano, mês, trimestre, dia da semana, etc.) para eu praticar Time Intelligence em DAX.

**2. Instruções de importação no Power BI Desktop**
- Passo a passo de como conectar ao MySQL a partir do Power BI (driver necessário, string de conexão, importação vs. DirectQuery).
- Passo a passo de como importar as planilhas Excel equivalentes.
- Orientações de boas práticas no Power Query: nomear consultas, organizar em pastas, aplicar tipos de dados corretos, criar parâmetros.

**3. Roteiro de exercícios progressivos**
- Exercícios de Power Query (transformações básicas → avançadas: mesclar consultas, funções M, colunas condicionais, pivotar/despivotar).
- Exercícios de modelagem (criar relacionamentos, resolver relacionamento muitos-para-muitos, tabelas de papel duplo/role-playing dimension como calendário).
- Exercícios de DAX progressivos: medidas básicas (SUM, COUNT) → CALCULATE com filtros → Time Intelligence (YTD, MoM, YoY) → variáveis → funções iterativas (SUMX, RANKX) → medidas de % e comparação.

**4. Relatórios de exemplo com KPIs**
- Sugira 2-3 relatórios completos que eu deva construir, cada um com:
  - Objetivo de negócio do relatório
  - KPIs específicos (ex.: Receita Total, Ticket Médio, Taxa de Crescimento MoM, Top N Produtos, Margem %)
  - Visuais recomendados para cada KPI (cartão, gráfico de linha, matriz, mapa, etc.)
  - Uso de segmentações (slicers), drill-through e bookmarks
- Inclua pelo menos um exercício de Row-Level Security (RLS) usando a base gerada.

**5. Checklist final de revisão PL-300**
- Liste os tópicos oficiais do exame e marque quais foram cobertos pelo projeto, para eu identificar lacunas antes da prova.

Formate a resposta em etapas numeradas e sequenciais, para eu seguir como um curso auto-guiado.

---

## Como usar
1. Cole o prompt acima em uma nova conversa.
2. Peça primeiro os scripts SQL/Excel da base de dados.
3. Depois peça, em mensagens separadas, cada etapa (importação → Power Query → modelagem/DAX → relatórios).
