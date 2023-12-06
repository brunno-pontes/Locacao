import streamlit as st
import controllers.clientecontroller as clientecontroller
import pages.cliente.cadastrar as pagecliente


def List():
      paramid = st.experimental_get_query_params()
      if paramid == {}:
                  
            st.title('Consultar cliente')
            st.experimental_set_query_params()
            colms = st.columns((1,2,2,3,3,2,2))
            campos = ['N°','Nome','Endereço','Complemento','Contato ','Excluir','Alterar']
            for col, campo_nome in zip(colms,campos):
                  col.write(campo_nome)   
            for item in clientecontroller.selecionartodos():
                  col1,col2,col3,col4,col5,col6,col7= st.columns((1,2,2,3,3,2,2,))
                  col1.write(item.id)
                  col2.write(item.nome)
                  col3.write(item.endereco)
                  col4.write(item.complemento)
                  col5.write(item.telefone)
                  button_space_excluir = col6.empty()
                  on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
                  button_space = col7.empty()
                  on_click_alterar = button_space.button('Alterar','bntAlterar'+str(item.id))
                 
                  
                  if on_click_excluir:
                        clientecontroller.excluir(item.id)
                        button_space_excluir.button('excluir', 'btnexcluir' + str(item.id))
                        st.success('Excluido com sucesso')
                        st.experimental_rerun()
                  if on_click_alterar:
                        st.experimental_set_query_params(
                        id=[item.id]
                        )
                  
                
                 
      else:
            on_click_voltar = st.button("Voltar")
            if on_click_voltar:
                  st.experimental_set_query_params()
                  st.experimental_rerun()
            pagecliente.create()      


                 
                   