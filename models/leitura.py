
import sqlite3
from datetime import datetime
from models.status import Status
from models.configuracao import Configuracao
'''Classe Leitura controla e valida as acoes de leitura e avaliacao. A classe também controla alguns parametros opcionais,
como o de metas de leituras anuais e o limite de leituras simultaneas '''
class Leitura:
    def __init__(self, id_obra, avaliacao = None):
        self.id_obra = id_obra
        self.avaliacao = avaliacao
        self.data_inicio = None
        self.data_termino = None

    def _conectar(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        return conn, cursor

    def _get_status(self):
        conn, cursor = self._conectar()
        cursor.execute("SELECT status FROM obra WHERE id_obra = ?", (self.id_obra,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Status(row[0])
        else:
            raise ValueError("Obra não encontrada.")
        
    def _contar_leituras_ativas(self):
        conn, cursor = self._conectar()
        cursor.execute("""
            SELECT COUNT(*)
            FROM obra
            WHERE status = ?
        """, (Status.LENDO.value,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
        
    def _atingiu_limite_leituras(self):
        config = Configuracao()
        leituras_ativas = self._contar_leituras_ativas()
        return leituras_ativas >= config.numero_leitura_simultanea

    def contar_leituras_concluidas_ano(self, ano=None):
        if ano is None:
            ano = datetime.now().year 
        conn, cursor = self._conectar()
        cursor.execute(
            "SELECT COUNT(*) FROM obra WHERE status=? AND strftime('%Y', data_termino)=?",
            (Status.LIDO.value, str(ano))
        )
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    
    def verificar_meta_anual(self):
        config = Configuracao()
        ano_atual = datetime.now().year
        leituras_ano = self.contar_leituras_concluidas_ano(ano_atual)

        if leituras_ano < config.meta_anual_leitura:
            print(f" Meta anual de leitura não concluída: {leituras_ano}/{config.meta_anual_leitura} livros lidos.")
        else:
            print(f" Meta anual de leitura atingida: {leituras_ano}/{config.meta_anual_leitura} livros lidos.")


    def iniciar_leitura(self):
        status = self._get_status()
        if status != Status.NAO_LIDO:
            raise ValueError("Leitura já iniciada ou concluída.")
        config = Configuracao()
        leituras_ativas = self._contar_leituras_ativas()
        if leituras_ativas >= config.numero_leitura_simultanea:
            raise ValueError(
                f"Limite de {config.numero_leitura_simultanea} leituras simultâneas atingido."
        )
        self.data_inicio = datetime.now()
        conn, cursor = self._conectar()
        cursor.execute(
            "UPDATE obra SET status=?, data_inicio=? WHERE id_obra=?",
            (Status.LENDO.value, self.data_inicio.strftime("%Y-%m-%d %H:%M:%S"), self.id_obra)
        )
        conn.commit()
        conn.close()
        print(f"Leitura iniciada em {self.data_inicio}")

    def concluir_leitura(self):
        status = self._get_status()
        if status != Status.LENDO:
            raise ValueError("Você deve iniciar a leitura antes de concluir.")
        self.data_termino = datetime.now()
        conn, cursor = self._conectar()
        cursor.execute(
            "UPDATE obra SET status=?, data_termino=? WHERE id_obra=?",
            (Status.LIDO.value, self.data_termino.strftime("%Y-%m-%d %H:%M:%S"), self.id_obra)
        )
        conn.commit()
        conn.close()
        print(f"Leitura concluída em {self.data_termino}")

    def _get_avaliacao(self):
        conn, cursor = self._conectar()
        cursor.execute("SELECT avaliacao FROM obra WHERE id_obra = ?", (self.id_obra,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return (row[0])
        else:
            raise ValueError("Obra não encontrada.")
        
    def validar_avaliacao(self, avaliacao):
        status = self._get_status()    
        if status != Status.LIDO:
            raise ValueError("Avaliacao só pode ser feita após a leitura estar concluída (status LIDO).")
        if not (0 <= avaliacao <= 10):
            raise ValueError("Avaliacao deve estar entre 0 e 10.")
        conn, cursor = self._conectar()
        cursor.execute("""
            UPDATE obra
            SET avaliacao = ?
            WHERE id_obra = ?
        """, (avaliacao, self.id_obra))
        conn.commit()
        conn.close()

        print(f"Avaliação registrada: {avaliacao}")
