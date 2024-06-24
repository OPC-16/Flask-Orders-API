# Flask Order Management Application

This project is a simple Flask application for managing orders and items. It demonstrates the usage of a factory function to create the Flask application, grouping routes using Blueprints, and using SQLite3 as the database.

## Features

- Create, read, and delete orders
- Each order can contain multiple items
- Uses SQLite3 as the database
- Organized code structure with factory function and Blueprints

## Prerequisites

- Python 3.x
- Flask
- SQLite3

## Running the Application

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Set the Flask application:
   ```bash
   export FLASK_APP=flask-orders-api
   export FLASK_ENV=development
   ```
5. Run the application:
   ```bash
   flask run
   ```
## Example Usage with cURL

### Create an Order
```bash
curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{"CustomerID": "C001", "Items": "Item1, Item2", "ShippedAt": "2023-06-11 12:00:00", "CompletedAt": "2023-06-15 15:00:00"}'
```

### Get an Order
```bash
curl -X GET http://127.0.0.1:5000/list/1
```

### Delete an Order
```bash
curl -X DELETE http://127.0.0.1:5000/delete/1
```
