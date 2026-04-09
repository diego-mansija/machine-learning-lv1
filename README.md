Predição de Demanda com Machine Learning

Este projeto aplica uma solução de Inteligência Preditiva. A aplicação utiliza modelos estatísticos para projetar volumes de vendas futuros com base em dados históricos, auxiliando na tomada de decisão estratégica e gestão de inventário.

1.Objetivo

Desenvolver um sistema preditivo que utiliza algoritmos de Regressão Linear para estimar a demanda de produtos nos meses subsequentes sem considerar oscilações sazonais específicas, mas útil para planejamento de estoque inicial. O foco é transformar registros históricos em insights acionáveis, demonstrando a aplicação prática de Machine Learning em cenários de negócio.

2.Tecnologias e Ferramentas

Ambiente de Desenvolvimento: Linux Mint Cinnamon.

Linguagem: Python 3.12.

Machine Learning: Scikit-Learn (LinearRegression).

Interface e Visualização: Streamlit para o dashboard interativo.

Análise de Dados: Pandas, NumPy e Matplotlib.

Versionamento: Git para controle de código.

3.Estrutura de Diretórios

    machine-learning-lv1/
    |
    ├── data/
    │   └── vendas.csv          # Histórico de transações
    ├── src/
    │   └── app.py           # Aplicação com lógica de treinamento e predição
    ├── .gitignore              # Proteção do ambiente virtual e arquivos temporários
    ├── README.md               # Documentação técnica
    └── requirements.txt        # Dependências (pandas, scikit-learn, streamlit)

4.Funcionalidades Implementadas

Modelagem Preditiva: Treinamento de modelo de Regressão Linear em tempo real utilizando a biblioteca Scikit-Learn.

Projeção Dinâmica: Slider interativo que permite ao usuário definir o horizonte de previsão (ex: prever os próximos 6 meses).

Análise de Séries Temporais: Processamento de dados históricos com agrupamento mensal e tratamento de sazonalidade.

Visualização de Tendências: Gráfico comparativo entre dados reais (passado) e dados projetados (futuro).

Métricas de Negócio: Cálculo automático do volume total de demanda previsto para o período selecionado.

5.Diferenciais Técnicos

Tratamento de Frequência: Implementação atualizada utilizando ME (Month End) para compatibilidade com as versões recentes do Pandas.

Performance: Uso do decorador @st.cache_data para otimização do carregamento e processamento do modelo.

Escalabilidade: Estrutura preparada para inclusão de novos modelos de regressão ou algoritmos de Random Forest em etapas futuras.

6.Instruções de Instalação e Execução
6.1 Configuração do Ambiente

Clone o repositório:

    git clone https://github.com/diego-mansija/machine-learning-lv1.git

Configure o ambiente virtual e instale as dependências:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

5.2 Execução da Aplicação

Para iniciar o sistema de predição localmente:

    streamlit run src/app.py

6.Demonstração e Acesso Online

A aplicação está hospedada no Streamlit Community Cloud e pode ser acessada através do link abaixo:

[Acesse o Dashboard Preditivo Online](https://machine-learning-lv1.streamlit.app/)
