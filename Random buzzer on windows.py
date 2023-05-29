# import random
# import time
# from playsound import playsound

# def ringing_alarm(max_time_hours, num_rings):
#     max_time_seconds = max_time_hours * 3600 - 11*num_rings
#     time_block = max_time_seconds / num_rings
#     print(f"Alarm will ring {num_rings} times in {max_time_seconds/60} minutes.")
#     for i in range(num_rings):
#         # Check if there is enough time left for the alarm to ring
#         if max_time_seconds <= 0:
#             print(f"No more time left for alarm {i+1} to ring.")
#             break
#         # Generate a random time interval for the alarm to ring
#         time_interval_rand = random.uniform(1, time_block)
#         # max_time_seconds -= time_interval_rand
#         time.sleep(time_interval_rand) # Wait for the alarm to ring
#         print(f"Ring! Ring! Ring! Alarm {i+1} rang after {time_interval_rand} seconds.")
#         # Play the sound file
#         playsound("ring.mp3")
#         if (time_block-time_interval_rand-11>1):
#             time.sleep(time_block-time_interval_rand-11) # Wait for the next alarm to ring
import random
import time
from playsound import playsound

def ringing_alarm():
    # Prompt user for input on maximum time and number of rings
    max_time = input("Enter the maximum time for the alarm (e.g. 1.5h or 90m): ")
    num_rings = int(input("Enter the number of times the alarm should ring: "))

    # Determine the maximum time in seconds based on user input
    if "h" in max_time:
        max_time_seconds = float(max_time[:-1]) * 3600
    elif "m" in max_time:
        max_time_seconds = float(max_time[:-1]) * 60
    else:
        max_time_seconds = float(max_time)

    # Calculate the time interval for each ring
    time_block = (max_time_seconds - 11*num_rings) / num_rings
    print(f"Alarm will ring {num_rings} times in {max_time_seconds/60} minutes.")

    for i in range(num_rings):
        # Check if there is enough time left for the alarm to ring
        if max_time_seconds <= 0:
            print(f"No more time left for alarm {i+1} to ring.")
            break
        # Generate a random time interval for the alarm to ring
        time_interval_rand = random.uniform(1, time_block)
        # max_time_seconds -= time_interval_rand
        time.sleep(time_interval_rand) # Wait for the alarm to ring
        print(f"Ring! Ring! Ring! Alarm {i+1} rang after {time_interval_rand} seconds.")
        # Play the sound file
        playsound("ring.mp3")
        left_time = time_block-time_interval_rand-11
        if (left_time>1) & (i!=num_rings-1):
            time.sleep(time_block-time_interval_rand-11) # Wait for the next alarm to ring
        if(i==num_rings-1):
            print("Alarm finished ringing.")
            print(f"you still have {left_time +11} seconds left")


ringing_alarm()