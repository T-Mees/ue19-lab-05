import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals"

def fetch_deals():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        deals = response.json()

        for deal in deals[:50]:  # Affiche les 50 premières offres
            print("")
            num = str(deals.index(deal) + 1)
            print(f"{num}. {deal['title']}")
            print(f"Sale Price: ${deal['salePrice']}")
            print(f"Normal Price: ${deal['normalPrice']}")
            print(f"image: {deal['thumb']}")  # Ajout de l'image
            print("link: https://www.cheapshark.com/redirect?dealID=" + deal['dealID'])  # Ajout du lien
            print('')
            print("--------------------------------------------------")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    fetch_deals()
