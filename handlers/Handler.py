from logger import *
from tornado import gen
import tornado

host = None
port = None


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):

        error_message_map = {
            400: "Required parameter is missing.",
            404: "page not found",
            500: "Service not available. Please try again"
        }

        error_message = error_message_map.get(status_code, "Unknown Error")

        if status_code in error_message_map.keys():
            self.write(
                {"error": {"statusCode": status_code, "message": error_message}})
        else:
            self.write('Unknown Error')


class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    """
    Default handler gonna to be used in case of 404 error
    """
    pass


class ServiceHandler(BaseHandler):
    def initialize(self, *args, **kwargs):
        global host, port
        logger.info("args %s keyword_args %s" % (args, kwargs))
        logger.info("request is %s",self.request)

    @gen.coroutine
    def post(self, **postargs):
        logger.info("POST keyword args %s", postargs)
        module = postargs['module']
        action = postargs['action']
        try:
            if module == "classifier" and action == "process":
                logger.info("processing the classifier")
            else:
                raise tornado.web.HTTPError(404)
        except Exception as e:
            log_traceback()

    @gen.coroutine
    def get(self, **getargs):
        logger.info("GET keyword args %s", getargs)
        module = getargs['module']
        action = getargs['action']
        try:
            if module == "classifier" and action == "reload":
                logger.info("Classifier reload...")
            else:
                raise tornado.web.HTTPError(404)
        except Exception as e:
            log_traceback()


