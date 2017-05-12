import configparser
import boto3
from boto3.dynamodb.conditions import Key, Attr
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil.parser


# Get user credentials 
userConfig = configparser.ConfigParser()
userConfig.read('credentials.cfg')

credential_section = "Credentials"
try:
	acces_key_id = userConfig.get(credential_section, "acces_key_id")
	secret_acces_key = userConfig.get(credential_section, "secret_acces_key")
	aws_region = userConfig.get(credential_section, "aws_region")
except Exception:
	print("Please set up valid credentials \n")

# Connect to NoSql DynamoDB database 
dynamodb = boto3.resource(
						 'dynamodb',
                          aws_access_key_id=acces_key_id,
                          aws_secret_access_key=secret_acces_key,
                          region_name=aws_region)

# Get Every Users UUID 
userTable = dynamodb.Table('Users')
response = userTable.scan(Select="SPECIFIC_ATTRIBUTES", AttributesToGet=["UUID"])

numberOfUsers = response['Count']
print("Number of users in db: " + str(numberOfUsers))
users = response['Items']
print(users)

# Collect Physiological Raw Data  
physioSignalTable = dynamodb.Table('PhysioSignal')

# We filter on a specific user and a specific day 
response = physioSignalTable.query(
	IndexName='User-index',
	KeyConditionExpression=Key('User').eq(users[1]['UUID'])
	)


numberOfDataSamples = response['Count']
print("Number of data samples in query: " + str(numberOfDataSamples))
physioDataSamples = response['Items']

# Sort the physiological data by date
sortedPhysioDataSamples = sorted(physioDataSamples, key=lambda k: k['Timestamp']) 

# format the data to be displayed as a xy plot (x-axis = date, y-axis= RrInterval)
x = []
y = []
for dataSample in sortedPhysioDataSamples:
	if dataSample["Type"] == "RrInterval":
		# convert iso 8601 String date to datetime python object
		x.append( dateutil.parser.parse(dataSample['Timestamp']) )
		y.append( dataSample['RrInterval'])

# format date label 
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis.set_major_formatter(xfmt)

#plot
x = md.date2num(x)
plt.gca().plot_date(x, y, linestyle='-', linewidth=2, markersize=2)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
