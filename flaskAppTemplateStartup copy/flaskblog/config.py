import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', 'your-stripe-secret-key')
    TEMPLATES_AUTO_RELOAD = True  # Optional: Reload templates on change
    template_folder = 'flaskblog/templates'  # Set the template folder if it's different
    static_folder = 'flaskblog/static'