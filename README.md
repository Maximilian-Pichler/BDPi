# BIG DATA Pi 

This project is inspired by the [Open Source Big Data Toolbelt (OSBDET)](https://github.com/raulmarinperez/osbdet) by Raúl Marín ([LinkedIn](https://github.com/raulmarinperez) | [GitHub](https://www.linkedin.com/in/raulmarinperez/)) and provides an educational platform of Big Data Technologies. It is intended for educational purposes, and might be useful for personal projects.

## HOW TO USE IT
In order to setup your RPi: 
- flash Ubuntu 21.04 Server 64bit on an SD-Card
- put that SD-Card into your RPi and start it up
- SSH into the RPi and put your SSH Key on it [Tutorial Link](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
- Install Ansible on your Laptop/Desktop (aka control machine) [via pip](https://docs.ansible.com/ansible/2.3/intro_installation.html#latest-releases-via-pip)
- download the contents of this repository with `git clone https://github.com/Maximilian-Pichler/BDPi`
- open the `hosts.ini` file and change the IP-Adress in the second line to the one of your RPi and save it.
- execute `ansible-playbook playbook.yml -i hosts.ini` from the BDPi folder on you control machine.
- get something to drink...or eat, this will take a while.


## WHY ANSIBLE?
Ansible automates the provisioning and setup of the technologies, and is human readable.