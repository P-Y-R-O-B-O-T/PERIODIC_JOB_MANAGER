import dbus
import time
import datetime
import json
import os
import subprocess
import threading

#$$$$$$$$$$#

THREADS = {}

class PERIODIC_JOB_MANAGER :
    def __init__(self) -> None :
        self.START_TIME = time.time()
        self.STATUS = True

        self.load_job_data()
        self.initialize_complete_data_structure()

    def interval_job_manager_thread(self) -> None :
        while self.STATUS :
            time.sleep(1)
            for _ in self.JOB_DATA :
                self.check_and_execute_job(_)

    def load_job_data(self) -> None :
        file = open("/home/{}/.config/PERIODIC_JOB_MANAGER/periodic_job_manager.json"
                    .format("kushl"), "r")
        self.JOB_DATA = json.load(file)

    def initialize_complete_data_structure(self) -> None :
        for _ in self.JOB_DATA :
            self.JOB_DATA[_]["LAST_RUN"] = None

    def check_and_execute_job(self,
                              job: str) -> None :
        now = datetime.datetime.now()

        if self.JOB_DATA[job]["LAST_RUN"] == None :
            print("first_run")
            if ((time.time() - self.START_TIME) >
                self.JOB_DATA[job]["MIN_TIME_TO_START"]) :

                self.execute_job(job)

        if "INTERVAL" in self.JOB_DATA[job] :
            if (((time.time() - self.JOB_DATA[job]["LAST_RUN"]) >
                 self.JOB_DATA[job]["INTERVAL"]) and
                (time.time() - self.JOB_DATA[job]["LAST_RUN"] > 1)) :

                self.execute_job(job)

        if "TIME" in self.JOB_DATA[job] :
            for _ in self.JOB_DATA[job]["TIME"] :
                if ((now.hour == _[0]) and (now.minute == _[1]) and (time.time() - self.JOB_DATA[job]["LAST_RUN"] > 60)) :
                    print("time_run_executed")
                    self.execute_job(job)
                    break

    def execute_job(self,
                    job: str) -> None :
        global THREADS

        if self.JOB_DATA[job]["TYPE"] == "ONESHOT" :
            print("\t\t\toneshot")
            os.system(self.JOB_DATA[job]["COMMAND"])
            self.JOB_DATA[job]["LAST_RUN"] = time.time()
            return

        if job in THREADS :
            if THREADS[job].is_alive() : return
            if THREADS[job].is_alive() : del THREADS[job]

        THREADS[job] = threading.Thread(target=os.system,
                                        args=(self.JOB_DATA[job]["COMMAND"],))
        THREADS[job].start()
        self.JOB_DATA[job]["LAST_RUN"] = time.time()


    def start(self) -> None :
        self.INTERVAL_THREAD = threading.Thread(target=self.interval_job_manager_thread)
        self.INTERVAL_THREAD.start()

    def stop(self) -> None :
        self.STATUS = False

#$$$$$$$$$$#

if __name__ == "__main__" :
    PERIODIC_JOB_MANAGER_OBJ = PERIODIC_JOB_MANAGER()
    PERIODIC_JOB_MANAGER_OBJ.interval_job_manager_thread()
"""
while True :
    print("Hello")
"""
