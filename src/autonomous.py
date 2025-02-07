
from main import *
from PID import *
from autoselect import *
from init import *
from turn import *

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