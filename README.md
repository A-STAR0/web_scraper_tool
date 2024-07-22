# Web Scraper Tool (**https://web-scraper-tool.onrender.com/docs**)

This is a web scraper tool developed using Python and FastAPI to automate the process of scraping product information from the [Dental Stall](https://dentalstall.com/shop/) website. 
The tool is capable of scraping product names, prices, and images from multiple pages of the product catalog and stores the scraped information in an in-memory cache and a JSON file.

## Features

- **Scrape Product Information**: Scrapes product names, prices, and images from the website.
- **Settings**: Allows setting a limit on the number of pages to scrape and using a proxy for the scraping process.
- **Authentication**: Simple authentication using a static API key.
- **Data Storage**: Stores scraped data in an in-memory cache and a JSON file.
- **Notification**: logs the scraping status to the console, indicating the number of products scraped and updated. 
(We can extend it further as I have used created ABC for notifier and can be implemented further for email_notifier or anything else as well.)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/A-STAR0/web_scraper_tool.git
    cd web_scraper_tool
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```

## Usage

### Authentication

All endpoints require an API key for authentication. Use the API key `engipper13` for accessing the endpoints.

### API Endpoints

- **Scrape
