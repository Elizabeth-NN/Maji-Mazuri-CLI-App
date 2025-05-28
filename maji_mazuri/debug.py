import click
from models import engine

def print_db_stats():
    """Print database statistics for debugging"""
    from models import Cocktail, Customer, Order, Session
    session = Session()
    
    click.secho("\nMaji-Mazuri Database Statistics:", fg='blue')
    click.secho(f"Cocktails: {session.query(Cocktail).count()}",fg='blue')
    click.secho(f"Customers: {session.query(Customer).count()}",fg='blue')
    click.secho(f"Orders: {session.query(Order).count()}",fg='blue')


print_db_stats()