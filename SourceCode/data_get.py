from urllib.request import urlopen
import json
from session_module import Session
from lapTime_module import Lap
from driver_module import Driver
from sort import MergeSort
from tkinter import messagebox

class Instance:
    sessions = []
    drivers = []
    laps = []
    selectedSession = None
    selectedFastLap = None

    def get_sessions(self):
        try:
            url = "https://api.openf1.org/v1/sessions?session_type=Race"
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            for i in data:
                session = Session(i['location'], i['session_name'], i['year'], i['session_key'])
                self.sessions.append(session)
        except Exception as e:
            print(f"Error fetching sessions: {e}")
            messagebox.showerror("Error", f"Failed to fetch sessions: {e}")

    def get_drivers(self, session):
        try:
            url = "https://api.openf1.org/v1/drivers?session_key=" + str(session.id)
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            for i in data:
                driver = Driver(i['full_name'], i['driver_number'])
                self.drivers.append(driver)
        except Exception as e:
            print(f"Error fetching sessions: {e}")
            messagebox.showerror("Error", f"Failed to fetch sessions: {e}")

    def get_laps(self, driver, session):
        try:
            url = "https://api.openf1.org/v1/laps?session_key=" + str(session.id)
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            for i in data:
                if i['driver_number'] == driver.number:
                    lap = Lap(i['lap_duration'], i['lap_number'])
                    self.laps.append(lap)
            lapCopy = [lap for lap in self.laps if lap.time != None]
            MergeSort.sort(lapCopy, 0, len(lapCopy) - 1)
            self.selectedFastLap = driver.name + "'s fastest lap was lap " + str(lapCopy[0])
            for j in range(0, len(self.laps)):
                if self.laps[j].time == None:
                    self.laps[j] = str(j + 1) + ": -:--.---"
                
        except Exception as e:
            print(f"Error fetching laps: {e}")
            messagebox.showerror("Error", f"Failed to fetch laps: {e}")
