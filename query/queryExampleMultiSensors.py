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
selectedUser = users[2]['UUID']
EDAQuery = 'select * from electro_dermal_activity where "user" = \'' + selectedUser + '\';'
print("Querying data: " + EDAQuery + " on User" + selectedUser)
EDAResponse = influxDBPhysioSignalClient.query(EDAQuery)
EDADataSamples = list(EDAResponse.get_points(measurement='electro_dermal_activity'))
numberOfEDADataSamples = len(EDADataSamples)

rrIntervalQuery = 'select * from heart where "user" = \'' + selectedUser + '\';'
print("Querying data: " + rrIntervalQuery + " on User" + selectedUser)
rrIntervalResponse = influxDBPhysioSignalClient.query(rrIntervalQuery)
rrIntervalDataSamples = list(rrIntervalResponse.get_points(measurement='heart'))
numberOfRrIntervalDataSamples = len(rrIntervalDataSamples)

temperatureQuery = 'select * from temperature where "user" = \'' + selectedUser + '\';'
print("Querying data: " + temperatureQuery + " on User" + selectedUser)
temperatureResponse = influxDBPhysioSignalClient.query(temperatureQuery)
temperatureDataSamples = list(temperatureResponse.get_points(measurement='temperature'))
numberOfTemperatureDataSamples = len(temperatureDataSamples)

print("Number of data samples in query: EDA - " + str(numberOfEDADataSamples) + " skinTemperature - " + str(numberOfTemperatureDataSamples) + " RrInterval - " + str(numberOfRrIntervalDataSamples))

# Sort the physiological data by date
sortedEDADataSamples = sorted(EDADataSamples, key=lambda k: k['time'])
sortedRrIntervalSamples = sorted(rrIntervalDataSamples, key=lambda k: k['time'])
sortedTemperatureSamples = sorted(temperatureDataSamples, key=lambda k: k['time'])

# format the data to be displayed as a xy plot
x1 = []
y1 = []
for EDASample in sortedEDADataSamples:
	if EDASample["type"] == "ElectroDermalActivity":
		# convert iso 8601 String date to datetime python object
	    x1.append( dateutil.parser.parse(EDASample['time']) )
	    y1.append( EDASample['electro_dermal_activity'])

x2 = []
y2 = []
for EDASample in sortedTemperatureSamples:
	if EDASample["type"] == "SkinTemperature":
		# convert iso 8601 String date to datetime python object
	    x2.append( dateutil.parser.parse(EDASample['time']) )
	    y2.append( EDASample['skin_temperature'])


x3 = []
y3 = []
for EDASample in sortedRrIntervalSamples:
	if EDASample["type"] == "RrInterval":
		# convert iso 8601 String date to datetime python object
	    x3.append( dateutil.parser.parse(EDASample['time']) )
	    y3.append( EDASample['rr_interval'])


plt.figure(1)                
ax1 = plt.subplot(311) 

# format date label 
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')

#plot graph 1
ax1.xaxis.set_major_formatter(xfmt)
x1 = md.date2num(x1)
ax1.plot_date(x1, y1, linestyle='-', linewidth=2, markersize=2)


ax2 = plt.subplot(312)            

#plot graph 2
ax2.xaxis.set_major_formatter(xfmt)
x2 = md.date2num(x2)
ax2.plot_date(x2, y2, linestyle='-', linewidth=2, markersize=2)


ax3 = plt.subplot(313)            

#plot graph 3
ax3.xaxis.set_major_formatter(xfmt)
x3 = md.date2num(x3)
ax3.plot_date(x3, y3, linestyle='-', linewidth=2, markersize=2)

# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
