import yara
import os
import time

rules = yara.compile(filepath='rules.yar') 

path_to_watch = '/home/user/monitored_directory'

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  for added_file in added:
    filepath = os.path.join(path_to_watch, added_file)
    if rules.match(filepath):
      print(f'Yara rule match on {filepath}')
  before = after 
  time.sleep (1)