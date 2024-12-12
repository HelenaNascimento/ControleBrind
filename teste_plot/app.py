from flask import Flask, render_template_string
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def plot():
    # Criar dados do gráfico
    fig = go.Figure(data=go.Bar(y=[2, 3, 1, 5]))
    graph = pio.to_html(fig, full_html=False)

    # Exibir o gráfico no HTML
    html = f"""
    <html>
        <head><title>Gráfico Plotly</title></head>
        <body>
            <h1>Gráfico Interativo com Plotly</h1>
            {graph}
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
