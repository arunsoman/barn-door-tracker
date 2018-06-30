import unittest


class Rod:
    def __init__(self, pitch, length):
        if pitch>length:
            raise ValueError("pitch can't be higher than length: unit:mm pitch:{} length:{} " ,pitch, length)
        self.pitch = pitch
        self.length = length
        self.current_protrude_length = 0

    def protrude(self, pitch_factor):
        delta = (pitch_factor * self.pitch)
        req = delta+self.current_protrude_length
        if req > self.length() or req< 0:
            raise ValueError("Can't go beyond {} and {} current value is {}" , 0, self.length(), req)
        self.current_protrude_length = req

    def length(self):
        return self.current_protrude_length

class TestRod(unittest.TestCase):
    def setUp(self):
        self.rod = Rod(pitch=2, length=.5)

    def test_spin_up(self):
        pass
    def test_spin_down(self):
        pass
    def test_spin_up_out_of_bound(self):
        pass
    def test_spin_down_out_of_bound(self):
        pass


class Gear:
    def __init__(self, rod, ratio):
        self.angle = 0
        self.rod = rod
        self.ratio = ratio
        self.step = 0

    def rotate(self, angle):
        self.angle += angle
        self.step += 1
        temp = self.step % self.ratio
        factor = 1 if temp == 0 else temp / self.ratio
        self.rod.protrude(factor)
