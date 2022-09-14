import requests
import privateInfo

# api-endpoint
api_endpoint = 'https://api-eu.libreview.io' 

headers= {
    # required headers
    'accept-encoding': 'gzip',
    'cache-control': 'no-cache',
    'connection': 'Keep-Alive',
    'content-type': 'application/json',
    'product': 'llu.android',
    'version': '4.3.0'
}

# create 'privateInfo.py' file with variable email and password
loginData = {
    "email": privateInfo.email,
    "password": privateInfo.password
}

def setToken(email, password):
    """ Requests authentication token and sets it automatically in the header files.

        Parameters:
        - Expects login credentials 
    """
    r = requests.post(url = api_endpoint + "/llu/auth/login", headers=headers, json=loginData)
    data = r.json()
    JWT_token = data['data']['authTicket']['token']
    extra_header_info = {'authorization': 'Bearer ' + JWT_token}
    headers.update(extra_header_info) 

def getPatientId():
    """ Requests and returns patient_id 
    """
    r = requests.get(url = api_endpoint + "/llu/connections", headers=headers)
    data = r.json()
    return data['data'][0]['patientId']

def getData(patient_id):
    """ Requests and returns data

        Parameters:
        - Patient_id 
    """
    r = requests.get(url = api_endpoint + "/llu/connections/" + patient_id + "/graph", headers=headers)
    return r.json()