# PYTHON AUTOMATED SMS
## Send Automated SMS with HTTP API and Python Redis Queue (RQ)
>This project was developed to automate the birthday sms to the employees

### Minimum Requirements
>Python Version 3.6.x

>Redis Server

#### Install Redis Server
<pre><b>Ubuntu: <b><code>sudo apt-get install redis-server</code>
<b>Cent OS: <b><code>sudo yum install redis</code>
</pre>

#### Installation the App
```
git clone https://github.com/bitopan/automated_sms.git
cd automate_sms
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration
<pre><code>cp config.example.ini config.ini</code></pre>
Modify the config.ini file as per your credentials

#### Run the application
<pre><code>python app.py</code></pre>

>Running the application, queue will be created.
>To execute the queued jobs, run rq worker
<pre><code>rq worker</code></pre>

>Please note that you have to run the above command within the Python Virtual environment.

>Once the application is ready, to automate the <code>rq worker</code> you can create the service file systemd

>My rqworker.service file [Path: <code>/etc/systemd/system/rqworker.service</code>] looks like below:
```
[Unit]
Description=RQ Worker
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/bitopan/Workspace/Python/automated_sms/
Environment=LANG=en_US.UTF-8
Environment=LC_ALL=en_US.UTF-8
Environment=LC_LANG=en_US.UTF-8
ExecStart=/home/bitopan/Workspace/Python/automated_sms/venv/bin/rq worker
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true
Restart=always

[Install]
WantedBy=multi-user.target
```

>After creating the above file, you can simply run the rq worker as service.

>To start the service

<code>sudo service rqworker start</code>

>To stop the service

<code>sudo service rqworker stop</code>

#### Guides on Python RQ
https://python-rq.org/

>Finally Add <code>python app.py</code> to the crontab