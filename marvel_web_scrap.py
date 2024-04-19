import requests
from bs4 import BeautifulSoup

def get_character_info(character_name):
    # URL of the character page on the Marvel Fandom Wiki
    url = f"https://marvel.fandom.com/wiki/{character_name.replace(' ', '_')}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the character information
        character_info = {}

        # Example: Extracting the character's real name
        real_name_element = soup.find('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
        if real_name_element:
            real_name = real_name_element.find('h3', class_='pi-data-label pi-secondary-font').text.strip()
            real_name_value = real_name_element.find('div', class_='pi-data-value pi-font').text.strip()  
            character_info[real_name] = real_name_value

        gender_element = soup.findAll('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
        #print(gender_element)
        for div_element in gender_element:
           # print(div_element.find('h3', class_='pi-data-label pi-secondary-font'))
            label = div_element.find('h3', class_='pi-data-label pi-secondary-font')
            if label.text.strip() == 'Gender':
                character_info['Gender'] = div_element.find('div', class_='pi-data-value pi-font').text.strip()
                print(div_element.find('div', class_='pi-data-value pi-font').text.strip())
        # You can extract other information similarly

        return character_info
    else:
        print("Error:", response.status_code)
        return None

if __name__ == "__main__":
    character_name = input("Enter the name of the Marvel character: ")
    character_info = get_character_info(character_name)
    if character_info:
        print("Character Information:")
        for key, value in character_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve character information.")