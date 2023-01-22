from m5stack import *
from m5stack_ui import *
from uiflow import *
from easyIO import *
import time
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)
tof_1 = unit.get(unit.TOF, unit.PAHUB1)
tof_2 = unit.get(unit.TOF, unit.PAHUB2)
tof_3 = unit.get(unit.TOF, unit.PAHUB3)
vibrator_0 = unit.get(unit.VIBRATOR, unit.PORTB)
vibrator_1 = unit.get(unit.VIBRATOR, unit.PORTC)


distance = None
left_hip_distance = None
right_hip_distance = None



label0 = M5Label('label0', x=99, y=0, color=0xa328b9, font=FONT_MONT_48, parent=None)
label1 = M5Label('label1', x=93, y=79, color=0xa328b9, font=FONT_MONT_48, parent=None)
label2 = M5Label('label2', x=88, y=161, color=0xa328b9, font=FONT_MONT_48, parent=None)


# Describe this function...
def head_sensor():
  global distance, left_hip_distance, right_hip_distance
  distance = tof_1.distance
  label0.set_text(str(distance))
  if distance <= 1500:
    power.setVibrationEnable(True)
    if distance < 150:
      power.setVibrationIntensity(100)
    elif distance < 200:
      power.setVibrationIntensity(100)
      for count in range(1):
        power.setVibrationEnable(True)
        wait_ms(60)
        power.setVibrationEnable(False)
        wait_ms(30)
        power.setVibrationEnable(True)
        wait_ms(60)
        power.setVibrationEnable(False)
        wait_ms(30)
    elif distance < 400:
      power.setVibrationIntensity(50)
    elif distance < 600:
      power.setVibrationIntensity(40)
    elif distance < 800:
      power.setVibrationIntensity(30)
    elif distance < 1200:
      power.setVibrationIntensity(20)
    elif distance < 2000:
      power.setVibrationIntensity(15)
    else:
      power.setVibrationIntensity(0)
  else:
    power.setVibrationEnable(False)

# Describe this function...
def left_hip():
  global distance, left_hip_distance, right_hip_distance
  left_hip_distance = tof_2.distance
  label1.set_text(str(left_hip_distance))
  if left_hip_distance <= 1000:
    if left_hip_distance < 150:
      analogWrite(26, 80)
    elif left_hip_distance < 200:
      analogWrite(26, 70)
    elif left_hip_distance < 400:
      analogWrite(26, 50)
    elif left_hip_distance < 600:
      analogWrite(26, 40)
    elif left_hip_distance < 800:
      analogWrite(26, 30)
    elif left_hip_distance < 1200:
      analogWrite(26, 20)
    elif left_hip_distance < 1500:
      analogWrite(26, 10)
    else:
      analogWrite(26, 0)
  else:
    vibrator_0.off()

# Describe this function...
def right_hip():
  global distance, left_hip_distance, right_hip_distance
  right_hip_distance = tof_3.distance
  label2.set_text(str(right_hip_distance))
  if right_hip_distance <= 1000:
    if right_hip_distance < 150:
      analogWrite(14, 80)
    elif right_hip_distance < 200:
      analogWrite(14, 70)
    elif right_hip_distance < 400:
      analogWrite(14, 50)
    elif right_hip_distance < 600:
      analogWrite(14, 40)
    elif right_hip_distance < 800:
      analogWrite(14, 30)
    elif right_hip_distance < 1200:
      analogWrite(14, 20)
    elif right_hip_distance < 1500:
      analogWrite(14, 10)
    else:
      analogWrite(14, 0)
  else:
    vibrator_1.off()



screen.set_screen_bg_color(0x000000)
screen.set_screen_brightness(80)
while True:
  head_sensor()
  left_hip()
  right_hip()
  wait_ms(2)
