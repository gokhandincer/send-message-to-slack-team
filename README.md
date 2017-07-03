# run-fortigate-commands-over-ssh
**Before Run the Script**
first you need to generate webhook url https://my.slack.com/services/new/incoming-webhook/```
then after, choose your channel
**you can use this script as below:**
```
python send_message_to_slack_channel.py --webhook "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXX" --message "Hi, Slack Users" --channel "#general"
```
```
python send_message_to_slack_channel.py -w "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXX" -m "Hi, Slack Users" -c "#general"
```

*Options**
```
--webhook or -w
--message or -m
--channel or -c
```
