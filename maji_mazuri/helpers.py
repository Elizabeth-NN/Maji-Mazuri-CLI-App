import click
from tabulate import tabulate

def get_nested_attr(obj, attr_path):
    """Access nested attributes like 'customer.name'."""
    for attr in attr_path.split('.'):
        obj = getattr(obj, attr)
    return obj


def display_table(items, headers, columns):
    """Display a list of items in a formatted table"""
    table_data = []
    for item in items:
        row = [get_nested_attr(item, col) for col in columns]
        table_data.append(row)
    
    click.echo(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def validate_email(ctx, param, value):
    """Basic email validation"""
    if value and '@' not in value:
        raise click.BadParameter('Invalid email format')
    return value

def format_datetime(dt):
    """Format datetime for display"""
    return dt.strftime('%Y-%m-%d %H:%M') if dt else 'N/A'