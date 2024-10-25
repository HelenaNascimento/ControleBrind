import streamlit as st

st.set_page_config(
    page_title="BI - NOVA CE",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")



def show(): 
    
    st.title("Entrada de Nota")
    
    cols = st.columns(2)
    
    with cols[0]:
        with st.container():
            
            st.subheader("Cabeçalho Nota de Entrada")
            
            with st.container():
                
                chv = st.radio(
                    
                    "Possui Chave de Acesso?:",
                    ["Sim", "Não"],
                
                )
                
                if chv == "Sim":
                    st.write("Sim")
                else:
                    st.write("Não")

    with cols[1]:
        with st.container():
          
            st.subheader("Itens")

if __name__ == "__main__":
    
    show()
