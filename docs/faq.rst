##########################
Frequently asked questions
##########################

This page contains frequently asked questions about fedora-happiness-packets.
It includes troubleshooting steps and other project details.


ERROR: Couldn't connect to Docker deamon at http+docker://localhost-is it running? 
    Verify the logged in user is member of the docker group.
    To verify logged in user run::

 	sudo usermod -aG docker ${USER}
    
    If logged in user is not member of the docker group add it using::

	sudo gpasswd -a${USER}

