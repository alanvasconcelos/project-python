from dao.banco import *
from model import *

class UnidadeDeSaudeDAO:
    def __init__(self):
        self.conn = Banco().conexao

    def insert(self, unitHealth):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO unidades (codigo, nome) VALUES (?,?)", (unitHealth.cnes, unitHealth.nome))
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def searchAll(self):
        cursor = self.conn.cursor()
        sql = "SELECT count(*) AS num_vezes, codigo, nome FROM unidades GROUP BY codigo ORDER BY num_vezes DESC"
        cursor.execute(sql)
        result = []
        for row in cursor.fetchall():
            l = [row[0], row[1], row[2]]
            result.append(l)
        cursor.close()
        self.conn.close()
        return result
