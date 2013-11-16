# import fabrics API functions - self-explanatory once you see 
from fabric.api import * 

env.shell = '/bin/bash'

def push_a_root():
    local('git push origin') # push al router
    
def push_y_deploy():
    local('git push origin') # push al router   
    run('/home/pi/git/pull.sh')# pull raspberry al router
    run('deploydjango')
  