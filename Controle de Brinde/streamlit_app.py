import streamlit as st
import requests

# Função para definir a página atual na URL
def set_page(page_name):
    st.query_params.update(page=page_name)

# Função para obter a página atual
def get_current_page():
    params = st.query_params
    return params.get("page", ["login"])[0]  # "login" como página padrão

# Página de Login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Simulação da requisição de login (substitua aqui pela requisição para sua API)
        response = requests.post(
            "http://127.0.0.1:5000/login",
            json={"username": username, "password": password}
        )
        if response and response.status_code == 200:
            data = response.json()
            if data.get('success'):
                st.success(data['message'])
                next_page = data.get('pages/entrada.py')  # Nome da página de destino
                if next_page:
                    set_page(next_page)  # Redireciona para a página de destino
            else:
                st.error(data['message'])
        else:
            st.error("Falha ao conectar com o servidor Flask.")

# Página de Entrada
def entrada_page():
    st.title("Página de Entrada")
    st.write("Conteúdo específico para a página de Entrada.")
    if st.button("Logout"):
        set_page("login")  # Redireciona para a página de login

# Outras páginas (Saída, Brinde, etc.) seguem o mesmo padrão
def saida_page():
    st.title("Página de Saída")
    st.write("Conteúdo específico para a página de Saída.")
    if st.button("Logout"):
        set_page("login")

def brinde_page():
    st.title("Página de Brinde")
    st.write("Conteúdo específico para a página de Brinde.")
    if st.button("Logout"):
        set_page("login")

# Roteamento das páginas
def main():
    page = get_current_page()
    if page == "login":
        login_page()
    elif page == "entrada":
        entrada_page()
    elif page == "saida":
        saida_page()
    elif page == "brinde":
        brinde_page()
    else:
        st.write("Página não encontrada")

if __name__ == "__main__":
    main()
