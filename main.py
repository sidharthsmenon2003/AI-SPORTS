import datetime

class BiometricData:
    def _init_(self):
        self.hrv_data = []
        self.sleep_data = []
        self.other_data = []

    def record_hrv(self, hrv):
        self.hrv_data.append((datetime.datetime.now(), hrv))

    def record_sleep(self, sleep_hours):
        self.sleep_data.append((datetime.datetime.now(), sleep_hours))

    def record_other_data(self, data):
        self.other_data.append((datetime.datetime.now(), data))

    def get_hrv_data(self):
        return self.hrv_data

    def get_sleep_data(self):
        return self.sleep_data

    def get_other_data(self):
        return self.other_data

# Create a class for the athlete
class Athlete:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        self.biometric_data = BiometricData()

    def record_hrv(self, hrv):
        self.biometric_data.record_hrv(hrv)

    def record_sleep(self, sleep_hours):
        self.biometric_data.record_sleep(sleep_hours)

    def record_other_data(self, data):
        self.biometric_data.record_other_data(data)

    def get_hrv_data(self):
        return self.biometric_data.get_hrv_data()

    def get_sleep_data(self):
        return self.biometric_data.get_sleep_data()

    def get_other_data(self):
        return self.biometric_data.get_other_data()

    def get_health_status(self):
        latest_hrv = self.biometric_data.get_hrv_data()[-1][1]
        latest_sleep = self.biometric_data.get_sleep_data()[-1][1]
        if latest_hrv > 100 and (latest_sleep < 6 or latest_sleep > 8):
            return "Bad Health"
        elif latest_hrv > 100 or (latest_sleep < 6 or latest_sleep > 8):
            return "Fair Health"
        else:
            return "Good Health"

# Example usage:

# Create an athlete
name = input("Enter athlete's name: ")
age = int(input("Enter athlete's age: "))
athlete = Athlete(name, age)

# Record HRV data
hrv_data = float(input("Enter HRV data: "))
athlete.record_hrv(hrv_data)

# Record sleep data
sleep_hours = float(input("Enter sleep hours: "))
athlete.record_sleep(sleep_hours)

# Get health status
