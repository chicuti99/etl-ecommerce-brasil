# **Projeto de Análise de Dados de E-commerce**

Este repositório contém dois arquivos mais importantes, "Notebook_Amentoria" e "dataViewer". Ambos realizam tarefas de extração, transformação e análise dos dados de um e-commerce, mas de maneiras diferentes.

### Estrutura dos Arquivos:

1. **Notebook_Amentoria.ipynb**:  
   Este notebook contém a pipeline usada no Google Cloud Platform (GCP), onde os dados são extraídos de um banco de dados SQL via queries otimizadas e transformados em dataframes para análise.

2. **dataViewer.ipynb**:  
   Este notebook realiza a extração dos dados diretamente de arquivos `.csv` que estão diretamente na pasta datasets, e os transforma em dataframes. para executar os arquivos, 
---

### Como Executar:

#### 1. **Executando o arquivo `Notebook_Amentoria.ipynb` no GCP (BigQuery)**

1. **Preparação do GCP (BigQuery)**:
   - No BigQuery do GCP, crie um conjunto de dados com o nome **"ecommerce_dataset"**.
   - Dentro do conjunto de dados, clique em **"Criar Tabela"** e faça o upload dos seguintes arquivos `.csv`:
   
     | Origem                               | Tabela                 |
     |--------------------------------------|------------------------|
     | olist_customers_dataset.csv          | Clientes               |
     | olist_order_items_dataset.csv        | Itens                  |
     | olist_order_payments_dataset.csv     | Pagamentos             |
     | product_category_name_translation.csv| NomePT-EN              |
     | olist_orders_dataset.csv             | Pedidos                |
     | olist_products_dataset.csv           | Produtos               |
     | olist_sellers_dataset.csv            | Vendedores             |

2. **Configuração do Esquema**:  
   - Em "Esquema", marque o botão **"Detectar automaticamente"** para que o BigQuery configure os tipos de dados corretamente.
   
3. **Execução**:  
   - Após criar as tabelas, basta executar as células de codigo do notebook **"Notebook_Amentoria"** seja importando o arquivo ou copiando e colando os codigos em um notebook criado manualmente.

---

#### 2. **Executando o arquivo `dataViewer.ipynb`**

1. **Criando um Ambiente Virtual**:
   - Crie um ambiente virtual com pipenv.Caso não tenha use o comando:
   ```bash
   pip install pipenv
   ```

   apos isso crie o ambiente virtual com:
   ```bash
   pipenv --python 3.9.15
   ```

   pode baixar as dependencias com:
    ```bash
   pipenv install pandas streamlit plotly
   ```

   ou so com 
    ```bash
    pipenv install
    ```

    apos isso user o comando
    ```bash
    pipenv shell
    ```

    Dentro do notebook selecione o kernel criado recentemente,que e o nome da pasta acrescido de um hash. apos isso execute as celulas do notebook,sempre em sequencia

   
2. **Instalar Dependências**:
   - Instale as dependências necessárias com o comando abaixo caso opte pelo pipenv com python 3.9.15:
     ```bash
     pipenv install pandas streamlit plotly sqlalchemy
     ```

     apos isso use o comando:
    ```bash
     pipenv shell
     ```

3. **Executando o Script**:
   - Após a instalação das dependências, execute as células do script em sequência para visualizar os dados.

---

#### 3. **Streamlit para Visualização dos Dados**

O arquivo `script.py` é responsável por criar um dashboard para visualização dos dados usando Streamlit. Infelizmente, o meu período de teste gratuito no PowerBI e Look Studio já expirou, então utilizei o **Streamlit** como alternativa para visualização dos dados.

Você pode visualizar a aplicação em execução através do link:  
**[https://testeamentoria.streamlit.app/](https://testeamentoria.streamlit.app/)**

---

#### 4. **Escolha do Dataset e Processamento**

Escolhi o dataset **[Brazilian E-commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** do Kaggle, pois ele contém várias tabelas inter-relacionadas com chaves estrangeiras e alguns dados faltantes. Decidi utilizá-lo devido à sua boa organização e qualidade dos dados, mas também pelo fato de que ele exigiria alguns ajustes durante o processo de ETL (Extração, Transformação e Carga).

Após a escolha do dataset, segui os seguintes passos:

1. **ETL - Extração**:
   - Os dados foram extraídos de um banco de dados SQL usando queries que armazenam os dados em dataframes separados.

2. **ETL - Transformação**:
   - **Limpeza dos Dados**: Excluímos as linhas com colunas nulas que não poderiam ser substituídas por outros valores (média, nulo ou vazio).
   - **Normalização de Datas**: Realizei a normalização das datas para um formato uniforme.
   - **Feature Engineering**:
     - **Vendedores**: Criei colunas mostrando quantas vendas foram feitas, quanto foi vendido e o ticket médio de cada vendedor.
     - **Produtos**: Criei colunas para mostrar quantos de cada produto foram vendidos e quanto de receita geraram.
     - **Clientes**: Adicionei colunas para mostrar quanto cada cliente gastou, quantas compras fez e quanto gastou em média.

3. **Data Warehouse**:
   - Após as etapas de transformação, consolidei os dados e criei um **Data Warehouse** chamado **ecommerce_analise** com as tabelas `resumo_vendas`, `vendedores` e `clientes`.

---

#### 5. **Automação do Pipeline**

Para automação do pipeline, utilizei as ferramentas do próprio GCP para executar a pipeline uma vez por dia, garantindo a atualização contínua dos dados.

---

#### 5. **script para criação de banco de dados**

Para criação do banco de dados local e so executar o script `database_create.py` com as credenciais corretas do banco

---

### Conclusão

Este projeto visa mostrar como é possível realizar a análise de dados de um e-commerce utilizando ferramentas de ETL, visualização (Streamlit) e BigQuery para processamento de grandes volumes de dados. A partir de um dataset real de e-commerce brasileiro, foram feitas várias transformações e análises para extrair insights sobre vendas, vendedores e clientes.
