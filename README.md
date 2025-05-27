# Maji-Mazuri-CLI-App

Maji-Mazuri-App is  CLI based.It is designed to healp a cocktail bar owner manage cocktail,customer and orders information.

## Relationships:
A cocktail and a customer have an indirect relationship
A customer can have many cocktail orders and a single cocktail can have many orders.Therefore a customer and a cocktail have a many to many relationship.
The orders table acts as a bridge table between customer and cocktail.

## file structure
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── maji_mazuri
│   ├── __init__.py
│   ├── __pycache__
│   │   └── models.cpython-312.pyc
│   ├── cli.py
│   ├── debug.py
│   ├── helpers.py
│   └── models.py
└── maji_mazuri.db



