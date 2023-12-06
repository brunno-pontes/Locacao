
import streamlit as st
import controllers.clientecontroller as clientecontroller
import models.Cliente as cliente
import this
from turtle import onclick
import streamlit as st;

def create():       
        idalteracao = st.experimental_get_query_params()
        st.experimental_set_query_params()
        clienterecuperado = None
        if idalteracao.get("id") != None:
            idalteracao = idalteracao.get("id")[0]
            clienterecuperado = clientecontroller.selecionarByid(idalteracao)
            st.experimental_set_query_params(
                 id=[clienterecuperado.id]
            ) 
            st.title('Alterar cliente')
            
        else:
              st.title('Cadastro de cliente')  
      
        with st.form(key="Cadastrar cliente"):

            if clienterecuperado == None:

                nome = st.text_input(label='Nome:')
                endereco = st.text_input(label='Endereço:')
                complemento = st.text_input(label='Complemento:')
                telefone = st.text_input(label='Telefone:')
               
            else:

                nome = st.text_input(label='Nome:',value=clienterecuperado.nome)
                endereco = st.text_input(label='Endereço:',value=clienterecuperado.endereco)
                complemento = st.text_input(label='Complemento:',value=clienterecuperado.complemento)
                telefone = st.text_input(label='Telefone:',value=clienterecuperado.telefone)
            button = st.form_submit_button(label='Enviar')
             
                     
        if button:
             
             if clienterecuperado == None:
                     
                  
                     clientecontroller.incluir(cliente.Cliente(0,nome,endereco,complemento,telefone))
                     st.success('Cadastrado com sucesso')
            
           
             else:
                   st.experimental_set_query_params()
                   clientecontroller.alterar(cliente.Cliente(clienterecuperado.id,nome,endereco,complemento,telefone))
                   st.success('Alterado com sucesso')
                         
             

                    

      