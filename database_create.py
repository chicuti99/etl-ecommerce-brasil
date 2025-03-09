import pandas as pd
from sqlalchemy import create_engine

def carregar_csv_no_banco(caminho_csv, nome_tabela, conexao_url):
    df = pd.read_csv(caminho_csv)
    
    engine = create_engine(conexao_url)
    
    df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)

    print(f"Dados carregados com sucesso na tabela {nome_tabela}!")


arquivos_tabelas = {
    'datasets/olist_customers_dataset.csv': 'Clientes',
    'datasets/olist_order_items_dataset.csv': 'Itens',
    'datasets/olist_order_payments_dataset.csv': 'Pagamentos',
    'datasets/product_category_name_translation.csv': 'NomePT-EN',
    'datasets/olist_orders_dataset.csv': 'Pedidos',
    'datasets/olist_products_dataset.csv': 'Produtos',
    'datasets/olist_sellers_dataset.csv': 'Vendedores'
}

conexao_url = 'mysql+mysqlconnector://user:password@localhost:3306/nome_do_banco'  # Substitua com suas credenciais

for caminho_csv, nome_tabela in arquivos_tabelas.items():
    carregar_csv_no_banco(caminho_csv, nome_tabela, conexao_url)
