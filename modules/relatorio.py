import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

'''A classe gera alguns tipos de relatório. Outros relatórios serão implementados futuramente'''
class Relatorio:
    def __init__(self):
        pass

# Cria o gráfico de número de obras cadastradas
    def gerar_grafico_obras(self):
        conn = sqlite3.connect('biblioteca.db')
        query = "SELECT * FROM obra"
        df = pd.read_sql_query(query, conn)
        conn.close()
        numero_de_linhas = len(df)
        print(f"O número de publicacoes em 'obra' é: {numero_de_linhas}")
        tabelas = ['obra']
        contagens = [numero_de_linhas]
        plt.figure(figsize=(6, 4))
        plt.bar(tabelas, contagens, color='skyblue')
        plt.ylabel('Número de obras')
        plt.title('Contagem de obras ao total')
        plt.show()

# Cria um gráfico pizza dos status de leitura
    def gerar_grafico_status(self):
        conn = sqlite3.connect('biblioteca.db')
        query = "SELECT status FROM obra"
        df = pd.read_sql_query(query, conn)
        conn.close()
        contagem_status = df['status'].value_counts()
        plt.figure(figsize=(8, 6)) 
        contagem_status.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title('Distribuição de Status de Leitura')
        plt.ylabel('') 
        plt.axis('equal') 
        plt.show()

# Instância para testar o relatório
rel = Relatorio()
rel.gerar_grafico_obras()
rel.gerar_grafico_status()
