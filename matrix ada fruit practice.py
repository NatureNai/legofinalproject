import time
import board
import busio
from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)

matrix = matrix.Matrix8x8(i2c)

col_max = 8
row_max = 8

matrix.fill(0)
col = 0
row = 0

while True:
    while col < col_max:
        matrix[row, col] =2
        col+=1
        time.sleep(.2)
        
    if row < row_max:
        row += 1
        col = 0
        
    else:
        row = col = 0
        matrix.fill(0)
        
        #https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Matrix_7-Segment_LED_Backpack_Raspberry_Pi/matrix8x8_test/code.py
