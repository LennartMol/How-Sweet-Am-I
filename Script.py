from ast import Param
import RequestSensorData
import ParseSensorData
import json

data = RequestSensorData.getData()

latest_measurement = ParseSensorData.getLatestMeasurement(data)
print("\nLatest measurement: \n" + json.dumps(latest_measurement) + "\n")
