cluster_command
===============
Simple rpc client server that provides execution of a command on many machines

Usage
=====
./remote-command.py “the command” --360 --720 --1080 --background

The options shown are configurable in the config.json file. For example, the --720 option will include all hosts in the cluster named 720.


./remote-command-server.py

This is to be ran on all of the hosts you wish to control.

Scripts
=====
./reset.sh 
will kill python and re-run the server (good for doing updates or killing other python programs without killing the server).

./reset_all.sh
will run the command using remote-command.py to reset 360, 720, and 1080 hosts

./load_experiment.sh
starts the scoot player on all hosts with the correct resolution for each host.


TODO
====
Remove hard coded variables (should all be from config.json)
Fix bug: confirmation of 2 commands ago and not the most recent.
