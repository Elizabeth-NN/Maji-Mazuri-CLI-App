from maji_mazuri.models import Base
from sqlalchemy import create_engine
from logging.config import fileConfig
from alembic import context

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

def run_migrations_online():
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))
    
    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()