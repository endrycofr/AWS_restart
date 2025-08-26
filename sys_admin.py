import os
import subprocess

print("\n=== Exercise 1: Using os.system() ===")
os.system("ls")

print("\n=== Exercise 2: Using subprocess.run(['ls']) ===")
subprocess.run(["ls"])

print("\n=== Exercise 3: Using subprocess.run(['ls', '-l']) ===")
subprocess.run(["ls", "-l"])

print("\n=== Exercise 4: Using subprocess.run(['ls', '-l', 'README.md']) ===")
subprocess.run(["ls", "-l", "README.md"])

print("\n=== Exercise 5: Retrieving system information (uname -a) ===")
command = "uname"
commandArgument = "-a"
print(f"Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])

print("\n=== Exercise 6: Retrieving active process information (ps -x) ===")
command = "ps"
commandArgument = "-x"
print(f"Gathering active process information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
