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

#### 📝  Angelo, C. F., Fouto, N. M. M. D., & Luppe, M. R. (2010). 
Previsão de vendas no varejo brasileiro: uma avaliação a partir de diferentes técnicas quantitativas. 
Revista Eletrônica de Administração, Universidade Federal do Rio Grande do Sul. ISSN 1413-2311.

#### 📝  Silva, G. J., & Piratelli, C. L. (s/d). 
Previsão de vendas por séries temporais em uma empresa de nutrição para animais domésticos. Universidade de Araraquara - UNIARA.

## 🛠️ Materiais e Métodos

### 🗄️ Descrição da Base de Dados
• A base de dados utilizada encontra-se no formato .xlsx (Microsoft Excel)  
• Período analisado 2019 a maio de 2025  
• Granularidade mensal  
• 72 mil registros aprox com 55 features  
• Features utilizadas: Ano, mês, quantidade e comissão  

### 📊 Análise Descritiva dos Dados
Além das analises realizadas abaixo, foram considerados o gráfico de decomposição sazonal e heatmap apresentado acima. 

#### Identificação e Análise dos Outliers
![Detecção de outliers](https://github.com/user-attachments/assets/573da1b4-eada-46f2-afeb-db8a2549ae84)

#### Distribuição de Vendas
![Distribuição de vendas](https://github.com/user-attachments/assets/5902a809-7693-4c5f-b5af-9151f8b148a6)

#### Teste de Dickey Fuller

• Estatística ADF: -5.5592630877642994  
• p-valor: 1.555205009293298e-06  
• Usou: 0 lags  
• Número de observações: 76  

**Valores Críticos:**  
  • 1%: -3.5195  
  • 5%: -2.9004  
  • 10%: -2.5875  

##### A série é estacionária (rejeita H0)

### ⚙️ Pré-processamento dos Dados
##### Todas as etapas foram realizadas na linguagem 🐍 Python  
##### Padronização dos metadados: Remoção de espaços em branco nos títulos das colunas e ajuste de nomenclaturas.  
##### Seleção de escopo: Aplicação de filtros para restringir a base ao tipo de produto em análise e à região geográfica de interesse, neste caso, o mercado doméstico (Brasil).  
##### Filtragem por faturamento: Exclusão de registros que não representavam faturamento efetivo, considerando apenas dados consolidados de vendas.  
##### Tratamento de valores ausentes: Avaliação pontual das variáveis, com aplicação de exclusão, imputação ou manutenção controlada dos dados faltantes, conforme a relevância e impacto  nas análises. Foram identificados e tratados 17 valores ausentes.  
##### Criação de variável temporal: Geração de uma coluna de data consolidada (formato ano-mês), uma vez que os dados originais estavam separados em colunas distintas.  
##### Agregação temporal: Agrupamento das vendas e das variáveis exógenas por período mensal, atendendo à granularidade estabelecida para o estudo.  
##### Divisão dos dados: Separação temporal da base em conjunto de treino (60%), validação (20%) e teste (20%), respeitando a ordem cronológica, conforme as boas práticas recomendadas por Hyndman e Athanasopoulos.  
##### Transformações: Aplicação de técnicas de normalização e padronização dos dados, além da transformação logarítmica nas variáveis exógenas, com o intuito de reduzir variância e suavizar a série temporal, conforme sugerido por Han, Kamber e Pei  

### 🧪 Metodologia Experimental
• Utilização de modelos da família ARIMA e SVR (Support Vector Regression).  
• Experimento com e sem variáveis exógenas.  
• Testes com normalização escalar e logaritmica.  
• Testes com parâmetros automáticos e manuais.  
#### Gráficos

##### Teste inicial com ARIMA - AutoRegressive Integrated Moving Average (Média Móvel Integrada Autorregressiva)
![Arima automatico](https://github.com/user-attachments/assets/2b9ad0fc-adc9-4c1f-b780-c80752424634)  

##### Teste com ARIMA utilizando parâmetros manuais
![Arima com ordem manual](https://github.com/user-attachments/assets/78137a46-4e31-4793-9adc-0103d5a78799)  

##### Teste com SARIMAX - AutoRegressive Integrated Moving Average + Sazonal e Exógena 
###### Normalização Scaled

![Sarimax scaled](https://github.com/user-attachments/assets/037f52d2-eade-41e9-8277-8332335105a5)  

![Sarimax residuos treino scaled ](https://github.com/user-attachments/assets/8e7d0048-342f-4740-ae51-fb5e02fa960f)  

![Sarimax residuos treino + validacao scaled](https://github.com/user-attachments/assets/86f4b203-d6dc-4dc8-abe6-41a01aa8c3ca)  

##### Teste com SARIMAX - AutoRegressive Integrated Moving Average + Sazonal e Exógena 
###### Normalização Logaritmica

![Sarimax log](https://github.com/user-attachments/assets/00d35ecd-6a09-49f1-81b6-03ecde02eb80)  

![Sarimax residuos treino log ](https://github.com/user-attachments/assets/dabb9c7e-e9e0-464e-b0db-29ea7c73c8a9)  

![Sarimax residuos treino + validacao log](https://github.com/user-attachments/assets/183f53c1-8024-45a3-bbfa-4bbe169379e3)  

##### Teste com SARIMAX - AutoRegressive Integrated Moving Average + Sazonal e Exógena (Utilizando R)

![Sarimax R Treino - 1 exogLog - 4-1-4](https://github.com/user-attachments/assets/d816ff78-d683-4638-90e7-913870257a9f)

![Sarimax R Teste - 1 exogLog - 4-1-4](https://github.com/user-attachments/assets/c33355a6-0cac-4614-a3b2-c039b4b84532)

<img width="863" alt="Captura de Tela 2025-07-06 às 14 13 31" src="https://github.com/user-attachments/assets/99d9ecb6-ddd3-4c29-9cd2-857afeb66f70" />


##### Teste com SVR - Support Vector Regression (SVR) - Machine learning

![svr passo 1 sem exogena](https://github.com/user-attachments/assets/b5af0e28-0882-4d36-8721-9da7a72769c1)  

![svr passo 2 sem exogena](https://github.com/user-attachments/assets/e0711257-5275-48cd-9084-64c4bbbe98a7)  

![svr passo 3 sem exogena](https://github.com/user-attachments/assets/dfc1918f-d7f2-4ca1-8a5e-edc13c8f5fb8)

![svr passo 1 com exogena](https://github.com/user-attachments/assets/9e646672-3c9f-4411-bdab-22227a7449be)

![svr passo 2 com exogena](https://github.com/user-attachments/assets/ac03409c-cc3a-4c11-b618-6bd89ad8148e)  
 
![svr passo 3 com exogena](https://github.com/user-attachments/assets/7ac3c6c2-b860-4d94-9753-3a5a07737e50)

## 🧐 Análise e Discussão dos Resultados

### 📈 Resultados
<img width="347" alt="Captura de Tela 2025-07-04 às 17 05 24" src="https://github.com/user-attachments/assets/aa54c0a8-7bc9-42b0-bafb-c4b2844d2a43" />

### 💭 Discussão

## 🚀 Conclusões e Trabalhos Futuros
#### Exploração de outras variáveis exógenas, pois além da comissão, é possível incluir outros fatores. Uma abordagem detalhada junto ao departamento que desenvolve a base de dados.
#### Testar com os dados de diferentes regiões geográficas, ampliando a robustez e aplicabilidade do modelo.
#### Analisar e aplicar os modelos por diferentes tipos de séries temporais, agregando produto e classificando qual tem maior rentabilidade e volume de vendas.


