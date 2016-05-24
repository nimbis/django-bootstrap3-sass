from setuptools import setup, find_packages


setup(
    name='django-bootstrap3-sass',
    version='3.3.6',
    author='Nimbis Services, Inc.',
    author_email='info@nimbisservices.com',
    description='Bootstrap 3 (Sass) static files for Django.',
    url='https://github.com/nimbis/django-bootstrap3-sass',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

