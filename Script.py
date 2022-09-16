import RequestSensorData
import ParseSensorData
import StatusQuotes
from pypresence import Presence
import time
import os

# fetch environment variables
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
client_id = os.environ.get('CLIENT_ID')
if email == None or password == None or client_id == None:
    print("\nMake sure to correctly set your environment variables.\n")
    exit()

# set auth token and patient_id
RequestSensorData.setToken(email, password)
patient_id = RequestSensorData.getPatientId()

# make connection to Discord rich presence
RPC = Presence(client_id)
RPC.connect()


while True: 
    data = RequestSensorData.getData(patient_id)
    latest_measurement = ParseSensorData.getLatestMeasurement(data)
    BG_value = latest_measurement['Value']
    info = StatusQuotes.getQuote(BG_value)

    RPC.update( state = "BG: " + str(BG_value) + " mmol/L - " + info["level"], 
                details = info["quote"],
                large_image = "blood-sugar-roller-coaster",
                large_text = "Riding highs and lows like there's no tomorrow.")
    time.sleep(15)