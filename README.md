# Backend Test

This API retrieve data from Yahoo Finance APIs into a MySQL database and identify dividends for an specific symbol (e.g. "PETR4.SA"). This API has an edpoint that summarize amount of dividends per year based on the symbol.

## Summary

- [Usage](#usage)
- [API Documentation](#api-documentation)

## Usage

To install and run the project locally, follow these steps:

1. Go to the project directory
2. Create a python venv
3. Activate the venv
5. Install the dependencies from the 'requirements.txt' file.
6. Set up the MySQL database:
   - Create a MySQL database with the name backendtest
   - Configure the database connection in the `settings.py` file, with the correct IP, User and Password
7. Run database migrations
8. Start the development server: `python manage.py runserver`
3. Access the API endpoint: `http://localhost:8000/api/v1/dividends/<symbol>/<year>/` (GET)
   This endpoint will fill the database with the info retrived from Yahoo and show an Response to the user.
   The data will be an JSON with the <year> an the amount of dividend for that specific <symbol> and specific <year>.

## API Documentation

- `<symbol>`: This variable represents the symbol of a financial instrument or stock for which you want to retrieve dividend information. Replace `<symbol>` with the specific symbol you are interested in, such as "PETR4.SA".
- `<year>`: This variable represents the year for which you want to retrieve dividend data. Replace `<year>` with the desired year, such as "2023" for the year 2023.
