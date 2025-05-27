import logging
import click
from models import engine

def setup_logging():
    """Configure logging for debugging"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Enable SQLAlchemy logging
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def print_db_stats():
    """Print database statistics for debugging"""
    from models import Cocktail, Customer, Order, Session
    session = Session()
    
    click.echo("\nDatabase Statistics:")
    click.echo(f"Cocktails: {session.query(Cocktail).count()}")
    click.echo(f"Customers: {session.query(Customer).count()}")
    click.echo(f"Orders: {session.query(Order).count()}")


print_db_stats()