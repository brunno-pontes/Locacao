import streamlit as st
import pages.cliente.cadastrar as pagecliente
import pages.cliente.list as pagelist
import pages.cliente.produto as pageproduto

     
st.title('Mônica Locaçôes')
st.image("image_1.png") 
st.sidebar.title('Menu')
pagina = st.sidebar.selectbox('Selecione:',['Cadastrar cliente','Consulta','Produto'])


if pagina == 'Produto':

     st.experimental_set_query_params()
     pageproduto.create_produto()
       

elif pagina == "Consulta":
      
      pagelist.List()
 
 
    
elif pagina == 'Cadastrar cliente':

     st.experimental_set_query_params()
     pagecliente.create()

# elif pagina == 'Orçamento':
     
#      pageorcamento.main()










    # Exibir a tabela atualizada

# # Função para criar PDF a partir da tabela
# def criar_pdf(dados, nome_do_arquivo='output.pdf'):
#     from reportlab.lib import colors
#     from reportlab.lib.pagesizes import letter
#     from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

#     # Criar um objeto PDF
#     pdf = SimpleDocTemplate(nome_do_arquivo, pagesize=letter)

   

#     # Estilo da tabela
#     estilo_tabela = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                 ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                 ('GRID', (0, 0), (-1, -1), 1, colors.black)])

#     tabela.setStyle(estilo_tabela)

#     # Adicionar tabela ao PDF
#     pdf.build([tabela])



#     # Criar o PDF atualizado
#     criar_pdf(dados, nome_do_arquivo='output_atualizado.pdf')
#     st.success('PDF atualizado com sucesso!')







     # pageorcamento.main()
     # pageorcamento.adicionar_item()
     # pageorcamento.gerar_pdf()







