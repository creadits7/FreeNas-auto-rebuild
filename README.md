# FreeNas-auto-rebuild
Python script to initiate a disk replace on FreeNas automatically

I am no longer working with FreeNas so I doubt this will be finished anytime soon. 

FreeNas comes with a "replace" command but no way of automatically replacing a failed disk from a spare.

My solution was a script that runs on startup and loops, checking at the set interval to see if the pool is degraded, if it is, initiate a replace with the next available spare.
