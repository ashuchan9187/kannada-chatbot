'''
This class is used as the logging configuration for this application
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'kannada_chatbot': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'filter': 'custom',
            'propagate': False
        },
        'root': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
    }
}
