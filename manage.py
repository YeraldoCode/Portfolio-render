#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Configuración para producción en Render
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')
    try:
        from django.core.management import execute_from_command_line  # type: ignore
        from django.conf import settings
        if not settings.DEBUG:
            import django.core.management.commands.runserver as runserver
            runserver.Command.default_port = os.environ.get('PORT', '8000')
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
