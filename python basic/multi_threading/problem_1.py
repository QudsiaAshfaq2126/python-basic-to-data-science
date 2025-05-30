# 

import threading
import time

# Function to be run by each thread
def show(i):
    print(f"Thread {i} is running")
    time.sleep(1)
    print(f"Thread {i} is done")

# Create and start 5 threads
for i in range(5):
    th = threading.Thread(target=show, args=(i,))
    th.start()

# Print total active threads
print("Active threads:", threading.active_count())
