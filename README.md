# BIG DATA Pi 
This project is inspired by the [Open Source Big Data Toolbelt (OSBDET)](https://github.com/raulmarinperez/osbdet) by Raúl Marín ([LinkedIn](https://github.com/raulmarinperez) | [GitHub](https://www.linkedin.com/in/raulmarinperez/)) and provides an educational platform of Big Data Technologies. It is intended for educational purposes and might be helpful in personal projects.

## HOW TO USE IT
To set up your RPi: 
- flash Ubuntu 21.04 Server (64bit on an SD-Card
- put that SD-Card into your RPi and start it up
- SSH into the RPi and put your SSH Key on it ([link to tutorial](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md))
- Install Ansible on your Laptop/Desktop (aka control machine) [via pip](https://docs.ansible.com/ansible/2.3/intro_installation.html#latest-releases-via-pip)
- download the contents of this repository with `git clone https://github.com/Maximilian-Pichler/BDPi`
- open the `hosts.ini` file and change the IP-Adress in the second line to the one of your RPi and save it.
- (optional: if you want to use an external drive, add the UUID and the Format-Type of your drive here too.)
- execute `ansible-playbook playbook.yml -i hosts.ini` from the BDPi-Repository folder on your control machine.
- get something to drink...or eat. This will take a while.

## WHY ANSIBLE?
- Because I was intrigued after reading about its capabilities [(short video)](https://www.ansible.com/resources/videos/quick-start-video).
- Because I am dumb: I'm no expert in setting up these environments, so I needed something that automates my steps, in case I have to reset the RPi because of some misconfiguration...and this happened many, many times.
- Because I am lazy: besides automating the setup, Ansible-Playbooks are human-readable (perfect for Beginners like me) and thus can be used for documenting the steps involved in this setup.
