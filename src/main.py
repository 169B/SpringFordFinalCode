#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
RightMotors_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
RightMotors_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
RightMotors = MotorGroup(RightMotors_motor_a, RightMotors_motor_b)
LeftMotors_motor_a = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
LeftMotors_motor_b = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
LeftMotors = MotorGroup(LeftMotors_motor_a, LeftMotors_motor_b)
Right_front = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
Left_Front = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
digital_out_b = DigitalOut(brain.three_wire_port.b)
rotation_15 = Rotation(Ports.PORT15, False)
Lady_Brown_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
Lady_Brown_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
Lady_Brown = MotorGroup(Lady_Brown_motor_a, Lady_Brown_motor_b)
Inertial21 = Inertial(Ports.PORT5)
digital_out_g = DigitalOut(brain.three_wire_port.g)
optical_4 = Optical(Ports.PORT4)
intake = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)
digital_out_e = DigitalOut(brain.three_wire_port.e)
gps_3 = Gps(Ports.PORT3, 0.00, 5.00, MM, -90)
distance_11 = Distance(Ports.PORT11)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

remote_control_code_enabled = True
vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
message1 = Event()
forward_move = Event()
Back_move = Event()
Stop = Event()
turn_right = Event()
turn = Event()
calibrate = Event()
stop_initialize = Event()
Auto_Stop = Event()
turn_left = Event()
start_auto = Event()
intake_forward = Event()
intake_backward = Event()
DOon = False
LB = False
DOon2 = False
Blue = False
Red = False
Intake_Control = False
Intake_running = False
myVariable = 0
volocity = 0
Right_Axis = 0
Left_Axis = 0
IntakeStake = 0
Degree = 0
pi = 0
movement = 0
distance1 = 0
time1 = 0
rot = 0
turn1 = 0
LadyBrown_Up = 0
LadyBrown_score = 0
LadyBrown = 0
Right_turn = 0
Left_turn = 0
DriveState = 0
start = 0
Next = 0
dos = 0
tog = 0
error = 0
output = 0
Kp = 0
Ki = 0
Kd = 0
Dellay = 0
Distance_travled = 0
imput = 0
Proportional = 0
integral = 0
derivitive = 0
direction = 0
Previus_error = 0
AutoSelect = 0
X_Start = 0
Y_Start = 0
Y_End = 0
X_End = 0
Angle = 0
Distnce2 = 0
Distance2 = 0
Turn_Angle = 0

def Move_In_direction_Degree_Speed(Move_In_direction_Degree_Speed__Degree, Move_In_direction_Degree_Speed__Speed):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # LINKED WITH CURRENT PID FOR MOVEMENT VELOCITY
    LeftMotors.set_velocity(Move_In_direction_Degree_Speed__Speed, PERCENT)
    Left_Front.set_velocity(Move_In_direction_Degree_Speed__Speed, PERCENT)
    RightMotors.set_velocity(Move_In_direction_Degree_Speed__Speed, PERCENT)
    Right_front.set_velocity(Move_In_direction_Degree_Speed__Speed, PERCENT)

