# My Zootopia API

A small Python project that generates a static HTML page with information about animals. It takes an animal name from the user, fetches data about that animal from the [API Ninjas Animals API](https://api-ninjas.com/api/animals), and renders the results into an `animals.html` file using a template.

## Features

- Prompts the user for an animal name.
- Fetches live animal data (diet, location, type, etc.) from the API Ninjas Animals API.
- Generates an `animals.html` page from `animals_template.html`.
- Shows a friendly message when no animal matches the given name.

## Installation

To install this project, simply clone the repository and install the dependencies in `requirements.txt` using `pip`:

```bash
git clone <repository-url>
cd My-Zootopia-API
pip install -r requirements.txt
```

This project uses the API Ninjas Animals API. You will need to sign up at [api-ninjas.com](https://api-ninjas.com/) to get a free API key.

Create a `.env` file in the project root and add your API key:

```
API_KEY=your_api_key_here
```

## Usage

To use this project, run the following command:

```bash
python animals_web_generator.py
```

You will be prompted to enter the name of an animal. Once the program finishes, open `animals.html` in your browser to view the generated page.

## Project Structure

- `animals_web_generator.py` — main entry point; prompts the user, serializes animals, and writes the HTML file.
- `data_fetcher.py` — handles the request to the API Ninjas Animals API.
- `animals_template.html` — HTML template used to render the page.
- `animals.html` — generated output file.
- `requirements.txt` — Python dependencies.
- `.env` — stores your API key (not committed).

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository and create a feature branch.
2. Make your changes with clear, well-documented code.
3. Test your changes locally before submitting.
4. Open a pull request describing what you changed and why.

Bug reports and feature suggestions are also welcome via the issue tracker.
