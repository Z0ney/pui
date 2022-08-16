distance = mbit_Sensor.ultrasonic(DigitalPin.P14, DigitalPin.P15)
speed = 90
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(4000)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_LEFT, speed)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(10000)
basic.pause(4000)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RIGHT, speed)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(3000)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RIGHT, speed)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(2000)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_LEFT, speed)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(3000)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_LEFT, speed)
basic.pause(500)
mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, speed)
basic.pause(2000)
mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        basic.show_icon(IconNames.HEART)
    elif huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever2)

def on_forever3():
    pass
basic.forever(on_forever3)
