import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASES_USERNAME = os.getenv('DATABASES_USERNAME', 'postgres')
DATABASES_PASSWORD = os.getenv('DATABASES_PASSWORD', '1234')
DATABASES_HOST = os.getenv('DATABASES_HOST', 'localhost')
DATABASES_NAME = os.getenv('DATABASES_NAME', 'ecommerce')
TEST_DATABASES_NAME = os.getenv('TEST_DATABASES_NAME', 'ecommerce_test')