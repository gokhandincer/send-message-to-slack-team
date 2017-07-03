import requests
from argparse import ArgumentParser

# first you need to generate webhook url https://my.slack.com/services/new/incoming-webhook/
# then after, choose your channel

# you can use this script as below:
# python send_message_to_slack_channel.py --webhook "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXX" --message "Hi, Slack Users" --channel "#alert"
# python send_message_to_slack_channel.py -w "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXX" -m "Hi, Slack Users" -c "#alert"

# Command  Lines Arguments
parser = ArgumentParser(description="Post to Slack Team")
parser.add_argument('--webhook', '-w', type=str)
parser.add_argument('--message', '-m', type=str)
parser.add_argument('--channel', '-c', type=str)
args = parser.parse_args()

webhook_url = args.webhook
channel = args.channel
username = "webhookbot"
icon_imoji = ":ghost:"

slack_data = '{"channel": "'+channel+'", "username": "'+username+'", "icon_imoji": "'+icon_imoji+'", "text": "'+args.message+'"}'

response = requests.post(webhook_url, data=slack_data, headers={'Content-Type': 'application/json'})

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)
