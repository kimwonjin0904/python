#pip install mss
#pip install googletrans==4.0.0=rc1
import mss
with mss.mss() as sct:
    screen = sct.shot(output="screenshot.png")