
def getLatestMeasurement(data):
    """ Returns latest measurement information

        Parameters:
        - Expects data dictionary
    """
    latest_measurement = data['data']['connection']['glucoseMeasurement']['Value']
    return latest_measurement

def getAllMeasurements(data):
    """ Returns all measurements with information

        Parameters:
        - Expects data dictionary
    """
    all_measurements = data['data']['graphData']
    return all_measurements