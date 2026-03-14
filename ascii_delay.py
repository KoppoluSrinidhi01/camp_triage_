import time

hourglass = [
"   __",
"  /  \\",
"  \\  /",
"   \\/",
"   /\\",
"  /  \\",
"  \\__/"
]

def show_hourglass():
    for line in hourglass:
        print(line)
        time.sleep(1)

    time.sleep(10)