def Forward_PID_Distance_Max_Speed(Forward_PID_Distance_Max_Speed__Distance, Forward_PID_Distance_Max_Speed__Max_Speed):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CURRENT PID - DISTANCE IN INCHES
    # PID VALUES: 0.5 - 0.01 - 0.1 - 0.05
    error = 0
    Kp = 0.5
    Ki = 0.01
    Kd = 0.1
    Dellay = 0.05
    Distance_travled = 0
    Inertial21.set_rotation(0, DEGREES)
    RightMotors.set_velocity(5, PERCENT)
    Right_front.set_velocity(5, PERCENT)
    LeftMotors.set_velocity(5, PERCENT)
    Left_Front.set_velocity(5, PERCENT)
    RightMotors.set_position(0, DEGREES)
    Right_front.set_position(0, DEGREES)
    LeftMotors.set_position(0, DEGREES)
    Left_Front.set_position(0, DEGREES)
    while True:
        imput = Inertial21.rotation(DEGREES)
        error = 0 - imput
        Proportional = error
        Distance_travled = ((math.fabs(Right_front.position(DEGREES)) / 360) * (2.75 * pi) + ((math.fabs(Left_Front.position(DEGREES)) / 360) * (2.75 * pi) + ((math.fabs(RightMotors.position(DEGREES)) / 360) * (2.75 * pi) + (math.fabs(LeftMotors.position(DEGREES)) / 360) * (2.75 * pi)))) / 4
        integral = (integral + error) * Dellay
        derivitive = (error - Previus_error) * Dellay
        direction = Kp * Proportional + (Ki * integral + Kd * derivitive)
        Previus_error = error
        Move_In_direction_Degree_Speed((direction * Forward_PID_Distance_Max_Speed__Max_Speed) / 33, Forward_PID_Distance_Max_Speed__Max_Speed)
        RightMotors.spin(REVERSE)
        Right_front.spin(REVERSE)
        LeftMotors.spin(FORWARD)
        Left_Front.spin(FORWARD)
        if Forward_PID_Distance_Max_Speed__Distance < Distance_travled:
            RightMotors.stop()
            Right_front.stop()
            LeftMotors.stop()
            Left_Front.stop()
            break
        wait(5, MSEC)

def turn_heading_velocity_momentum(turn_heading_velocity_momentum__heading, turn_heading_velocity_momentum__velocity, turn_heading_velocity_momentum__momentum):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CURRENT ACCURATE TURN USING IMU
    Inertial21.set_rotation(0, DEGREES)
    if turn_heading_velocity_momentum__heading > Inertial21.rotation(DEGREES):
        while turn_heading_velocity_momentum__heading - turn_heading_velocity_momentum__momentum > Inertial21.rotation(DEGREES):
            RightMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Right_front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Left_Front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightMotors.spin(REVERSE)
            Right_front.spin(REVERSE)
            LeftMotors.spin(REVERSE)
            Left_Front.spin(REVERSE)
            wait(5, MSEC)
    else:
        while turn_heading_velocity_momentum__heading + turn_heading_velocity_momentum__momentum < Inertial21.rotation(DEGREES):
            RightMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Right_front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Left_Front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightMotors.spin(FORWARD)
            Right_front.spin(FORWARD)
            LeftMotors.spin(FORWARD)
            Left_Front.spin(FORWARD)
            wait(5, MSEC)
    RightMotors.stop()
    LeftMotors.stop()
    Right_front.stop()
    Left_Front.stop()
    turn1 = 1

def GPS_Move_to_X_Y_at_max_velocity_of_Velocity(GPS_Move_to_X_Y_at_max_velocity_of_Velocity__X, GPS_Move_to_X_Y_at_max_velocity_of_Velocity__Y, GPS_Move_to_X_Y_at_max_velocity_of_Velocity__Velocity):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    pass

def Red_Ring_Turn_Velocity(Red_Ring_Turn_Velocity__Turn_Velocity):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    pass

def Blue_Ring_Turn_Velocity(Blue_Ring_Turn_Velocity__Turn_Velocity):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    Forward_PID_Distance_Max_Speed(13, -30)
    Lady_Brown.spin_for(FORWARD, 450, DEGREES)
    wait(0.2, SECONDS)
    Lady_Brown.spin_to_position(0, DEGREES, wait=False)
    Forward_PID_Distance_Max_Speed(43, 50)
    Forward_PID_Distance_Max_Speed(5, 10)
    wait(0.2, SECONDS)
    digital_out_b.set(True)
    intake.spin(FORWARD)
    wait(0.2, SECONDS)
    turn_heading_velocity_momentum(135, 40, 1)
    wait(0.2, SECONDS)
    Forward_PID_Distance_Max_Speed(30, -70)
    Forward_PID_Distance_Max_Speed(3, 40)
    turn_heading_velocity_momentum(-9, 40, 1)
    Forward_PID_Distance_Max_Speed(18, -40)
    wait(1, SECONDS)
    Forward_PID_Distance_Max_Speed(10, 40)
    wait(0.8, SECONDS)
    turn_heading_velocity_momentum(-60, 40, 1)
    Forward_PID_Distance_Max_Speed(19, -40)
    wait(0.5, SECONDS)
    turn_heading_velocity_momentum(-70, 50, 1)
    wait(0.3, SECONDS)
    Lady_Brown.spin_for(FORWARD, 300, DEGREES)
    Forward_PID_Distance_Max_Speed(45, -25)

