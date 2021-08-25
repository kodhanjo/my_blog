class Config:
    '''
    General configuration parent class
    '''
    # BLOG_API ='GET http://quotes.stormconsultancy.co.uk/random.json'
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    config_options = {
    'development': DevConfig,
    'production': ProdConfig
}