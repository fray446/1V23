import ctypes
from playsound import playsound

ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\\Users\\p09s3203\\Desktop\\py\\jony.jpg', 0)

playsound('eblan.mp3')
