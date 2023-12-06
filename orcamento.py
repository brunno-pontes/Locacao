# import streamlit as st
# import pages.cliente.produto as produto
# import controllers.clientecontroller as clientecontroller
# import pandas as pd
# from fpdf import FPDF
# import streamlit as st
# import pandas as pd
# from reportlab.pdfgen import canvas
# import models.Cliente as cliente





# def main():
   

# # Verificar se a lista de dados já existe, se não, criar uma lista vazia
#   if 'dados' not in st.session_state:
#       st.session_state.dados = []

# # Criar a tabela usando o componente st.table()
#   st.table(st.session_state.dados)

# # Coletar dados do usuário
#   nome = st.text_input('Produto:')
#   quantidade= st.number_input('quantidade:', min_value=0, max_value=120)
  

# # Adicionar dados à lista quando o botão for pressionado
#   if st.button('Adicionar à Tabela'):
#      novo_dado = {'Nome': nome, 'Quantidade': quantidade}
#      st.session_state.dados.append(novo_dado)
#      st.success('Dados adicionados com sucesso!')
     

# # Exemplo de como você pode salvar os dados em um arquivo
#   if st.button('Salvar em um arquivo'):
#      with open('dados.csv', 'w') as f:
#          for item in st.session_state.dados:
#              f.write("%s\n" % item)
#      st.success('Dados salvos em dados.csv')

 





   


         

    

   


    


# # def orcamento():
                     
# #                      st.title('Orçamento') 
                     

# #                      st.text('Itens') 
# #                      cadeira= st.number_input(label='Caderira:',format='%d',step=1)
# #                      mesa= st.number_input(label='Mesa Quadrada:',format='%d',step=1)
# #                      st.number_input(label='Prato:',format='%d',step=1)
# #                      st.number_input(label='Garfo:',format='%d',step=1)
# #                      st.number_input(label='Colher:',format='%d',step=1)
# #                      st.number_input(label='Mesa Redonda:',format='%d',step=1)
# #                      st.number_input(label='Faca:',format='%d',step=1)
# #                      st.number_input(label='Forro:',format='%d',step=1)
# #                      st.number_input(label='Pula Pula:',format='%d',step=1)  

# #                      if st.button("gerar"):
# #                              pdf = FPDF()
# #                              pdf.add_page()
# #                              pdf.set_font('Arial', '', 14)
# #                              pdf.image("Orçamento.png", 50, 50)
# #                              pdf.output('Orçamento.pdf', 'F') 


      
                 
                    

                   