import multiprocessing
import random
import time
from datetime import datetime

def print_current_time(process_id):
    # Generate a random sleep time between 0 and 1 seconds
    sleep_time = random.uniform(0, 1)
    
    # Sleep for the random time
    time.sleep(sleep_time)
    
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current time and process ID
    print(f"Process {process_id}: Current Time: {current_time}")

if __name__ == "__main__":
    # Create three separate processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=print_current_time, args=(i,))
        processes.append(process)
        process.start()
    
    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have completed.")
