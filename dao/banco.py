import sqlite3

class Banco():
    def __init__(self):
        self._conexao = sqlite3.connect('banco.db')
        self.createTable()
   
    def _get_conexao(self):
        return self._conexao

    def _set_conexao(self, con):
        self._conexao = con

    def createTable(self):
        c = self._conexao.cursor()
   
        c.execute("""create table if not exists unidades (
                       id integer primary key,
                       codigo integer,
                       nome text)""")
        
        self._conexao.commit()
        c.close()

    def close(self):
		    self._conexao.close()

    conexao = property(_get_conexao, _set_conexao)
