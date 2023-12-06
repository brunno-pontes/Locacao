
import streamlit as st
import controllers.clientecontroller as clientecontroller
import models.Produto as produto


def create_produto():
        with st.form(key="Cadastro de Produto"):               
                st.title('Cadastro de Produto')  
                nome_produto = st.text_input(label='Nome produto:')
                quantidade = st.number_input(label='Quantidade:',format='%d',step=1)
                buton = st.form_submit_button(label='Cadastrar')
        if buton:

                clientecontroller.incluir_produto(produto.Produto(nome_produto,quantidade))       
                st.success('Cadastrado com sucesso')
        # idalteracao = st.experimental_get_query_params()
        # st.experimental_set_query_params()
        # clienterecuperado = None
        # if idalteracao.get("id") != None:
        #     idalteracao = idalteracao.get("id")[0]
        #     clienterecuperado = clientecontroller.selecionarByid(idalteracao)
        #     st.experimental_set_query_params(
        #          id=[clienterecuperado.id]
        #     ) 
        #     st.title('Alterar cliente')
        # else:
        #       st.title('Cadastro de Produto')  
      
        # with st.form(key="Cadastro de Produto"):

        #     if clienterecuperado == None:

        #         nome_produto = st.text_input(label='Nome Produto:')
        #         quantidade = st.text_input(label='Quantidade:')
                
               
        #     else:

        #         nome = st.text_input(label='Nome:',value=clienterecuperado.nome)
        #         endereco = st.text_input(label='Endereço:',value=clienterecuperado.endereco)
        #         complemento = st.text_input(label='Complemento:',value=clienterecuperado.complemento)
        #         telefone = st.text_input(label='Telefone:',value=clienterecuperado.telefone)
        #     button = st.form_submit_button(label='Enviar')
             
                     
        # if button:
             
        #      if clienterecuperado == None:
                     
                  
        #              clientecontroller.incluir(cliente.Cliente(0,nome,endereco,complemento,telefone))
        #              st.success('Cadastro com sucesso')
            
           
        #      else:
        #            st.experimental_set_query_params()
        #            clientecontroller.alterar(cliente.Cliente(clienterecuperado.id,nome,endereco,complemento,telefone))
        #            st.success('Alterado com sucesso')
                         



