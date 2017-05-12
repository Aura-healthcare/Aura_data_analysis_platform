# Headline #
The **Aura** device will alert an user from an epilepsy seizure within few minutes notice.
**Aura data analysis platform** provides a set of tools to easily acces and analyse anonymized patient data.

# Quick Start #

 - install python 3, pip and virtualenv

 - clone the repository

```
        git clone https://github.com/clecoued/Aura_data_analysis_platform.git
```
 - create a new python [virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) in the repository
```
        cd Aura_data_analysis_platform
        virtualenv myProject
```
 - install python package dependencies
```
        pip install -r requirements.txt
```
 - get your personnal credentials file *credentials.cfg* and copy it to *Aura_data_analysis_platform/query/credentials.cfg*
 - launch the demo script
```
        cd query
        python queryExample.py
```
 - Success !

# API #
## Database

Data are stored in a DynamoDB (NoSql) database on a Cloud. 
We acces it using python Amazon library [boto3](http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html) 

The database is divided into 2 tables:

- **Users** *stores the users list under format:*
```javascript
// User sample
{
    "UUID": "0399a758-da41-4fa5-aa30-625bc19c92ac" //(String) User UUID 
}
```
- **PhysioSignal** *stores the data samples under format:*
```javascript
// Generic Data sample
{
    "UUID": "eee9f933-701a-454f-b713-aa7755b3b6a3", //(String) Data sample UUID
    "Timestamp": "2017-05-05T11:59:34.365", //(String) Data sample timestamp stored following iso8601 format
    "User": "", //(String) User UUID on which has been recorded the data sample
    "Type": "RrInterval", //(String) Data sample type - RrInterval, ElectroDermalActivity, Temperature ...
}
```

We store differents physiological parameters:

- Cardiac R-R interval
- Electro dermal activity *(soon documented)*
- Skin external temperature *(soon documented)*


```javascript
// Specific R-R interval data sample field
{
    "RrInterval": "850" //(Integer) cardiac rr interval value in milliseconds 
}
```


