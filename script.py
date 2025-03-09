
import pandas as pd
import streamlit as st
import plotly.express as px


df_clientes = pd.read_csv("datasets/olist_customers_dataset.csv")
df_items = pd.read_csv("datasets/olist_order_items_dataset.csv")
df_nomes = pd.read_csv("datasets/product_category_name_translation.csv")
df_pedidos = pd.read_csv("datasets/olist_orders_dataset.csv")
df_vendedores = pd.read_csv("datasets/olist_sellers_dataset.csv")
df_pagamentos = pd.read_csv("datasets/olist_order_payments_dataset.csv")
df_produtos = pd.read_csv("datasets/olist_products_dataset.csv")

df_pedidos = df_pedidos.dropna(subset=['order_delivered_carrier_date', 'order_delivered_customer_date'])

df_items['shipping_limit_date'] = pd.to_datetime(df_items['shipping_limit_date'])

df_pedidos['order_purchase_timestamp'] = pd.to_datetime(df_pedidos['order_purchase_timestamp'])
df_pedidos['order_approved_at'] = pd.to_datetime(df_pedidos['order_approved_at'])
df_pedidos['order_delivered_carrier_date'] = pd.to_datetime(df_pedidos['order_delivered_carrier_date'])
df_pedidos['order_delivered_customer_date'] = pd.to_datetime(df_pedidos['order_delivered_customer_date'])
df_pedidos['order_estimated_delivery_date'] = pd.to_datetime(df_pedidos['order_estimated_delivery_date'])

df_pedidos['is_delivered_late'] = df_pedidos['order_delivered_customer_date'] > df_pedidos['order_estimated_delivery_date']

df_vendas = df_items.groupby("seller_id").agg(
    sales=("order_id", "count"),
    total_sold=("price", "sum"),
)


df_vendas["medium_ticket"] = df_vendas["total_sold"] / df_vendas["sales"]

df_vendas.reset_index(inplace=True)

df_vendedores = df_vendedores.merge(df_vendas, on="seller_id", how="left")

df_vendedores.fillna({"sales": 0, "total_sold": 0, "medium_ticket": 0}, inplace=True)


df_produto_vendas = df_items.groupby("product_id").agg(
    total_sales=("order_id", "count"),
    total_revenue=("price", "sum")
)

df_produto_vendas.reset_index(inplace=True)


df_produtos = df_produtos.merge(df_produto_vendas, on="product_id", how="left")

df_produtos.fillna({"total_sales": 0, "total_revenue": 0}, inplace=True)

df_order_totals = df_items.groupby('order_id')['price'].sum().reset_index()
df_order_totals.rename(columns={'price': 'total_order_value'}, inplace=True)

df_pedidos = df_pedidos.merge(df_order_totals, on='order_id', how='left')


df_customer_stats = df_pedidos.groupby('customer_id').agg(
    total_spent=('total_order_value', 'sum'),
    average_order_value=('total_order_value', 'mean'),
    total_orders=('order_id', 'count')
).reset_index()

df_clientes = df_clientes.merge(df_customer_stats, on='customer_id', how='left')

df_clientes.fillna({'total_spent': 0, 'average_order_value': 0, 'total_orders': 0}, inplace=True)

receita_total = df_items['price'].sum()

vendas_por_estado = df_pedidos.merge(df_clientes, on='customer_id').groupby('customer_state')['order_id'].count()

vendas_por_categoria = df_items.merge(df_produtos, on='product_id').groupby('product_category_name')['order_id'].count()

df_resumo = pd.DataFrame({
    'Receita Total': [receita_total],
    'Vendas por Estado': [vendas_por_estado.to_dict()],
    'Vendas por Categoria': [vendas_por_categoria.to_dict()]
})

st.title("📊 Dashboard de Vendas - E-commerce")

# **Métrica de Receita Total**
receita_total = df_resumo["Receita Total"].values[0]
st.metric(label="💰 Receita Total", value=f"R$ {receita_total:,.2f}")

# **Gráfico de Vendas por Estado**
st.subheader("📍 Vendas por Estado")
df_estado = pd.DataFrame(df_resumo["Vendas por Estado"].values[0].items(), columns=["Estado", "Número de Vendas"])
fig_estado = px.bar(df_estado, x="Estado", y="Número de Vendas", title="Vendas por Estado")
st.plotly_chart(fig_estado)

# **Gráfico de Vendas por Categoria de Produto**
st.subheader("🛍️ Vendas por Categoria de Produto")
df_categoria = pd.DataFrame(df_resumo["Vendas por Categoria"].values[0].items(), columns=["Categoria", "Total de Vendas"])
fig_categoria = px.pie(df_categoria, names="Categoria", values="Total de Vendas", title="Vendas por Categoria")
st.plotly_chart(fig_categoria)