# -----------
# NEW FASHION
from pathlib import Path

print( Path(__file__) )              # Relative path to the program file
print( Path(__file__).absolute() )   # Absolute path to the program file

print( Path(__file__).parent )                           # Relative path to the parent of the program dir
print( Path(__file__).parent.absolute() )                # Absolute path to the parent of the program dir
print( Path(__file__).resolve().parents[1].absolute() )  # Absolute path to the parent of the program dir
print( Path(__file__).resolve().parents[2].absolute() )  # Absolute path to the parent of the program dir

# Call the program from its own location
'''
(alarm) pi@alarm:~/Dev/home_alarm/src $ python emails.py
emails.py
/home/pi/Dev/home_alarm/src/emails.py
.
/home/pi/Dev/home_alarm/src
/home/pi/Dev/home_alarm
/home/pi/Dev

'''
# Call of the program from another location
'''
(alarm) pi@alarm:~/Dev/home_alarm/src $ cd .. && python src/emails.py
src/emails.py
/home/pi/Dev/home_alarm/src/emails.py
src
/home/pi/Dev/home_alarm/src
/home/pi/Dev/home_alarm
/home/pi/Dev
'''

# -----------
# OLD FASHION
import os

# CWD is the current working directory or location form where the program is called

# short: Relative path to the program
# long: relative path between CWD and the file (ie the filename if CWD is the directory containing the program. ie the path+filename to call in order to execute the programme from CWD)
print (__file__) 

# short: Relative path to the program directory
# long: Same as above but without the filename at the end, only path to directory containing the programme (ie "" if CWD is the directory containing the programme)
print (os.path.dirname(__file__))

# short: Absolute path to the program
print (os.path.abspath(__file__)) # Absolute path to the program filename

# short: Absolute path to the program directory
# long: Absolute path of the directory where the program resides (whatever the location it is executed from)
print (os.path.abspath(os.path.dirname(__file__)))
print (os.path.dirname(os.path.abspath(__file__)))

# Call the program from its own location
'''
(alarm) pi@alarm:~/Dev/home_alarm/src $ python emails.py
emails.py

/home/pi/Dev/home_alarm/src/emails.py
/home/pi/Dev/home_alarm/src
/home/pi/Dev/home_alarm/src
'''
# Call of the program from another location
'''
(alarm) pi@alarm:~/Dev/home_alarm/src $ cd ..
(alarm) pi@alarm:~/Dev/home_alarm $ python src/emails.py
src/emails.py
src
/home/pi/Dev/home_alarm/src/emails.py
/home/pi/Dev/home_alarm/src
/home/pi/Dev/home_alarm/src
'''
