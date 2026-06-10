"""
Animals Web Generator
"""
from data_fetcher import fetch_data

REPLACE_TEMPLATE_TEXT = '__REPLACE_ANIMALS_INFO__'


def serialize_animal(animal_obj):
    """Serializes an animal object"""
    animal_string = ''
    animal_string += '<li class="cards__item">\n'
    animal_string += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    animal_string += '<p class="card__text">\n'
    animal_string += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    animal_string += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    animal_type = animal_obj["characteristics"].get("type")
    if animal_type:
        animal_string += f'<strong>Type:</strong> {animal_type}<br/>\n'
    animal_string += '</p>\n'
    animal_string += '</li>\n'
    return animal_string


def main():
    """Main function"""
    animal_to_search = input('Enter a name of an animal: ')
    animals_data = fetch_data(animal_to_search)

    animals_data_string = ''
    if not animals_data:
        animals_data_string = f'<h2>The animal "{animal_to_search}" doesn\'t exist.</h2>'

    for animal in animals_data:
        animals_data_string += serialize_animal(animal)

    with open('animals_template.html', 'r') as handle:
        template = handle.read()

    filled_template = template.replace(REPLACE_TEMPLATE_TEXT, animals_data_string)
    with open('animals.html', 'w') as handle:
        handle.write(filled_template)
        print("Website was successfully generated to the file animals.html.")

if __name__ == '__main__':
    main()