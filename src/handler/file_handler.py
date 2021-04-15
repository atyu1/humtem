from handler import Handler

class FileHandler(Handler):
  """ Common class for all Handlers """
 
  def __init__(self, file_path='/var/humtemp/'):
    """ File handler which saves values to file """
    self.file_path = file_path 

  def save(self, value, timestamp):
    """ Save output to the file """
    with open(self.file_path, 'w') as FILE:
      FILE.write(','.join(timstamp, value))
