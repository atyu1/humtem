import abc

class SensorError(Exception):
  """ Common Errors with Sensor """
  pass

class Sensor(SensorError, metaclass=abc.ABCMeta):
  """ Common class for all Sensors """
  
  @abc.abstractmethod
  def run(self):
    return
