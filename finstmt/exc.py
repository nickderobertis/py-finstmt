
class NotACalculatedItemException(Exception):
    pass


class NoSuchItemException(Exception):
    pass


class CouldNotParseException(Exception):
    pass


class ForecastException(Exception):
    pass


class ForecastNotFitException(ForecastException):
    pass


class ForecastNotPredictedException(ForecastException):
    pass


class ImproperManualForecastException(ForecastException):
    pass