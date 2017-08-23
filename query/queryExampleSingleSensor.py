import configparser
import boto3
from boto3.dynamodb.conditions import Key, Attr
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil.parser
from influxdb import InfluxDBClient

# Get user credentials 
userConfig = configparser.ConfigParser()
userConfig.read('credentials.cfg')

dynamoDBCredentialsSection = "DynamoDB Credentials"
influxDBCredentialsSection = "InfluxDB Credentials"
try:
	dynamoDB_acces_key_id = userConfig.get(dynamoDBCredentialsSection, "acces_key_id")
	dynamoDB_secret_acces_key = userConfig.get(dynamoDBCredentialsSection, "secret_acces_key")
	aws_region = userConfig.get(dynamoDBCredentialsSection, "aws_region")

	influxDB_url = userConfig.get(influxDBCredentialsSection, "database_url")
	influxDB_port = userConfig.get(influxDBCredentialsSection, "database_port")
	influxDB_user = userConfig.get(influxDBCredentialsSection, "username")
	influxDB_password = userConfig.get(influxDBCredentialsSection, "password")
except Exception:
	print("Please set up valid credentials \n")


# Connect to NoSql DynamoDB database 
dynamodb = boto3.resource(
						 'dynamodb',
                          aws_access_key_id=dynamoDB_acces_key_id,
                          aws_secret_access_key=dynamoDB_secret_acces_key,
                          region_name=aws_region)

# Get Every Users UUID 
userTable = dynamodb.Table('Users')
response = userTable.scan(Select="SPECIFIC_ATTRIBUTES", AttributesToGet=["UUID"])

numberOfUsers = response['Count']
print("Number of users in db: " + str(numberOfUsers))
users = response['Items']
print(users)


# Connect to InfluxDB database
InfluxDBPhysioSignalDBName = "physio_signal"
InfluxDBSensitiveEventDBName = "sensitive_event"
influxDBPhysioSignalClient = InfluxDBClient(influxDB_url, influxDB_port, influxDB_user, influxDB_password, InfluxDBPhysioSignalDBName)

# Get physiological data for a specific user
selectedUser = users[8]['UUID']
physioSignalQuery = 'select * from heart where "user" = \'' + selectedUser + '\';'
print("Querying data: " + physioSignalQuery + " on User" + selectedUser)
response = influxDBPhysioSignalClient.query(physioSignalQuery)

physioDataSamples = list(response.get_points(measurement='heart'))
numberOfDataSamples = len(physioDataSamples)
print("Number of data samples in query: " + str(numberOfDataSamples))

# Sort the physiological data by date
sortedPhysioDataSamples = sorted(physioDataSamples, key=lambda k: k['time'])
import json
with open('PartialNight-01-08.dat', 'w') as outfile:
    json.dump(sortedPhysioDataSamples, outfile)

# format the data to be displayed as a xy plot (x-axis = date, y-axis= RrInterval)
x = []
y = []
for dataSample in sortedPhysioDataSamples:
	if dataSample["type"] == "RrInterval":
		# convert iso 8601 String date to datetime python object
	 	if dataSample['rr_interval'] < 2000 and dataSample['rr_interval'] > 500:
		    x.append( dateutil.parser.parse(dataSample['time']) )
		    y.append( dataSample['rr_interval'])

# format date label 
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis.set_major_formatter(xfmt)

#plot
x = md.date2num(x)
plt.gca().plot_date(x, y, linestyle='-', linewidth=2, markersize=2)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
