# address-book-api/README.md

# Address Book API

This is a minimal API for managing an address book using FastAPI and SQLite. Users can create, update, delete, and retrieve addresses with coordinates.

## Features

- Create, update, and delete addresses.
- Retrieve addresses within a specified distance from given coordinates.
- Built-in Swagger documentation for API interaction.

## Project Structure

```
address-book-api
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   └── address_service.py
│   └── utils
│       ├── __init__.py
│       └── distance_calculator.py
├── tests
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_services.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd address-book-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To create the database tables, run:
```
python -c "from app.database.database import Base, engine; from app.database import models; Base.metadata.create_all(bind=engine)"
```

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` in your browser to access the Swagger documentation and interact with the API.

## Environment Variables

Make sure to set up your `.env` file with the necessary configuration, such as the database connection string.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.