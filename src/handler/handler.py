import abc

class HandlerError(Exception):
  """ Common Errors with Handler """
  pass

class Handler(HandlerError, metaclass=abc.ABCMeta):
  """ Common class for all Handlers """
  
  @abc.abstractmethod
  def save(self):
    return
