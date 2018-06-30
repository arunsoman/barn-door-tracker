from math import acos,cos
from rod import Rod, Gear
from mortor import Nema23
from driver import Nema_Driver



class c:
    arm = .234
    two_arms_sq = 2*arm*arm
    degressPerArcSecond = 0.00417807457

    def __c_len( degrees):
        arm = c.arm
        return 2*arm*arm*(1-cos(degrees))

    def angle_due_cord_length( cord_len):
        c_len_sq = cord_len**2
        x= (c.two_arms_sq-c_len_sq)/c.two_arms_sq
        return acos(x)

    def cord_length_after_count_steps( count):
        degrees=count*c.degressPerArcSecond
        return c.__c_len( degrees)

    def angle_due_to_count_steps( count):
        return  c.degressPerArcSecond*count



def test_const():
    l1=c.cord_length_after_count_steps(1)
    l2=c.cord_length_after_count_steps(10)
    print("cord len step  1={}, 10={}", l1, l2)
    a1 = c.angle_due_to_count_steps(1)
    a2 = c.angle_due_to_count_steps(10)
    print("angle step  1={}, 10={}", a1, a2)

test_const()



def simulate():
    rod = Rod(1, .3)
    rod_gear = Gear( 5, rod)
    motor = Nema23(reduction_gear_ratio=100)
    motor.attach_gear(rod_gear)
    driver = Nema_Driver(motor)

    driver.feedback(rod)
    driver.start_motor()
    result = []
    delta = []
    delta.append(0)
    for i in range(1, 60 * 60):
        result.append(cordPartial(computeP()))
    print(result)


