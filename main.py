def on_forever():
    if mbit_Robot.Line_Sensor(mbit_Robot.enPos.LEFT_STATE, mbit_Robot.enLineState.WHITE) and mbit_Robot.Line_Sensor(mbit_Robot.enPos.RIGHT_STATE, mbit_Robot.enLineState.WHITE):
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 60)
    elif mbit_Robot.Line_Sensor(mbit_Robot.enPos.LEFT_STATE, mbit_Robot.enLineState.WHITE) and mbit_Robot.Line_Sensor(mbit_Robot.enPos.RIGHT_STATE, mbit_Robot.enLineState.BLACK):
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINRIGHT, 70)
    elif mbit_Robot.Line_Sensor(mbit_Robot.enPos.LEFT_STATE, mbit_Robot.enLineState.BLACK) and mbit_Robot.Line_Sensor(mbit_Robot.enPos.RIGHT_STATE, mbit_Robot.enLineState.WHITE):
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINLEFT, 70)
    elif mbit_Robot.Line_Sensor(mbit_Robot.enPos.LEFT_STATE, mbit_Robot.enLineState.BLACK) and mbit_Robot.Line_Sensor(mbit_Robot.enPos.RIGHT_STATE, mbit_Robot.enLineState.BLACK):
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
        mbit_Display.RGB2(DigitalPin.P0,
            DigitalPin.P0,
            DigitalPin.P0,
            mbit_Display.enColor.RED)
        basic.pause(5000)
basic.forever(on_forever)
