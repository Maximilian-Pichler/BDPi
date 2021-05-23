# BIG DATA Pi 
This project is inspired by Raúl Marín's ([LinkedIn](https://github.com/raulmarinperez) | [GitHub](https://www.linkedin.com/in/raulmarinperez/)) project [Open Source Big Data Toolbelt (OSBDET)](https://github.com/raulmarinperez/osbdet) and provides an educational platform for Big Data technologies on the Raspberry Pi (RPi).


![](/assets/raspberry-pi-4.png)


The newest version of the small single-board computer - the Raspberry Pi 4 B - is equipped with a faster processor and more RAM than its predecessors. This allows users to run more demanding applications while still benefitting from the energy efficiency of the ARM-Architecture. The RPi only uses 6.4W under full load, which is ~1/10 of a traditional light-bulb. 

---

## Technologies
This Ansible-Playbook installs and configures the following technologies:
- Archiconda3 [(conda on 64bit arm)](https://github.com/Archiconda)
- Apache Kafka [(message broker & storage)](https://kafka.apache.org/)
- Apache Spark [(stream processing)](https://spark.apache.org/)
- Apache Superset [(visualization)](https://superset.apache.org/)
- Jupyter Lab [(next gen coding interface)](https://jupyterlab.readthedocs.io/en/stable/)
- MariaDB [(storage)](https://mariadb.org/)
- Samba [(network file service)](https://www.samba.org/)

---

## HOW TO USE IT

### Prerequisites:
- a Raspberry Pi 4/400 (4Gb+)
- a USB-C power supply
- a boot drive (SD card or [USB 3 stick](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md))
- admin access to your router
- recommended: a LAN-cable to connect to the router


### Initial Setup: 
- install Ubuntu 21.04 Server (64bit) on your RPi [(link to tutorial)](https://itsfoss.com/install-ubuntu-server-raspberry-pi/)
- SSH into the RPi and put your SSH Key on it [(link to tutorial)](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
- Install Ansible on your Laptop/Desktop/control machine ([via pip](https://medium.com/@mitesh_shamra/introduction-to-ansible-e5b56ee76b8c) | [official documentation](https://docs.ansible.com/ansible/2.3/intro_installation.html#latest-releases-via-pip))

### Run the Ansible Playbook
- download this repository to your control machine with `git clone https://github.com/Maximilian-Pichler/BDPi`
- open the `hosts.ini` file and put the IP-Adress of your RPi in the second line.
- if you use additional storage, add the UUID and the Format-Type of your drive here too, otherwise leave these strings empty.
- execute `ansible-playbook playbook.yml` from the BDPi-Repository folder on your control machine.
- get something to drink...or eat. This will take a while.*
    - *The time it takes to run the playbook heavily depends on your boot drive. A USB 3 stick is the preferred choice and reduces the time needed to approx. 45min*

## Have Fun
Once the installation is finished, the services are listening on the following ports:
|Service        |Port |Password / Token| user |
|---------------|-----|----------------|------|
|SparkHub*      |4040 |                |      |
|Jupyter Lab    |8881 |abcd            |      |
|Maria DB       |3306 |abcd            |ubuntu|
|Superset       |8088 |abcd            |ubuntu|
|Network Storage|445  |abcd            |ubuntu|

*only with an active Spark-Job

From a security standpoint this configuration is not ideal, but makes things easier to access.

---

## WHY ANSIBLE?
- Because I wanted to learn it after reading about its capabilities. ([Deploy a Kafka Cluster with Ansible](https://towardsdatascience.com/deploy-a-kafka-cluster-with-terraform-and-ansible-21bee1ee4fb) | [short introduction video](https://www.ansible.com/resources/videos/quick-start-video))
- Because I mess things up and automation makes starting from scratch less painful.
- Because I'm lazy. Ansible-Playbooks are easy-to-read/understand and reduce the need for documentation.

---

## UPCOMING FEATURES (maybe)
- *Continuous Integration Workflow on selfhosted GitLab*
- *Spark Cluster Integration*
- *VPN for remote access*