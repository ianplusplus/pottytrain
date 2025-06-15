from child import Child
from rewards_chart import RewardChart
from pathlib import Path
import time
import threading
import pygame

timer_thread = None
stop_flag = False

def main():
    #Check to see if the options file exists

    file_path = Path("options")

    print("Welcome to PottyTrain! Let's get this kid going!")

    # if the options file exists use this to load the settings from the previous run otherwise run through setup
    if not file_path.exists():
        child = setup()
        child.SaveChild() 

    child = load_from_options()

    print("Your child will be reminded every", child.reminder_time, 'minutes.')
    start_timer(child, "alarm.wav")

    while True:
         user_input = input("Enter 'exit' to the program or 'help' for more options: ")
         if user_input == 'exit':
              stop_flag = True
              child.SaveChild()
              break
         elif user_input == 'help':
              print("'restart' will restart the timer for the set duration.")
              print("'help' will bring you to this menu.")
              print("'reset' will let you adjust the options for your child.")
              print("'show' will show your child their sticker collection.")
              print("'success' will record the current attempt as a success and restart the timer.")
              print("'pass' will record the attempt as a no success and restart the timer.")
              print("'set' will allow you to change the reminder interval")
         elif user_input == 'restart':
              start_timer(child, 'alarm.wav')
              print("The timer has been restarted for", child.reminder_time, 'minutes.')
         elif user_input == 'show':
              chart = RewardChart(child, 100)
              chart.draw_canvas()
         elif user_input == 'success':
              child.PottyAttempt(True)
         elif user_input == 'pass':
              child.PottyAttempt(False)
         elif user_input == 'reset':
              confirm = input("This will reset all progress on the current rewards chart (yes)")
              if confirm == 'yes':
                setup().SaveChild()
                child = load_from_options()
                start_timer(child, "alarm.wav")
         elif user_input == 'set':
              new_time = int(input("Enter the number of minutes you would like to be reminded: "))
              child.reminder_time = new_time
              user_in = input("Would you like to restart the timer? (yes/no): ")
              if user_in == "yes":
                start_timer(child, 'alarm.wav')
                print("The timer has been restarted for", child.reminder_time, 'minutes.')
              else:
                print("Timer change will take affect after next restart.")
         else:
              "The input is not correct. Type 'help' for more details."

def setup():
    print("Let's get some first time information about your child!")
    childs_name = input("Please enter your child's name: ")
    childs_reminders = int(input("How often (in minutes) would you like to have your child reminded? "))
    childs_major_reward = int(input("What would be your major success milestone? (This also affects the row length on the reward chart) "))
    childs_row_count = int(input("How many major records would you like to keep? (This is the amount of rows) "))

    childs_record_list = []
    for i in range(childs_major_reward * childs_row_count):
        childs_record_list.append(False)

    return Child(childs_name, childs_reminders, childs_major_reward, childs_record_list, 0, childs_major_reward * childs_row_count)

def load_from_options():
    with open('options', "r") as file:
            line = file.readline()
            line = line.strip()
            return Child.LoadChildFromFile(line)

def play_reminder(reminder_file):
     pygame.mixer.init()
     pygame.mixer.music.load(reminder_file)
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy():
          time.sleep(0.1)

def start_timer(child, sound_file):
     global timer_thread, stop_flag
     if timer_thread and timer_thread.is_alive():
          stop_flag = True
          timer_thread.join()
     stop_flag = False
     timer_thread = threading.Thread(target=timer_func, args=(child, sound_file), daemon = True)
     timer_thread.start()

def timer_func(child, sound_file):
     global stop_flag
     seconds = child.reminder_time * 60
     start = time.time()
     while time.time() - start < seconds:
          if stop_flag:
               print("Timer has been cancelled.")
               return
          time.sleep(1)
     play_reminder(sound_file)

main()