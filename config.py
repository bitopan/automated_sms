import configparser

config = configparser.ConfigParser()
config.read('config.ini')
SMS_URL = config.get('sms_gateway', 'url')
SMS_UNAME = config.get('sms_gateway', 'uname')
SMS_PASS = config.get('sms_gateway', 'pass')
SMS_SEND = config.get('sms_gateway', 'send')
SMS_PRIORITY = config.get('sms_gateway', 'priority')

EMPLOYEE_FILE = config.get('files', 'data_file')