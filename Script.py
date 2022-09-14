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

    RPC.update(state= "BG:" + str(BG_value) + " - " + quote)
    time.sleep(15)