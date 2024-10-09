
# Importar os dados
import pandas as pd
from IPython.core.display_functions import display
import plotly.express as px

# Ler o arquivo CSV
tabela = pd.read_csv("cancelamentos.csv")

# Visualizar os dados: O que temos e os problemas da base de dados
tabela = tabela.drop(columns="CustomerID")

# Exibir informações da tabela
tabela.info()

tabela = tabela.dropna()

tabela.info()

# Analise de cancelados
# contagem
display(tabela["cancelou"].value_counts())

# porcentagem
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color="cancelou",text_auto=True)
    # exibir o gráfico
    grafico.show()

# CONCLUSÃO
    #  Todos os contratos mensal cancelaram