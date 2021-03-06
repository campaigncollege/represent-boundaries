import os
import sys

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'travis_ci_test',
                'USER': 'postgres' if os.getenv('CI', False) else '',
            }
        },
        ROOT_URLCONF='boundaries.urls',
        INSTALLED_APPS=(
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.gis',
            'boundaries',
        ),
        MIDDLEWARE_CLASSES=(),
    )
    if hasattr(django, 'setup'):  # Django 1.7
        django.setup()

if __name__ == '__main__':
    # @see https://docs.djangoproject.com/en/1.6/releases/1.6/#discovery-of-tests-in-any-test-module
    # @see https://docs.djangoproject.com/en/1.6/releases/1.6/#new-test-runner
    try:
        from django.test.runner import DiscoverRunner
        runner = DiscoverRunner(failfast=False)
    except ImportError:  # Django < 1.6
        from django.test.simple import DjangoTestSuiteRunner
        runner = DjangoTestSuiteRunner(failfast=False)
    failures = runner.run_tests(['boundaries'])
    sys.exit(failures)
