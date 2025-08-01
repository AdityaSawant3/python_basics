import requests

def fetch_data_books():
    url = "https://api.freeapi.app/api/v1/public/books"
    response = requests.get(url)
    data = response.json()

    if data["success"]:
        book_data = data["data"]["data"]
        return book_data
    else:
        raise Exception("Failed to fetch data.")
    
def main():
    try:
        books_data = fetch_data_books()
        for i in range(0, 10):
            data = books_data[i]
            title = data["volumeInfo"].get("title")
            subtitle = data["volumeInfo"].get("subtitle")
            published_date = data["volumeInfo"].get("publishedDate")
            description = data["volumeInfo"].get("description")
            category = data["volumeInfo"]["categories"]
            country = data["saleInfo"].get("country")
            list_price = data["saleInfo"].get("listPrice")
            price = list_price.get("amount") if list_price else "Not Available"

            with open("books_data_using_api.txt", "a", encoding="utf-8") as file:
                file.write(f"\nSr no.{i} Title: {title}\nSubtitle: {subtitle}\nPublised Date: {published_date}\nDescription: {description}\nCategory: {category}\nCountry: {country}\nPrice: {price}\n\n")
    except Exception as e:
        print("Exception: ", str(e))


if __name__ == "__main__":
    main()