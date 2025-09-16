import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("✅ Server is running at IP:", ip_address)
#server_update.py
import os
from datetime import datetime

# Messages লগ ফাইল
MESSAGE_LOG = "messages.txt"

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {msg}"
    with open(MESSAGE_LOG, "a") as f:
        f.write(entry + "\n")
    print(f"✅ Message logged: {entry}")

def view_messages():
    if os.path.exists(MESSAGE_LOG):
        print("\n--- All Messages ---")
        with open(MESSAGE_LOG, "r") as f:
            print(f.read())
        print("-------------------")
    else:
        print("No messages yet.")

def main():
    print("=== Server Update: Message System Active ===")
    
    while True:
        print("\nOptions:")
        print("1. Log a message")
        print("2. View all messages")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            msg = input("Enter your message: ").strip()
            if msg:
                log_message(msg)
            else:
                print("❌ Empty message, not logged.")
        
        elif choice == "2":
            view_messages()
        
        elif choice == "3":
            print("Exiting server update system. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
