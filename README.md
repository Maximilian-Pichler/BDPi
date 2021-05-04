# BIG DATA Pi 
This project is inspired by the [Open Source Big Data Toolbelt (OSBDET)](https://github.com/raulmarinperez/osbdet) by Raúl Marín ([LinkedIn](https://github.com/raulmarinperez) | [GitHub](https://www.linkedin.com/in/raulmarinperez/)) and provides an educational platform with the following (Big Data) Technologies installed and configured:
- Apache Kafka (message broker and Storage)
- Jupyter Lab (development interface)
- Apache Spark (stream processing)
- MariaDB (storage)
- Apache Superset (visualization)
- Samba (network file service)

## HOW TO USE IT
To set up your RPi: 
- flash Ubuntu 21.04 Server (64bit on an SD-Card
- put that SD-Card into your RPi and start it up
- SSH into the RPi and put your SSH Key on it ([link to tutorial](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md))
- Install Ansible on your Laptop/Desktop/control machine ([via pip](https://medium.com/@mitesh_shamra/introduction-to-ansible-e5b56ee76b8c) | [official documentation](https://docs.ansible.com/ansible/2.3/intro_installation.html#latest-releases-via-pip))
- download the contents of this repository with `git clone https://github.com/Maximilian-Pichler/BDPi`
- open the `hosts.ini` file and change the IP-Adress in the second line to the one of your RPi and save it.
- (optional: if you want to use an external drive, add the UUID and the Format-Type of your drive here too.)
- execute `ansible-playbook playbook.yml -i hosts.ini` from the BDPi-Repository folder on your control machine.
- get something to drink...or eat. This will take a while.

## WHY ANSIBLE?
- because I was intrigued after reading about its capabilities. ([Deploy a Kafka Cluster with Terraform and Ansible](https://towardsdatascience.com/deploy-a-kafka-cluster-with-terraform-and-ansible-21bee1ee4fb) | [short introduction video](https://www.ansible.com/resources/videos/quick-start-video))
- because I am dumb: I'm no expert in setting up Servers or VMs, so I needed something to automate my steps in case I had to start from scratch because I messed up something *...and this happened many, many, many times*.
- because I am lazy: besides automating the setup, Ansible-Playbooks are human-readable and thus can be used for documenting the steps involved in this setup.


## Upcoming Features
- *Spark-Cluster Integration*
- *VPN for remote access*
- *more operating systems (CentOS, Debian)*
- *more processor architectures (x64, armhf)*