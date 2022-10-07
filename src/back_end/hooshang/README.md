# ASD-Social Robot
 
# Add the following line to nginx sites-enabled/[my website's name] configuration file because your media files will be ignored by the browser if they are served with the default mimetype of text/plain : "include /etc/nginx/mime.types;"

# *NOTE* *If requirements.txt does not exist, run "pipreqs [path/to/ project]" to generate requirements.txt file for your project and install the requirements with pip install -r requirements.txt*

# The user-interface must be accessible from browser with the following address: http://[Jetson|Computer's IP address]:[port number(default:5353)]/index.html
# If you want to be able to access the user-interface from other devices in the same network, you should use the same url but replace the IP address with the IP address of the main server (e.g. Jetson).

## Android App ********************************************************************

### You must first fill in the url with the [IP address:port number] of the main server (e.g. Jetson). No need for the "/reqcli" part. *NOTE* *"http://" IS required though.*

### The android app starts listening on [user-given url:port number]/reqcli (in this case: ip:5353/reqcli) for requests from the user-interface. It then waites for an update in the json it recieves as a GET request and then changes the media output accordingly.

### It looks for changes in "audio_url" and "video_url" fields of the json and plays each media through a seprarate channel at the same time; Meaning that the user is not limited to playing video's audio only and can play any audio file with any video file.

#### After each action, the android app sends a POST request with the body being the status of the action (e.g. "Error!","Video played successfuly", etc.) All of which are then recieved by the user-interface(Back-end => Django: Views.py) and displayed to the user(front-end => index.html).

### If you want to stream a video or audio file from the server, you must first put the file in the "media" folder of the project and then use the following url to access it: http://[IP address:port number]/media/[file name].[file extension]
#### Additionaly, you can online stream a video or audio by sending the url of the stream server to the androind app, just like you would do with a local file. (It is recommended to use a local server for streaming though for faster response time and less bandwidth usage.) 

### The app is capable of playing any video or audio file that is supported by the android device (e.g. mp4, mp3, wav, etc.) and any video or audio stream that is supported by the android device (e.g. rtsp, rtmp, etc.) 
#### *NOTE* *This can be a little tricky if using a 4.4.0>= android device because it does not support some of the newer streaming protocols.*


# Web server run and debug*************************************************************

## You need a web server to run the project. I used nginx and gunicorn. You can use apache or any other web server. 
## To have direct access to the database, you need to be a superuser.
### To create a superuser, run the following command: python manage.py createsuperuser
#### Now you can access the database at /admin with admin privileges. (e.g. modify model objects, add new users, etc.)

## To run the project from scratch, run the following command: gunicorn --bind host:port --workers 3 --threads 2 --timeout 120 --log-level debug --log-file log.txt --access-logfile access_log.txt --error-logfile error_log.txt --capture-output --enable-stdio-inheritance --daemon --pid pid.txt --pythonpath [path/to/project] [project_name].wsgi:application

## To use the built-in django web-server, run the following command: python manage.py runserver. 
### However, the server must have automaticly been served by the web server (e.g. nginx) in production environment (e.g. Jetson Nano) and gunicorn service & socket in the background on each reboot.

### If not, check nginx status to make sure it is active and then check for errors in the log file: /var/log/nginx/error.log and /var/log/nginx/access.log. If you are using a different web server, check its log file.

### Also this could have happened because of failed gunicorn service. Check the status of gunicorn service with the following command: sudo systemctl status gunicorn and check gunicorn configuration file: /etc/systemd/system/gunicorn.service and gunicorn.socket configuration file: /etc/systemd/system/gunicorn.socket.

### *NOTE* *Make sure you have allowed the ports in use (e.g. 1935, 5353, 8080, etc.) in the firewall. To check the status of the firewall, run the following command: sudo ufw status. To allow a port, run the following command: sudo ufw allow [port number]. To allow a range of ports, run the following command: sudo ufw allow [port number]:[port number]*


# Additions to the project****************************************************************

## If you want to assign a static IP address to the Jetson Nano, you can use the following command: sudo nmtui.
### To check the IP address of the Jetson Nano, run the following command: hostname -I.
### To check the IP address of the computer, run the following command: ipconfig.

## If you want to deploy the project or assign a purchased domain name to the project, you must change the server_name in the nginx configuration file from localhost to the domain name. Be sure to configure the DNS settings of the domain name to point to the IP address of the server using cloudflare or any other DNS service provider.