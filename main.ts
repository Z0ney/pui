let distance = mbit_Sensor.Ultrasonic(DigitalPin.P14, DigitalPin.P15)
let speed = 90
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(4000)
basic.pause(200)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Left, speed)
basic.pause(500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(4500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_SpinRight, speed)
basic.pause(15)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(5000)
basic.pause(4100)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Right, speed)
basic.pause(500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(3000)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Right, speed)
basic.pause(500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(2000)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Left, speed)
basic.pause(500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(3000)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Left, speed)
basic.pause(500)
mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, speed)
basic.pause(2000)
mbit_Robot.CarCtrl(mbit_Robot.CarState.Car_Stop)
basic.forever(function () {
	
})
basic.forever(function () {
    huskylens.request()
    if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        basic.showIcon(IconNames.Heart)
    } else if (huskylens.isAppear(2, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        basic.showIcon(IconNames.SmallHeart)
    }
})
basic.forever(function () {
	
})
