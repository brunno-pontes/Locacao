import models.Cliente as cliente
import services.database as bd

def selecionarByid(id):
     bd.cur.execute("SELECT * FROM cliente WHERE ID= ?",(id,))
     costumerlist =[]
     for row in bd.cur:   
          costumerlist.append(cliente.Cliente(row[0],row[1],row[2],row[3],row[4]))        
     return costumerlist[0]  

def incluir_produto(produto):
        bd.cur.execute(
            """INSERT INTO produto (nome_produto,quantidade)
              VALUES(?,?)""", 
              (produto.nome_produto, produto.quantidade))
        bd.conexao.commit()

def incluir(cliente):
        bd.cur.execute(
            """INSERT INTO cliente (nome,endereco,complemento,telefone)
              VALUES(?,?,?,?)""", 
              (cliente.nome, cliente.endereco,cliente.complemento, cliente.telefone))
        bd.conexao.commit()
        # bd.conexao.close()  

def selecionartodos():
     bd.cur.execute("SELECT * FROM cliente")
     costumerlist =[]
     for row in bd.cur:   
          costumerlist.append(cliente.Cliente(row[0],row[1],row[2],row[3],row[4]))        
     return costumerlist   

def alterar(cliente):
     bd.cur.execute("UPDATE cliente SET nome = ?, endereco = ?,complemento = ?, telefone = ? WHERE id = ?",
     (cliente.nome,cliente.endereco,cliente.complemento,cliente.telefone,cliente.id)) 
     bd.conexao.commit()
     # bd.conexao.close() 

def excluir(id):
    bd.cur.execute("""
    DELETE FROM CLIENTE WHERE id = ?""",
    (id,))
    bd.conexao.commit()
#     bd.conexao.close() 
def selecionarproduto():
     bd.cur.execute("SELECT * FROM produto")
     bd.conexao.commit()

            