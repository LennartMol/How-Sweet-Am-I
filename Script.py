import RequestSensorData
import ParseSensorData
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
    RPC.update(state="Current bloodsugar: " + str(latest_measurement['Value']))
    time.sleep(15)
