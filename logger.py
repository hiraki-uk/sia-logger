from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG

class Logger:
	__slots__ = ('logger',)

	def __init__(self, name=__name__):
		self.logger = getLogger(name)
		self.logger.setLevel(DEBUG)
		formatter = Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")

		# stdout
		handler = StreamHandler()
		handler.setLevel(DEBUG)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

		# file
		handler = handlers.RotatingFileHandler(filename='logger.log',
												encoding='utf-8',
												maxBytes=1048576,
												backupCount=3)
		handler.setLevel(DEBUG)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		del formatter, handler

	def debug(self, msg):
		self.logger.debug(msg)
	

	def info(self, msg):
		self.logger.info(msg)
	

	def warn(self, msg):
		self.logger.warning(msg)


	def critical(self, msg):
		self.logger.critical(msg)