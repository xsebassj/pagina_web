#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():
    load_dotenv()
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pagina.settings')

    PORT = os.getenv('DJANGO_PORT')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if 'runserver' in sys.argv and PORT:
        sys.argv.append(PORT)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
