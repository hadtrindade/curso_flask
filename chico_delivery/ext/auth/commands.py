import click
from chico_delivery.ext.auth.controller import create_user
from chico_delivery.ext.auth.models import User


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    create_user(
        email=email, password=passwd, admin=admin
    )
    # TODO: tratar execept User exists
    click.echo(f"Usuário {email} criado com sucesso!")

#TODO: mover para o controller


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")