import RequestSensorData
import ParseSensorData
import json
from pypresence import Presence
import privateInfo
import time

# make connection to Discord rich presence
RPC = Presence(privateInfo.client_id)
RPC.connect()

while True: 
    data = RequestSensorData.getData()
    latest_measurement = ParseSensorData.getLatestMeasurement(data)
    RPC.update(state="Current bloodsugar: " + str(latest_measurement['Value']))
    time.sleep(15)
