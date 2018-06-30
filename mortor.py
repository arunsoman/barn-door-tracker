
class ReductionGear:
    def __init__(self, ratio):
        self.ratio = ratio
        self.steps = 0
        self.gear = None

    def attach_gear(self, gear):
        self.gear = gear

    def step(self):
        self.steps += 1
        if self.gear is None:
            raise AttributeError("No gear attached")
        self.gear.rotate(self.___angle())

    def ___angle(self):
        temp = self.steps % self.ratio
        if temp == 0:
            return 360
        return (temp / self.ratio) * 360


class Nema23:
    def __init__(self, reduction_gear_ratio=100):
        self.step_deg = 1.8
        self.step_cnt = 0
        self.reduction_gear = ReductionGear(reduction_gear_ratio)

    def step(self):
        self.step_cnt += 1
        self.reduction_gear.step()

    def angle(self):
        return self.step_deg * self.step_cnt % 360

    def attach_gear(self, rod_gear):
        self.reduction_gear.attach_gear(rod_gear)
