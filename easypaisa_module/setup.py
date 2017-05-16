from distutils.core import setup

setup(
    name='easypaisa-module',
    version='0.0.1',
    packages=['migrations'],
    url='',
    license='MIT License',
    author='Qasim Gulzar',
    author_email='qasim.frt@gmail.com',
    description='',
    install_requires=['djangorestframework==3.6.3', 'markdown==2.6.8', 'psycopg2==2.7.1','django-filter==1.0.2']
)
