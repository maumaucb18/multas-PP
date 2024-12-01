from flask import Flask, request, render_template
import pandas as pd

# Inicializar o Flask
app = Flask(__name__)

# Carregar os dados com tratamento para colunas específicas
data_path = "relacao_produtos_perigosos.csv"
data = pd.read_csv(data_path, dtype=str)  # Garantir que os dados sejam strings

# Selecionar e renomear colunas
selected_columns = {
    "Nº ONU (1)": "Codigo_ONU",
    "Nome e Descrição (2)": "Nome_Descricao",
    "Classe ou Subclasse de Risco (3)": "Classe_Subclasse_Risco",
    "Risco Subsi- diário (4)": "Risco_Subsidiario",
    "Nº de Risco (5)": "Numero_Risco",
    "Grupo de Emb. (6)": "Grupo_Embalagem",
    "Provisões Especiais (7)":"Provisões_especiais",
   

    
}

# Filtrar e renomear colunas
data_cleaned = data[list(selected_columns.keys())].copy()
data_cleaned.columns = selected_columns.values()

# Substituir valores ausentes por "Não informado"
data_cleaned.fillna("Não informado", inplace=True)

# Garantir que os códigos ONU estejam no formato correto
data_cleaned['Codigo_ONU'] = data_cleaned['Codigo_ONU'].str.strip()

# Página inicial com o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota de pesquisa
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').upper()  # Converte a entrada para maiúsculas
    filtered_data = data_cleaned[
        data_cleaned['Codigo_ONU'].str.contains(query, na=False) |
        data_cleaned['Nome_Descricao'].str.upper().str.contains(query, na=False)
    ]
    results = filtered_data.to_dict(orient='records')
    return render_template('results.html', results=results, columns=data_cleaned.columns.tolist())


# Executar o app
if __name__ == '__main__':
    app.run(debug=True)
