import requests
from bs4 import BeautifulSoup

def get_all_characters():
    characters = []

    # URL of the page listing all characters on the Marvel Fandom Wiki
    url = "https://marvel.fandom.com/wiki/Category:Characters"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links to character pages
        character_links = soup.find_all('a', class_='category-page__member-link')
        
        # Extract character names from links
        for link in character_links:
            characters.append(link.text.strip())

    else:
        print("Error:", response.status_code)

    return characters

if __name__ == "__main__":
    all_characters = get_all_characters()
    print("List of all Marvel characters:")
    for character in all_characters:
        print(character)