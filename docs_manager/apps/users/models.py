"""
models.py

Define o modelo de usuário da aplicação.

Este módulo contém a classe `User`, que representa um usuário do sistema.
Cada usuário possui um nome de usuário único e uma senha armazenada
de forma segura (hash).
"""

from django.db import models


class User(models.Model):
    """
    Representa um usuário do sistema.

    Campos:
        username (str): Nome de usuário único.
        password (str): Senha do usuário (armazenada como hash).
    """
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        """Retorna o nome de usuário como representação do objeto."""
        return self.username