def all_stop():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # STOP ALL MOTORS FUNCTION
    RightMotors.stop()
    Right_front.stop()
    LeftMotors.stop()
    Left_Front.stop()
    Lady_Brown.stop()
    intake.stop()

def Stop_Intake():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # STOP INTAKE FUNTION
    Intake_running = True
    intake.stop()

def onevent_controller_1axis2Changed_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CONTROLLER jOYSTICK
    Right_Axis = controller_1.axis2.position()

def ondriver_drivercontrol_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # INTAKE CONTROLLER CONTROL
    while True:
        while Intake_Control:
            if controller_1.buttonR1.pressing():
                intake.set_velocity(80, PERCENT)
                intake.spin(FORWARD)
            elif controller_1.buttonR2.pressing():
                intake.set_velocity(80, PERCENT)
                intake.spin(REVERSE)
            else:
                intake.stop()
            wait(5, MSEC)
        wait(5, MSEC)

def onevent_controller_1axis3Changed_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CONTROLLER jOYSTICK
    Left_Axis = controller_1.axis3.position()

def ondriver_drivercontrol_1():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CONTROLLER MOTOR VELOCITY CONTROL
    remote_control_code_enabled = True
    DriveState = 1
    volocity = 200
    RightMotors.set_stopping(COAST)
    LeftMotors.set_stopping(COAST)
    Right_front.set_stopping(COAST)
    Left_Front.set_stopping(COAST)
    while True:
        if Right_Axis > 0:
            Right_Axis =  21.6 * Right_Axis ** 1/3
        else:
            Right_Axis = 21.6 * -(math.fabs(Right_Axis) ** 1/3)

        if Left_Axis > 0:
            Left_Axis = 21.6 * (Left_Axis) ** 1/3
        else:
            Left_Axis = 21.6 * -(math.fabs(Left_Axis) ** 1/3)

        while True:
            RightMotors.set_velocity(Right_Axis, PERCENT)
            LeftMotors.set_velocity(Left_Axis, PERCENT)
            Right_front.set_velocity(Right_Axis, PERCENT)
            Left_Front.set_velocity(Left_Axis, PERCENT)
            RightMotors.spin(FORWARD)
            LeftMotors.spin(REVERSE)
            Right_front.spin(FORWARD)
            Left_Front.spin(REVERSE)
            wait(5, MSEC)
        wait(5, MSEC)

def ondriver_drivercontrol_2():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CONTROLLER CLAMP CONTROL
    while True:
        if controller_1.buttonB.pressing():
            if DOon:
                digital_out_b.set(True)
                DOon = False
                wait(0.1, SECONDS)
            else:
                digital_out_b.set(False)
                DOon = True
                wait(0.1, SECONDS)
            wait(0.5, SECONDS)
        wait(5, MSEC)

def ondriver_drivercontrol_3():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CONTROLLER SWEEPER CONTROL
    while True:
        if controller_1.buttonA.pressing():
            if DOon2:
                digital_out_g.set(True)
                DOon2 = False
                wait(0.1, SECONDS)
            else:
                digital_out_g.set(False)
                DOon2 = True
                wait(0.1, SECONDS)
            wait(0.5, SECONDS)
        wait(5, MSEC)

