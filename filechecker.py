import os
filename="/etc/hosts"

if os.path.exists(filename) and os.path.isfile(filename):
    print("File exist")
else:
    print("File doesn't exist")
