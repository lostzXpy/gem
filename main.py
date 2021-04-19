import os 

os.system('apt install mpg123')
file = 'gemidão.mp3'
os.system('mpg123 ' + file)
