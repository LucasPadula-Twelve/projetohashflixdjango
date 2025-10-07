from django.apps import AppConfig
import os


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        # This import is done inside the method to avoid circular imports
        # when the app is initialized.
        from .models import Usuario

        # Get environment variables for admin email and password.
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        # Check if an admin user with the specified email already exists.
        if email and not Usuario.objects.filter(email=email).exists():
            # If no user exists, create a superuser.
            print("Criando superusuário padrão...")
            Usuario.objects.create_superuser(
                username="admin2",
                email=email,
                password=senha,
                is_active=True,
                is_staff=True
            )
