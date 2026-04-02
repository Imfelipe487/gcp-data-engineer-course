from google.cloud import bigquery

def query_public_dataset():
    client = bigquery.Client()

    query = """
    SELECT order_items.id, order_id, product_id, products.name  
    FROM `bigquery-public-data.thelook_ecommerce.order_items` as order_items
    join `bigquery-public-data.thelook_ecommerce.products` as products
    ON order_items.product_id = products.id
    """

    results = client.query(query).to_dataframe()[0:5]

    print(results)

if __name__ == "__main__":
    query_public_dataset()