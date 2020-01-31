# eYIC19-20-Robotic-Learning-Platform

Index :
1. Project Proposal - 
    Project proposal for eYIC 2019-20.
2. Scratch code - 
    The code for the visual drag and drop programming language used in the project.
3. ezGPIO Python library - 
    The python library for easy control of the robot and its ports.
4. Front-end - 
    The GUI front page the user will see when accessing the robot's interface.
5. s3_extend - 
    The server used to recieve commands from the scratch programming language interface to the Raspberry Pi.

Directions to use : 
1. Install apache server on the Raspberry Pi.
2. Place the front-end code to the root directory of the apache server (usr/www/html).
3. Build the scratch project using npm and place it in the root directory of the apache server.
4. Configure Jupyter notebook to launch at start and use the 'http' method to serve the Jupyter notebook interface to another computer over the network. (https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)
5. Install the 'Python banyan server' using 'sudo pip3 install python-banyan'
6. Place the s3_extend folder at the folder where other pip packages are installed. (/usr/local/lib/python3.7/dist-packages)
7. Place the ezGPIO folder at the same folder as the above step.
8. Connect the robot to the host laptop via ethernet port. Then open any browser and go to the address "http://raspberrypi.local".
9. If the steps are followed correctly, you should see the front-end webpage of our project.
10. Further clicking on Scratch and Python should load up the scratch and jupyter notebook interfaces in new tabs.