def ondriver_drivercontrol_4():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # LADY BROWN MACROS AND INIT
    Lady_Brown.spin_to_position(0, DEGREES)
    rotation_15.set_position(300, DEGREES)
    Lady_Brown.set_timeout(1, SECONDS)
    Lady_Brown.set_velocity(40, PERCENT)
    while True:
        if controller_1.buttonDown.pressing() and 198 < rotation_15.position(DEGREES):
            Lady_Brown.set_velocity(40, PERCENT)
            Lady_Brown.set_stopping(COAST)
            Lady_Brown.spin(FORWARD)
            while not rotation_15.position(DEGREES) < 278:
                wait(5, MSEC)
            Lady_Brown.set_stopping(HOLD)
            Lady_Brown.stop()
        if controller_1.buttonUp.pressing():
            Lady_Brown.set_velocity(100, PERCENT)
            Lady_Brown.set_stopping(COAST)
            Lady_Brown.spin(FORWARD)
            while not rotation_15.position(DEGREES) < 152:
                wait(5, MSEC)
            Lady_Brown.set_stopping(HOLD)
            Lady_Brown.stop()
        if controller_1.buttonLeft.pressing():
            Lady_Brown.set_velocity(40, PERCENT)
            Lady_Brown.set_stopping(COAST)
            Lady_Brown.spin(REVERSE)
            while not 300 < rotation_15.position(DEGREES):
                wait(5, MSEC)
            Lady_Brown.set_stopping(HOLD)
            Lady_Brown.stop()
        wait(5, MSEC)

