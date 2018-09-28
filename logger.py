import traceback
import logging.config
import logging_config

logging.config.dictConfig(logging_config.LOGGING)


logger = logging.getLogger("kannada_chatbot")


def log_traceback():
    '''
    This method is used to formant stack trance
    :return:
    '''
    trace_back = traceback.format_exc().split("\n")
    trace_back.pop()  # removing empty string
    for line in trace_back:
        logger.error(line)
