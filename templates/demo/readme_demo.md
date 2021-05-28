## Demo
If you installed the demo, you could now open superset by typing `<raspberry-pi-ip-adress>:8088` into the browser of your choice. 
Once you are logged in, you can add a new database connection with the following URI: `mysql://ubuntu:abcd@localhost:3306/crypto`. 

![](/images/add_database.png)
![](/images/database_uri.png)

Then import the dashboard-file from the git repository folder `templates/demo/superset_crypto.json`.
Now you can access the dashboard.
![](/images/dashboard.png)

If you want to see how the demo works, you can find the according files in the folder `~/projects/demo/`.

Finally, if you want to disable the autostart of the demo, then enter the following two command lines:

```
systemctl disable superset_crypto_consumer && systemctl stop superset_crypto_consumer

systemctl disable superset_crypto_producer && systemctl stop superset_crypto_producer
```