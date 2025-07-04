# 📊 Modelagem Preditiva para Projeção Trimestral de Vendas
### Autora: Flávia Costa
### Projeto Acadêmico | Previsão de Vendas | Séries Temporais | Machine Learning
## 📝 Descrição do Projeto
Este projeto tem como objetivo desenvolver e comparar modelos preditivos para estimar o volume de vendas trimestral de uma empresa multinacional do setor industrial. Aplicando técnicas de Ciência de Dados, séries temporais e algoritmos de aprendizado de máquina, busca-se fornecer projeções de vendas mais confiáveis que apoiem o planejamento estratégico, comercial e logístico da organização.

O estudo explora modelos tradicionais de séries temporais, como ARIMA e SARIMAX, além de abordagens baseadas em aprendizado de máquina, como o Support Vector Regression (SVR), incorporando variáveis exógenas financeiras.

## 📖 Introdução
A previsão de vendas é uma atividade estratégica fundamental para a gestão eficiente de recursos, definição de metas, planejamento da produção e suporte à tomada de decisões comerciais. Em um ambiente cada vez mais competitivo e orientado por dados, a capacidade de antecipar o comportamento do mercado com base em informações históricas representa um diferencial crucial para as organizações. Nesse contexto, os modelos de séries temporais assumem papel central, ao permitirem a identificação de padrões sazonais, tendências e ciclos que influenciam diretamente os níveis de vendas ao longo do tempo.

Observa-se abaixo, por exemplo, que após 2019 houve uma queda acentuada nas vendas em decorrência da pandemia da COVID-19, seguida de oscilações expressivas, o que gerou um cenário de alta incerteza.
![Evolução de vendas](https://github.com/user-attachments/assets/de617eeb-6e02-4eaf-9b3a-c7e06938ea36)

### 📝 Descrição do Problema
A partir da análise dos dados de pedidos e faturamento, identificou-se a necessidade de desenvolver um método robusto de previsão de vendas, principalmente diante do cenário de alta volatilidade do mercado.

Um dos grandes desafios está relacionado a eventos de grande porte que ocorrem a cada dois anos no segundo semestre. Esses eventos, apesar de serem previstos no calendário, geram incertezas no comportamento de compra dos clientes, impactando diretamente o volume de vendas.

Nesse contexto, contar com modelos preditivos orientados por dados torna-se essencial para mitigar riscos e antecipar possíveis problemas relacionados à queda de vendas, custos operacionais e aquisição de materiais. A implementação de técnicas de previsão proporciona maior segurança ao planejamento comercial, logístico e financeiro da empresa.

### 🎯 Objetivo
O principal objetivo é desenvolver um modelo de previsão capaz de projetar o volume de vendas mensais e trimestrais de forma aproximada, com foco inicial nas quantidades comercializadas, visando estimar a receita em dólar e apoiar o planejamento estratégico das áreas de vendas, finanças e logística.

### 💡 Justificativa
A previsão de vendas com maior precisão é essencial para subsidiar decisões assertivas relacionadas à aquisição de materiais, planejamento da produção, definição de ações de marketing e otimização de custos logísticos e operacionais. Segundo Chopra & Meindl (2016), previsões de demanda confiáveis são fundamentais para o alinhamento eficiente entre oferta e demanda, permitindo às organizações melhorar seu desempenho financeiro e operacional.
![livro chopra e meindi](https://github.com/user-attachments/assets/ef802c43-3de7-406a-8ae4-ddbacb5a94db)

### 🚫 Escopo negativo 

Inicialmente, foi avaliada a possibilidade de utilizar a base de dados contendo os registros de pedidos realizados. Essa base, em teoria, seria ideal para antecipar o volume de novos pedidos para os meses seguintes, considerando que a empresa trabalha sob demanda, ou seja, os pedidos confirmados servem como gatilho para o planejamento de produção e faturamento. Dessa forma, o uso dessa base permitiria testar o impacto de variáveis exógenas, como indicadores econômicos ou eventos de mercado, capazes de capturar variações externas ao ambiente interno da empresa.
No entanto, essa abordagem mostrou-se inviável, pois a base de pedidos apresentou limitações significativas: trata-se de um sistema alimentado manualmente, com baixa padronização e histórico insuficiente, o que compromete a integridade dos dados e inviabiliza análises robustas.
É importante destacar que na base trabalhada para este projeto, as limitações são semelhantes, mas de uma maneira geral, por se tratar de uma base de faturamento, encontrei alternativa realizando validações e tratamento dos dados.

<img width="259" alt="Captura de Tela 2025-07-04 às 14 54 44" src="https://github.com/user-attachments/assets/271a761a-d5b1-4afb-946e-6580e16ada6c" />

## 📚 Fundamentação Teórica

### 🏢 Área do Negócio
O presente projeto está inserido no contexto do setor industrial, mais especificamente em uma empresa multinacional dedicada à fabricação e comercialização de produtos para o mercado B2B (business-to-business). 

### ⛏️ Mineração de Dados
Aplicação de métodos e técnicas para identificar padrões, tendências e relações ocultas em conjuntos de dados.

📈 Com o gráfico abaixo, é possível analisar os dados reais, a tendência das vendas, a sazonalidade e os resíduos. 
Um bom ponto de partida para a modelagem dos dados.
![Decomposição sazonal](https://github.com/user-attachments/assets/819e7cbd-6d2e-43c9-bf8d-7e9b017bdb57)

🔥 No mapa de calor é possível avaliar a correlação entre as variáveis numéricas e testar possíveis variáveis exógenas a serem utilizadas na modelagem preditiva
![Heatmap](https://github.com/user-attachments/assets/749f605f-c594-4a01-89cf-8ef36b1008a6)


### 🔗 Trabalhos Relacionados

## 🛠️ Materiais e Métodos

### 🗄️ Descrição da Base de Dados

### 📊 Análise Descritiva dos Dados

### ⚙️ Pré-processamento dos Dados

### 🧪 Metodologia Experimental

## 🧐 Análise e Discussão dos Resultados

### 📈 Resultados

### 💭 Discussão

## 🚀 Conclusões e Trabalhos Futuros

