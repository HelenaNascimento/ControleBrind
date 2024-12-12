from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    # Dados de exemplo
    data = {
        'Ano': [2018, 2019, 2020, 2021, 2022],
        'Vendas': [150, 200, 300, 400, 350]
    }

    # Criando um gráfico de linha com Plotly
    fig = px.line(data, x='Ano', y='Vendas', title='Vendas por Ano')

    # Convertendo o gráfico para HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Renderiza a página HTML e passa o gráfico
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
