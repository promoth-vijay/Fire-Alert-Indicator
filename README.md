# Fire-Alert-Indicator

A random temperature sensor program used in here to send values to the AWS IoT core and the values are sent to aws Lambda function by message passing function in IoT core. If certain values comes larger than specified threshold value, the lambda function triggers the SNS and SES services to let the owner of the house and the fire engine department about the fire and the address of the house is attached with the message.
