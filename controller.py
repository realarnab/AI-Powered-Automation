import pyfirmata

comport = 'COM4'
board = pyfirmata.Arduino(comport)
led_1=board.get_pin('d:7:o')
led_2=board.get_pin('d:6:o')
led_3=board.get_pin('d:5:o')
led_4=board.get_pin('d:4:o')

def led(total):
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
    elif total == 1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
    elif total == 2:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
    elif total == 3:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
    elif total == 4:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
    elif total == 5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
