import click
from models import Session, Cocktail, Customer, Order
from helpers import display_table
from datetime import datetime

session = Session()

@click.group()
def cli():
    """Maji-Mazuri Cocktail App - Manage cocktails, customers, and orders"""
    pass

# ====== COCKTAIL COMMANDS ======
@cli.group()
def cocktail():
    """Manage cocktails"""
    pass

@cocktail.command()
@click.option('--name', prompt=True, help='Name of the cocktail')
@click.option('--ingredients', prompt=True, help='List of ingredients')
@click.option('--price', prompt=True, type=float, help='Price of the cocktail')
@click.option('--category', prompt=True, help='Category of the cocktail')
def add(name, ingredients, price, category):
    """Add a new cocktail"""
    try:
        cocktail = Cocktail(name=name, ingredients=ingredients, price=price, category=category)
        session.add(cocktail)
        session.commit()
        click.secho(f" Added cocktail: {name}", bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

@cocktail.command()
def list():
    """List all cocktails"""
    cocktails = session.query(Cocktail).all()
    if not cocktails:
        click.echo("No cocktails found")
        return
    
    display_table(
        cocktails,
        headers=["ID", "Name", "Price", "Category"],
        columns=["id", "name", "price", "category"]
    )

@cocktail.command()
@click.option('--id', prompt='Cocktail ID', type=int, help='ID of the cocktail to update')
@click.option('--name', type=click.STRING, help='New name of the cocktail')

@click.option('--ingredients',type=click.STRING, help='New list of ingredients')
@click.option('--price',type=float, help='New price of the cocktail')
@click.option('--category',type=click.STRING, help='New category of the cocktail')
def update(id, name, ingredients, price, category):
    """Update a cocktail by ID"""
    try:
        cocktail = session.get(Cocktail, id)

        if not cocktail:
            click.secho(f"Cocktail with ID {id} not found!",bg='red')
            return
        
        if name: cocktail.name = name
        if ingredients: cocktail.ingredients = ingredients
        if price: cocktail.price = price
        if category: cocktail.category = category
        
        session.commit()
        click.secho(f"Updated Cocktail (ID: {id})", bg='green')

    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

@cocktail.command()
@click.option('--id', prompt='Cocktail ID', type=int, help='ID of the cocktail to delete')
def delete(id):
    """Delete a cocktail by ID"""
    try:
        cocktail = session.get(Cocktail,id)
        if not cocktail:
            click.secho(f"Cocktail with ID {id} not found!",bg='red')
            return
        
        session.delete(cocktail)
        session.commit()
        click.secho(f" Deleted cocktail (ID: {id})",bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

# ====== CUSTOMER COMMANDS ======
@cli.group()
def customer():
    """Manage customers"""
    pass

@customer.command()
@click.option('--name', prompt=True, help='Name of the customer')
@click.option('--email', prompt=True, help='Email of the customer')
@click.option('--phone', prompt=True, help='Phone number of the customer')
@click.option('--favorite', prompt=True, help="Customer's favorite drink")
def add(name, email, phone, favorite):
    """Add a new customer"""
    try:
        customer = Customer(name=name, email=email, phone=phone, favorite_drink=favorite)
        session.add(customer)
        session.commit()
        click.secho(f" Added customer: {name}", bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

@customer.command()
def list():
    """List all customers"""
    customers = session.query(Customer).all()
    if not customers:
        click.echo("No customers found")
        return
    
    display_table(
        customers,
        headers=["ID", "Name", "Email", "Favorite Drink"],
        columns=["id", "name", "email", "favorite_drink"]
    )

@customer.command()
@click.option('--id', prompt='Customer ID', type=int, help='ID of the customer to update')
@click.option('--name', type=click.STRING, help='New name of the customer')
@click.option('--email', type=click.STRING, help='New email of the customer')
@click.option('--phone',type=click.STRING, help='New phone number of the customer')
@click.option('--favorite', type=click.STRING, help="New favorite drink")
def update(id, name, email, phone, favorite):
    """Update a customer by ID"""
    try:
        customer = session.get(Customer,id)
        if not customer:
            click.secho(f"Customer with ID {id} not found!",bg='red')
            return
        
        if name: customer.name = name
        if email: customer.email = email
        if phone: customer.phone = phone
        if favorite: customer.favorite_drink = favorite
        
        session.commit()
        click.secho(f"Updated customer (ID: {id})", bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

@customer.command()
@click.option('--id', prompt='Customer ID', type=int, help='ID of the customer to delete')
def delete(id):
    """Delete a customer by ID"""
    try:
        customer = session.get(Customer,id)
        if not customer:
            click.secho(f"Customer with ID {id} not found!",bg='red')
            return
        
        session.delete(customer)
        session.commit()
        click.secho(f" Deleted customer (ID: {id})",bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

# ====== ORDER COMMANDS ======
@cli.group()
def order():
    """Manage orders"""
    pass

@order.command()
@click.option('--customer-id', prompt='Customer ID', type=int, help='ID of the customer')
@click.option('--cocktail-id', prompt='Cocktail ID', type=int, help='ID of the cocktail')
@click.option('--quantity', prompt='Quantity', type=int, default=1, help='Quantity to order')
def add(customer_id, cocktail_id, quantity):
    """Place a new order"""
    try:
        customer = session.get(Customer ,customer_id)
        cocktail = session.get(Cocktail,cocktail_id)
        
        if not customer:
            click.echo(f"❌ No customer found with ID {customer_id}")
            return
        if not cocktail:
            click.echo(f"❌ No cocktail found with ID {cocktail_id}")
            return
            
        order = Order(customer_id=customer_id, cocktail_id=cocktail_id, quantity=quantity)
        session.add(order)
        session.commit()
        click.secho(f" Added order: {customer.name} ordered {quantity}x {cocktail.name}", bg='green')
    except Exception as e:
        session.rollback()
        click.echo(f"❌ Error: {str(e)}")

@order.command()
def list():
    """List all orders"""
    orders = session.query(Order).all()
    if not orders:
        click.echo("No orders found")
        return
    
    display_table(
        orders,
        headers=["ID", "Customer", "Cocktail", "Quantity", "Status"],
        columns=["id", "customer.name", "cocktail.name", "quantity", "status"]
    )

@order.command()
@click.option('--id', prompt='Order ID', type=int, help='ID of the order to update')
@click.option('--customer-id', type=int, help='New customer ID')
@click.option('--cocktail-id', type=int, help='New cocktail ID')
@click.option('--quantity',type=int, help='New quantity')
@click.option('--status',type=click.STRING,help='New status (pending/completed/cancelled)')
def update(id, customer_id, cocktail_id, quantity, status):
    """Update an order by ID"""
    try:
        order = session.get(Order, id)
        if not order:
            click.secho(f"Order with ID {id} not found!",bg='red')
            return
        
        if customer_id: order.customer_id = customer_id
        if cocktail_id: order.cocktail_id = cocktail_id
        if quantity: order.quantity = quantity
        if status: order.status = status
        
        session.commit()
        click.secho(f"Updated order (ID: {id})", bg='green')

    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

@order.command()
@click.option('--id', prompt='Order ID', type=int, help='ID of the order to delete')
def delete(id):
    """Delete an order by ID"""
    try:
        order = session.get(Order, id)
        if not order:
            click.secho(f"Order with ID {id} not found!",bg='red')
            return
        
        session.delete(order)
        session.commit()
        click.secho(f" Deleted order (ID: {id})",bg='green')
    except Exception as e:
        session.rollback()
        click.secho(f"Error: {str(e)}",bg='red')

if __name__ == "__main__":
    cli()