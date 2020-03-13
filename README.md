# SEND AUTOMATED SMS With HTTP API AND PYTHON

>This project was developed to automate the birthday sms to the employees

### Minimum Requirements
>Python Version 3.6.9

#### Installation the App
<pre><code>git clone https://github.com/bitopan/automated_sms.git
cd automate_sms
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</code></pre>

#### Install Redis Server
<pre><b>Ubuntu: <b><code>sudo apt-get install redis-server</code>
<b>Cent OS: <b><code>sudo yum install redis</code>
</pre>

### Configuration
<pre><code>cp config.example.ini config.ini</code></pre>
Modify the config.ini file as per your credentials

#### Running the application
<pre><code>python app.py</code></pre>
