#!/usr/bin/env python
import os
import sys


def setup_env():
    pathname = os.path.dirname(sys.argv[0])
    pathname = os.path.dirname(pathname)

    sys.path.append(os.path.abspath(pathname))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'fang.settings'
    import django
    django.setup()


setup_env()

import house.models as models

if __name__ == "__main__":
    houses = models.OldHouse.objects.all()
