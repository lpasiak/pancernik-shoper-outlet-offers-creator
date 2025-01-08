from api_connection import ShoperAPIClient
import pandas as pd

# special_offer = {
#     'discount': 10,
#     'date_from': '2024-12-13 00:00:00',
#     'date_to': '2026-01-01 00:00:00',
#     'product_id': 10753,
#     'discount_type': 2,
# }

if __name__ == "__main__":
    client = ShoperAPIClient()

    try:
        # Authenticate with the Shoper API
        client.connect()
        # == Fetch and display products == #
        df = pd.DataFrame(client.get_all_products())
        df.to_excel('wszystkie_produkty.xlsx', index=False)

    except Exception as e:
        print(f"Error: {e}")
