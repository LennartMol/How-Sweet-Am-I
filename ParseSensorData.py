
def getLatestMeasurement(data):
    """ Returns latest measurement information

        Parameters:
        - Expects data dictionary
    """
    
    all_measurements = data['data']['graphData']
    latest_measurement = all_measurements[len(all_measurements) - 1]
    return latest_measurement

def getAllMeasurements(data):
    """ Returns all measurements with information

        Parameters:
        - Expects data dictionary
    """
    all_measurements = data['data']['graphData']
    return all_measurements