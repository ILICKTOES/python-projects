import subprocess as linux
linux.run(['deskflow-core', 
           'client',
           '-f', 
           '--debug', 
           'INFO', 
           '--name', 
           'jake2',
           '--prevent-sleep',
           '--sync-language',
           '192.168.68.157:28000'
           ])