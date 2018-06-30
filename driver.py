import sched
import time


class Nema_Driver:
    def __init__(self, nema):
        self.nema = nema
        self.scheduler = None
        self.stop = False
        self.feedback = None
        self.counter = 0

    def ___gen_pulse(self):
        if self.stop == False:
            self.counter += 1
            self.scheduler.enter(1, 1, self.___gen_pulse)
            self.nema.step()

    def start_motor(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.scheduler.enter(1, 1, self.___gen_pulse)

    def feedback(self, rod):
        self.feedback = rod

    def stop(self):
        self.stop = True

