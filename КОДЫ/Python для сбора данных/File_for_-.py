from ev3dev2.motor import OUTPUT_B, LargeMotor
import time

motor = LargeMotor(OUTPUT_B)

for volt in range(10, 51, 5):
    volt = -volt
    start_time = time.time()
    startPos = motor.position
    filename = "data_" + str(volt) + '.txt'
    file = open(filename, 'w')
    while time.time() - start_time < 1:
        delta_t = time.time() - start_time
        motor.run_direct(duty_cycle_sp=volt)
        pos = motor.position - startPos
        vel = motor.speed
        file.write(str(delta_t) + ", " + str(pos) + ", " + str(vel) + "\n")
    else:

        motor.stop()
        time.sleep(2)
    file.close()
