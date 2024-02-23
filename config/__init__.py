import os
from . import dev,qa,prod,test

def loadConfig(app):
    # Load configuration based on environment
    if os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object(dev.Config)
    elif os.environ.get('FLASK_ENV') == 'stg':
        app.config.from_object(stg.Config)     
    elif os.environ.get('FLASK_ENV') == 'qa':
        app.config.from_object(qa.Config)    
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(prod.Config)
    elif os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object(test.Config)
    else:
        app.config.from_object(dev.Config)