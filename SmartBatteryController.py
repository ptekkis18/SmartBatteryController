import psutil
import tkinter as tk
from PyP100 import PyP100
import time
import threading


class BatterySmartPlugController:
    def __init__(self, email, password, device_ip):
        self.email = email
        self.password = password
        self.device_ip = device_ip
        self.running = True
        self.plug = None
        self.thread = None

    def connect_plug(self):
        try:
            self.plug = PyP100.P100(self.device_ip, self.email, self.password)
           
        except Exception as e:
            print(f"Failed to create plug object: {e}")
            self.plug = None



    def control_plug(self):
        # Ensure plug is connected
        self.connect_plug()
        
        while self.running:
            try:
                battery = psutil.sensors_battery()
                percent = battery.percent

                #Adjust values here for different charging cicle (optional)
                if self.plug:
                    if percent <= 20 and not battery.power_plugged:
                        self.plug.turnOn()
                        print(f"Battery low ({percent}%). Turned plug ON.")

                    if percent >= 80 and battery.power_plugged:
                        self.plug.turnOff()
                        print(f"Battery charged ({percent}%). Turned plug OFF.")

            except Exception as e:
                print(f"Error controlling plug: {e}")
                # Attempt to reconnect
                self.connect_plug()

            time.sleep(30)  # Check every 30 seconds - Adjust value to check battery % more / less frequently to adjust plug accordingly (optional)

    def start(self):
        thread = threading.Thread(target=self.control_plug)
        thread.daemon = True  # Allow thread to exit when main program exits
        thread.start()

    def stop(self):
        #Close program when X is pressed from GUI
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
            print("Plug controller stopped.")

class BatteryIndicator:
    def __init__(self,root,controller):
        self.root = root
        self.controller = controller
        self.root.title("Battery Indicator")
        self.root.geometry("200x200")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.update_battery()
    
    def update_battery(self):
        battery = psutil.sensors_battery()
        percent = battery.percent

        # Clear previous drawing
        self.canvas.delete('all')

        # Draw background circle (gray)
        self.canvas.create_oval(50, 50, 150, 150, outline='lightgray', width=20)

        # Draw battery percentage circle
        start_angle = 90  # Top of circle
        extent_angle = -(360 * percent / 100)

        # Color changes based on battery percentage
        color = 'green' if percent > 50 else 'orange' if percent > 25 else 'red'

        # Draw battery percentage arc
        self.canvas.create_arc(50, 50, 150, 150, start=start_angle, extent=extent_angle, 
                                style=tk.ARC, width=20, outline=color)

        # Add percentage text
        self.canvas.create_text(100, 100, text=f"{percent}%", font=('Arial', 20))

        # Update every 5 seconds - Adjust to lower number for more frequent GUI updates (Optional)
        self.root.after(5000, self.update_battery)

    def on_close(self):
        try:
            print("Smart Battery Controller Stopping...")
            self.controller.stop()
            self.root.destroy()
        except:
            print("Error Stopping")
        

def main():
    # Replace with your Tapo credentials and device IP
    controller = BatterySmartPlugController(
        email="Your_Tapo_Email", 
        password="Your_Tapo_Password", 
        device_ip="Device_IP_Address"  # Your Tapo P100 IP address
    )
    controller.start()
    
    root =tk.Tk()
    app = BatteryIndicator(root,controller)
    root.mainloop()
   

if __name__ == "__main__":
    main()