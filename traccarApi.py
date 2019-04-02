import json
import requests


class traccarApi:
    baseAddressApi = ""
    sessionApi = "session/"  # done
    deviceApi = "devices/"  # done
    positionApi = "positions/"  # done
    eventApi = "reports/events/"  # done
    routeApi = "reports/route/"  # done
    stopApi = "reports/stops/"  # done
    summaryApi = "reports/summary/"  # done
    tripsApi = "reports/trips/"  # done

    timeout = 30  ### response timeout in seconds
    user = ''
    _pass = ''

    def __init__(self, url, _user, _pass):
        self.baseAddressApi = url
        self.setLogin(_user=_user, _pass=_pass)

    def setLogin(self, _user, _pass):
        self.user = _user
        self._pass = _pass

    def getDevices(self):
        response = requests.get(self.baseAddressApi + self.deviceApi, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getPositions(self):
        response = requests.get(self.baseAddressApi + self.positionApi, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getRoutes(self, deviceId, startDate, endDate):
        params = {
            'deviceId': deviceId,
            'from': startDate.isoformat(),
            'to': endDate.isoformat()
        }
        response = requests.get(self.baseAddressApi + self.routeApi, params=params, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getEvents(self, deviceId, startDate, endDate, type='allEvents'):
        params = {
            'deviceId': deviceId,
            'from': startDate.isoformat(),
            'to': endDate.isoformat(),
            'type': type
        }
        response = requests.get(self.baseAddressApi + self.eventApi, params=params, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getStops(self, deviceId, startDate, endDate):
        params = {
            'deviceId': deviceId,
            'from': startDate.isoformat(),
            'to': endDate.isoformat(),
        }
        response = requests.get(self.baseAddressApi + self.stopApi, params=params, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getSummary(self, deviceId, startDate, endDate):
        params = {
            'deviceId': deviceId,
            'from': startDate.isoformat(),
            'to': endDate.isoformat(),
        }
        response = requests.get(self.baseAddressApi + self.summaryApi, params=params, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)

    def getTrips(self, deviceId, startDate, endDate):
        params = {
            'deviceId': deviceId,
            'from': startDate.isoformat(),
            'to': endDate.isoformat(),
        }
        response = requests.get(self.baseAddressApi + self.tripsApi, params=params, auth=(self.user, self._pass),
                                timeout=self.timeout)
        return json.loads(response.content)
