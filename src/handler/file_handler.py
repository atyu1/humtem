from handler import Handler

class File_Handler(Handler):
  """ Common class for all Handlers """
 
  def __init__(self, filename='/var/humtemp/file.csv'):
    """ File handler which saves values to file """
    self.filename = filename 

  def save(self, value, timestamp):
    """ Save output to the file """
    with open(self.filename, 'w') as FILE:
      FILE.write(','.join(timstamp, value))
