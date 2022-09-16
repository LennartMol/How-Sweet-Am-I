import RequestSensorData
import ParseSensorData
import StatusQuotes
from pypresence import Presence
import time
import os

# fetch environment variables
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
client_id = os.environ.get("CLIENT_ID")
if email == None or password == None or client_id == None:
    print(f"\nMake sure to correctly set your environment variables.\n")
    exit()

# set auth token and patient_id
RequestSensorData.setToken(email, password)
patient_id = RequestSensorData.getPatientId()


# make connection to Discord rich presence
def connectToPresence():
    global RPC 
    RPC = Presence(client_id)
    try:
        RPC.connect()
    except:
        print(f"\n{time.strftime('%H:%M:%S')} - Discord is closed. Make sure to have it running.")

connectToPresence()

while True: 
    
    data = RequestSensorData.getData(patient_id)
    latest_measurement = ParseSensorData.getLatestMeasurement(data)
    BG_value = latest_measurement['Value']
    info = StatusQuotes.getQuote(BG_value)

    try:
        RPC.update( state = f"BG: {BG_value} mmol/L - {info['level']}", 
                    details = info['quote'],
                    large_image = "blood-sugar-roller-coaster",
                    large_text = "Riding highs and lows like there's no tomorrow.")
        print(f"\n{time.strftime('%H:%M:%S')} - Updated Discord playing status.")
    except:
        connectToPresence()
    time.sleep(15)