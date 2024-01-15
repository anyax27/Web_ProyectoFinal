#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebProyectoFinal.settings')
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drj.settings")
>>>>>>> 70208ee41d45cebd45e60f04c58aa9ff5c5090e4
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> 70208ee41d45cebd45e60f04c58aa9ff5c5090e4
    main()
