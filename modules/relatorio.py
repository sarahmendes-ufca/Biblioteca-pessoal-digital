import sqlite3
import pandas as pd
import os
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
        folder_path = 'C:\\Users\\sarah\\bibliotecapessoal\\graphics'
        file_name = 'Número Total de Obras.png'
        full_path = os.path.join(folder_path, file_name)
        os.makedirs(folder_path, exist_ok=True)
        plt.savefig(full_path, bbox_inches='tight', pad_inches=0.5)
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
        folder_path = 'C:\\Users\\sarah\\bibliotecapessoal\\graphics'
        file_name = 'Porcentagem de Livros por Status de Leitura.png'
        full_path = os.path.join(folder_path, file_name)
        os.makedirs(folder_path, exist_ok=True)
        plt.savefig(full_path, bbox_inches='tight', pad_inches=0.5)
        plt.show()

    # Gera gráfico da media de avaliações das obras, ao total   
    def gerar_grafico_media_avaliacoes(self):
        conn = sqlite3.connect('biblioteca.db')
        query = "SELECT avaliacao FROM obra WHERE status = 'LIDO'"
        df = pd.read_sql_query(query, conn)
        conn.close()
        media_avaliacoes = df['avaliacao'].value_counts()
        plt.figure(figsize=(8, 6))
        media_avaliacoes.plot(kind='bar')
        plt.ylabel('')
        plt.title('Media de avaliacões de Obras Lidas')
        folder_path = 'C:\\Users\\sarah\\bibliotecapessoal\\graphics'
        file_name = 'Media de avaliacões de Obras Lidas.png'
        full_path = os.path.join(folder_path, file_name)
        os.makedirs(folder_path, exist_ok=True)
        plt.savefig(full_path, bbox_inches='tight', pad_inches=0.5)
        plt.show()


    def mostrar_top5_avaliacoes(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        query = """
            SELECT titulo, avaliacao
            FROM obra
            WHERE status = 'LIDO' AND avaliacao > 0
            ORDER BY avaliacao DESC
            LIMIT 5;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        conn.close()
    
        titulos = [row[0] for row in resultados]
        avaliacoes = [row[1] for row in resultados]
    
        print(titulos)
        print(avaliacoes)

