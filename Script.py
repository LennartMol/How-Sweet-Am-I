import RequestSensorData
import ParseSensorData
import StatusQuotes
from pypresence import Presence
import privateInfo
import time

# set auth token and patient_id
RequestSensorData.setToken(privateInfo.email, privateInfo.password)
patient_id = RequestSensorData.getPatientId()

# make connection to Discord rich presence
RPC = Presence(privateInfo.client_id)
RPC.connect()

while True: 
    
    data = RequestSensorData.getData(patient_id)
    latest_measurement = ParseSensorData.getLatestMeasurement(data)
    BG_value = latest_measurement['Value']
    quote = StatusQuotes.getQuote(BG_value)

    RPC.update( state = "Glucose level: " + str(BG_value) + " mmol/L", 
                details = quote,
                large_image = "blood-sugar-roller-coaster",
                large_text = "Riding highs and lows like there's no tomorrow.")
    time.sleep(15)