def when_started1():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    brain.screen.set_font(FontType.PROP20)
    while True:
        brain.screen.print("Team: ")
        if Blue:
            brain.screen.print("BLUE")
            brain.screen.next_row()
        elif Red:
            brain.screen.print("RED")
            brain.screen.next_row()
        else:
            brain.screen.print("OH NOO!!!")
            brain.screen.next_row()
        brain.screen.print("AVG Motor Temp:  ")
        brain.screen.print(((RightMotors.temperature(PERCENT) + LeftMotors.temperature(PERCENT)) + (Right_front.temperature(PERCENT) + Left_Front.temperature(PERCENT))) / 2, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.next_row()
        brain.screen.print("L.B  Position:")
        brain.screen.print(Lady_Brown.position(DEGREES), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.next_row()
        wait(5, MSEC)

def when_started2():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    while True:
        if Red:
            while Red:
                if optical_4.color() == Color.BLUE and optical_4.is_near_object():
                    digital_out_e.set(True)
                    while not (optical_4.color() == Color.RED and optical_4.is_near_object()):
                        wait(5, MSEC)
                    digital_out_e.set(False)
                wait(5, MSEC)
        elif Blue:
            while Blue:
                if optical_4.color() == Color.RED and optical_4.is_near_object():
                    digital_out_e.set(True)
                    while not (optical_4.color() == Color.BLUE and optical_4.is_near_object()):
                        wait(5, MSEC)
                    digital_out_e.set(False)
                wait(5, MSEC)
        else:
            controller_1.screen.print("NO AUTO!!!")
        wait(5, MSEC)

def when_started3():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # SENSING FOR ANTI-OBSTRUTION - GLOBAL
    while True:
        while Intake_running:
            if not intake.is_spinning():
                intake.spin(REVERSE)
                wait(0.5, SECONDS)
            wait(5, MSEC)
        wait(5, MSEC)

def when_started4():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CALIBRATE AND INIT
    optical_4.gesture_disable()
    optical_4.set_light(LedStateType.ON)
    optical_4.set_light_power(50, PERCENT)
    start = 1
    Degree = 0
    pi = 3.14159265359
    Lady_Brown.set_velocity(100, PERCENT)
    Lady_Brown.set_position(0, DEGREES)
    intake.set_velocity(80, PERCENT)
    movement = 0
    Intake_Control = True

def onevent_stop_initialize_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # INIT
    RightMotors.set_stopping(BRAKE)
    LeftMotors.set_stopping(BRAKE)
    Right_front.set_stopping(BRAKE)
    Left_Front.set_stopping(BRAKE)
    Lady_Brown.set_stopping(BRAKE)
    intake.set_stopping(BRAKE)
    RightMotors.set_velocity(0, PERCENT)
    LeftMotors.set_velocity(0, PERCENT)
    Right_front.set_velocity(0, PERCENT)
    Left_Front.set_velocity(0, PERCENT)
    RightMotors.set_max_torque(100, PERCENT)
    LeftMotors.set_max_torque(100, PERCENT)
    Right_front.set_max_torque(100, PERCENT)
    Left_Front.set_max_torque(100, PERCENT)

def onauton_autonomous_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # GLOBAL FINAL AUTONOMOUS SELECTION
    remote_control_code_enabled = False
    Inertial21.calibrate()
    while Inertial21.is_calibrating():
        sleep(50)
    stop_initialize.broadcast()
    intake.set_velocity(70, PERCENT)
    Red = True
    digital_out_g.set(True)
    turn_heading_velocity_momentum(30, 10, 1)
    wait(0.5, SECONDS)
    digital_out_g.set(False)
    turn_heading_velocity_momentum(-73, 30, 1)
    Forward_PID_Distance_Max_Speed(35, 40)
    digital_out_b.set(True)
    intake.spin(FORWARD)
    turn_heading_velocity_momentum(3, 40, 1)
    Forward_PID_Distance_Max_Speed(30, -40)
    wait(1, SECONDS)
    Forward_PID_Distance_Max_Speed(17, 40)
    turn_heading_velocity_momentum(168, 40, 1)
    Forward_PID_Distance_Max_Speed(35, -40)
    wait(1, SECONDS)
    turn_heading_velocity_momentum(168, 40, 1)
    Forward_PID_Distance_Max_Speed(35, -40)

def onevent_Stop_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # STOP DRIVE FUNCTION
    RightMotors.stop()
    Right_front.stop()
    LeftMotors.stop()
    Left_Front.stop()
    RightMotors.stop()

def when_started5():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # ---------------------------------------------------------------------------------------------------------------------------------------------------AUTONOMOUS SELECTOR-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    AutoSelect = 0
    while True:
        if AutoSelect == 1:
            controller_1.screen.set_cursor(1, 1)
            AutoSelect = 1
            controller_1.screen.print("RED LEFT RING")
        else:
            if AutoSelect == 2:
                controller_1.screen.set_cursor(1, 1)
                AutoSelect = 2
                controller_1.screen.print("BLUE RIGHT RING")
            else:
                if AutoSelect == 3:
                    controller_1.screen.set_cursor(1, 1)
                    AutoSelect = 3
                    controller_1.screen.print("RED RIGHT STAKE")
                else:
                    if AutoSelect == 4:
                        controller_1.screen.set_cursor(1, 1)
                        AutoSelect = 4
                        controller_1.screen.print("BLUE LEFT STAKE")
                    else:
                        controller_1.screen.clear_screen()
                        controller_1.screen.set_cursor(1, 1)
                        AutoSelect = 0
                        controller_1.screen.print("NO AUTO")
        wait(5, MSEC)

def onevent_controller_1buttonL1_pressed_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    controller_1.screen.clear_screen()
    if AutoSelect == 5:
        AutoSelect = 0
    AutoSelect = AutoSelect + 1
    controller_1.rumble("-.-.")

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )
    driver_control_task_1 = Thread( ondriver_drivercontrol_1 )
    driver_control_task_2 = Thread( ondriver_drivercontrol_2 )
    driver_control_task_3 = Thread( ondriver_drivercontrol_3 )
    driver_control_task_4 = Thread( ondriver_drivercontrol_4 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()
    driver_control_task_1.stop()
    driver_control_task_2.stop()
    driver_control_task_3.stop()
    driver_control_task_4.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.axis2.changed(onevent_controller_1axis2Changed_0)
controller_1.axis3.changed(onevent_controller_1axis3Changed_0)
stop_initialize(onevent_stop_initialize_0)
Stop(onevent_Stop_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
ws4 = Thread( when_started4 )
ws5 = Thread( when_started5 )
when_started1()
