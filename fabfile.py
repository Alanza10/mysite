# import fabrics API functions - self-explanatory once you see 
from fabric.api import * 

def push():
    local('git push origin') # runs the command on the local environment
    #run('cd //to/project/; git pull') # runs the command on the remote environment 
