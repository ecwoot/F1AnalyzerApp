from urllib.request import urlopen
import json
from session_module import Session
from lapTime_module import Lap
from driver_module import Driver
from sort import MergeSort
from meeting_module import Meeting

class Instance:
    meetings = []
    sessions = []
    drivers = []
    laps = []
    latest = None
    selectedFastLap = None

    def get(self, url):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            print(e)

    def get_latest(self):
        url = "https://api.openf1.org/v1/sessions?session_key=latest"
        i = self.get(url)
        self.latest = Session(i[0]['location'], i[0]['session_name'], i[0]['year'], i[0]['session_key'])

    def get_meetings(self):
        url = "https://api.openf1.org/v1/meetings"
        data = self.get(url)
        self.meetings.clear()
        for i in data:
            self.meetings.append(Meeting(i['meeting_name'], i['year'], i['meeting_key']))


    def get_sessions(self, id):
        url = "https://api.openf1.org/v1/sessions?meeting_key=" + str(id)
        data = self.get(url)
        self.sessions.clear()
        for i in data:
            session = Session(i['location'], i['session_name'], i['year'], i['session_key'])
            self.sessions.append(session)

    def get_res(self, session):
        url = "https://api.openf1.org/v1/position?session_key=" + str(session.id)
        data = self.get(url)
        nums = set()
        self.get_drivers(session)
        for i in reversed(data):
            if i['driver_number'] not in nums:
                nums.add(i['driver_number'])
                for driver in self.drivers:
                    if i['driver_number'] == driver.number:
                        driver.set_pos(i['position'])
                if len(nums) == 20:
                    break
        MergeSort.sort(self.drivers, 0, len(self.drivers) - 1, key=lambda driver: driver.pos)

    def get_drivers(self, session):
        url = "https://api.openf1.org/v1/drivers?session_key=" + str(session.id)
        data = self.get(url)
        self.drivers.clear()
        for i in data:
            driver = Driver(i['full_name'], i['driver_number'], i['team_name'], i['team_colour'])
            self.drivers.append(driver)

    def get_laps(self, session):
        url = "https://api.openf1.org/v1/laps?session_key=" + str(session.id)
        data = self.get(url)
        self.laps.clear()
        for i in data:
            lap = Lap(i['lap_duration'], i['lap_number'], i['driver_number'])
            if lap.time != None:
                self.laps.append(lap)

        MergeSort.sort(self.laps, 0, len(self.laps) - 1, key=lambda lap: lap.time)
        self.selectedFastLap = "Fastest lap was lap " + str(self.laps[0])
        for j in range(0, len(self.laps)):
            if self.laps[j].time == None:
                self.laps[j] = str(j + 1) + ": -:--.---"
