import forex_python
import boto3
import json
from datetime import datetime
from forex_python.converter import CurrencyRates

s3_client = boto3.client("s3")
sns_client = boto3.client('sns')

def get_exchange_rates():
    try:
        time_now = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
        rates = CurrencyRates().get_rates('USD')

        file_name = '/home/ubuntu/xchange/data/'+time_now+'.json'
        with open(file_name, "w") as file: 
            json.dump(rates, file)

        s3_name = 'data/'+time_now+'.json'
        s3_client.upload_file(file_name, '155446843238-exchange-rates', s3_name);
    except Exception as error:
        send_failure_notification(error)


def send_failure_notification(error):
    sns_client.publish(
        TargetArn = 'arn:aws:sns:us-east-2:155446843238:exchange_rate_job',
        Subject = 'Oops! Exchange Rate Job Failure',        
        Message = 'Something went wrong with your exchange rate job \n' + str(error)
    )


get_exchange_rates()

