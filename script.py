import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar os CSVs
df_clientes = pd.read_csv("datasets/olist_customers_dataset.csv")
df_items = pd.read_csv("datasets/olist_order_items_dataset.csv")
df_pedidos = pd.read_csv("datasets/olist_orders_dataset.csv")
df_produtos = pd.read_csv("datasets/olist_products_dataset.csv")

# Calcular Receita Total
receita_total = df_items["price"].sum()

# Número de Vendas por Estado
df_vendas_estado = df_pedidos.merge(df_clientes, on="customer_id").groupby("customer_state")["order_id"].count().reset_index()
df_vendas_estado.columns = ["estado", "num_vendas"]

# Número de Vendas por Categoria de Produto
df_vendas_categoria = df_items.merge(df_produtos, on="product_id").groupby("product_category_name")["order_id"].count().reset_index()
df_vendas_categoria.columns = ["categoria_produto", "total_vendas"]

# Criar DataFrame Resumo
df_resumo = pd.DataFrame({"Receita Total": [receita_total]})

# Criar o dashboard
st.title("Dashboard de Vendas - E-commerce")

# Receita Total
st.metric(label="Receita Total", value=f"R$ {receita_total:,.2f}")

# Gráfico de Número de Vendas por Estado
fig_estado = px.bar(df_vendas_estado, x="estado", y="num_vendas", title="Vendas por Estado")
st.plotly_chart(fig_estado)

# Gráfico de Vendas por Categoria de Produto
fig_categoria = px.pie(df_vendas_categoria, names="categoria_produto", values="total_vendas", title="Vendas por Categoria")
st.plotly_chart(fig_categoria)
