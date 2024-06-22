import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Functions for the Tkinter UI
def browse_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("jpeg files", "*.jpeg"), ("png files", "*.png"), ("all files", "*.*")))
    image_path_var.set(filename)

def start_whatsapp_script():
    try:
        country_code = int(country_code_var.get())
        numbers = numbers_var.get().split(',')
        msg = message_var.get("1.0", tk.END).strip()
        image_path = image_path_var.get()

        # Create a profile directory if it does not exist
        profile_path = os.path.join(os.getcwd(), 'chrome-profile')
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)

        # Create driver with user data directory
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={profile_path}")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open browser with default link
        link = 'https://web.whatsapp.com'
        driver.get(link)
        time.sleep(login_time)

        # Loop Through Numbers List
        for num in numbers:
            try:
                num = num.strip()
                link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
                driver.get(link)
                time.sleep(new_msg_time)
                # Click on button to load the input DOM
                if image_path:
                    time.sleep(3)
                    attach_btn = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
                    attach_btn.click()
                    time.sleep(action_time)
                    # Find and send image path to input
                    time.sleep(3)
                    msg_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
                    msg_input.send_keys(image_path)
                    time.sleep(action_time)
                # Start the action chain to write the message
                actions = ActionChains(driver)
                for line in msg.split('\n'):
                    actions.send_keys(line)
                    # SHIFT + ENTER to create next line
                    actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(send_msg_time)

            except Exception as e:
                print(f"Error with number {num}: {e}")
                continue  # Skip to the next number if there's an error

        # Log out of WhatsApp Web
        # menu_btn = driver.find_element(By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div')
        # menu_btn.click()
        # time.sleep(action_time)

        # logout_btn = driver.find_element(By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]')
        # logout_btn.click()
        # time.sleep(action_time)

        # logout_ok_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]')
        # logout_ok_btn.click()
        # time.sleep(action_time)
        
        # Quit the driver
        driver.quit()
        messagebox.showinfo("Success", "Messages sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter UI Setup
root = tk.Tk()
root.title("WhatsApp Automation")

country_code_var = tk.StringVar()
numbers_var = tk.StringVar()
image_path_var = tk.StringVar()

tk.Label(root, text="Country Code:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
tk.Entry(root, textvariable=country_code_var).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Numbers (comma-separated):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
tk.Entry(root, textvariable=numbers_var, width=50).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Message:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
message_var = tk.Text(root, width=50, height=10)
message_var.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Image Path:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
tk.Entry(root, textvariable=image_path_var, width=50).grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
tk.Button(root, text="Browse", command=browse_image).grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

tk.Button(root, text="Start", command=start_whatsapp_script).grid(row=4, column=1, padx=10, pady=20)

# Configurations
login_time = 30  # Time for login (in seconds)
new_msg_time = 5  # Time for a new message (in seconds)
send_msg_time = 5  # Time for sending a message (in seconds)
action_time = 2  # Set time for button click action

root.mainloop()
