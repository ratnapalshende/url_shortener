# URL Shortener

Welcome to the URL Shortener project! This application allows users to shorten long URLs into more manageable links. It's built using Django and is deployed on Render.

## Features

- Shorten long URLs
- Copy shortened URLs to clipboard
- Toggle between light and dark themes
- View access count for each shortened URL

## Live Demo

Check out the live demo of the project [here](https://url-shortener-r8k7.onrender.com/).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ratnapalshende/url_shortener.git
   cd url_shortener
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

5. **Visit the application:**

   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- Enter a long URL in the input field and click "Shorten URL".
- Copy the generated short URL using the "Copy URL" button.
- Use the theme toggle button to switch between light and dark modes.

## Code Overview

- **Templates:** The HTML templates are located in `shortener/templates/shortener/`.
  - `home.html`: Main page for URL shortening.
  - `base.html`: Base template with common layout and theme toggle script.

- **Views:** The views are defined in `shortener/views.py`.
  - `home`: Renders the home page.
  - `shorten_url`: Handles URL shortening logic.

- **Models:** The URL mapping model is defined in `shortener/models.py`.

- **URLs:** The URL patterns are defined in `shortener/urls.py`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

