# BIG DATA Pi 
This project is inspired by the [Open Source Big Data Toolbelt (OSBDET)](https://github.com/raulmarinperez/osbdet) by Raúl Marín ([LinkedIn](https://github.com/raulmarinperez) | [GitHub](https://www.linkedin.com/in/raulmarinperez/)) and provides an educational platform for Big Data on the Raspberry Pi (RPi).


![](/assets/raspberry-pi-4.png)


The newest version of the small single-board computer - the Raspberry Pi 4 B - is equipped with a faster processor and more RAM than its predecessors. This allows users to run more demanding applications while still benefitting from the energy efficiency of the ARM-Architecture. The RPi only uses 6.4W under full load, which is ~1/10 of a traditional light-bulb. 

---

## Technologies
This Ansible-Playbook installs and configures the following technologies:
- Apache Kafka [(message broker & storage)](https://kafka.apache.org/)
- Archiconda3 [(conda on 64bit arm)](https://github.com/Archiconda)
- Jupyter Lab [(next gen coding interface)](https://jupyterlab.readthedocs.io/en/stable/)
- Apache Spark [(stream processing)](https://spark.apache.org/)
- MariaDB [(storage)](https://mariadb.org/)
- Apache Superset [(visualization)](https://superset.apache.org/)
- Samba [(network file service)](https://www.samba.org/)

---

## HOW TO USE IT
### Prerequisites:
- a Raspberry Pi 4/400
- a USB-C power supply
- an SD Card
- admin access to your router
- recommended: a LAN-cable to connect to the router


### Set up your RPi: 
- flash Ubuntu 21.04 Server (64bit) on an SD-Card and start up your RPi [(link to tutorial)](https://itsfoss.com/install-ubuntu-server-raspberry-pi/)
- SSH into the RPi and put your SSH Key on it [(link to tutorial)](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
- Install Ansible on your Laptop/Desktop/control machine ([via pip](https://medium.com/@mitesh_shamra/introduction-to-ansible-e5b56ee76b8c) | [official documentation](https://docs.ansible.com/ansible/2.3/intro_installation.html#latest-releases-via-pip))
- download the contents of this repository with `git clone https://github.com/Maximilian-Pichler/BDPi`
- open the `hosts.ini` file and put the IP-Adress of your RPi in the second line.
- if you use additional storage, add the UUID and the Format-Type of your drive here too, otherwise leave these strings empty.
- execute `ansible-playbook playbook.yml` from the BDPi-Repository folder on your control machine.
- get something to drink...or eat. This will take a while.

## Have Fun
Once the installation is finished, the services are listening on the following ports:
|  Service  |  Port  | Password / Token  | user |
|-----------|--------|-------------------|------|
|SparkHub*  | 4040   |                   |      |
|Jupyter Lab| 8881   | abcd              |      |
| Maria DB  | 3306   | abcd              |ubuntu|
|Superset   | 8088   | abcd              |ubuntu|
|Network Storage|  445   | abcd              |ubuntu|

*only with an active Spark-Job

From a security standpoint this configuration is not ideal, but makes things easier to access.

---

## WHY ANSIBLE?
- because I was intrigued after reading about it. ([Deploy a Kafka Cluster with Ansible](https://towardsdatascience.com/deploy-a-kafka-cluster-with-terraform-and-ansible-21bee1ee4fb) | [short introduction video](https://www.ansible.com/resources/videos/quick-start-video))
- because I'm dumb: I needed something to automate my steps in case I had to start from scratch *...and this happened many, many, many times*.
- because I'm lazy: Ansible-Playbooks are human-readable and reduce the need for documentation.

---

## Upcoming Features (maybe)

- *Spark Cluster Integration*
- *BDPi on AWS*
- *VPN for remote access*
- *more operating systems (CentOS, Debian)*
- *more processor architectures (x64, armhf)*