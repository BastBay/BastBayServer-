# server.py
import os

# পাসওয়ার্ড সেট
PASSWORD = "5683"

def main():
    print("=== Welcome to your Server Update System ===")
    user_pass = input("Enter password to continue: ")
    
    if user_pass != PASSWORD:
        print("❌ Incorrect password! Access denied.")
        return
    
    print("✅ Password correct. You can now update the server.")
    print("Type your Python code below (type 'END' in a new line to finish):")

    # ইউজারের কোড ইনপুট নেওয়া
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)
    
    # কোডকে server_update.py তে সেভ করা
    update_file = "server_update.py"
    with open(update_file, "w") as f:
        f.write("\n".join(code_lines))
    
    print(f"✅ Update saved successfully to {update_file}!")
    print("You can now run or deploy this update as needed.")

if __name__ == "__main__":
    main()
