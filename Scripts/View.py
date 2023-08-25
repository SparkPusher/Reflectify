# %%
import tkinter as tk
import random
import serial
import subprocess
import threading

class View(tk.Frame):

    def __init__(self, model):
        
        ####
        # Essentials
        self.s = serial.Serial('/dev/ttyACM0', 9600)
        self.model = model
        self.state_yt = False
        self.state_sc = False
        self.state_n = False
        self.state_cam = False
        self.state_keyboard = False
        self.visible_subprocess = True
        
        # Viewport thread
        t_vp = threading.Thread(target=self.thread_vp())
        t_vp.start()
        
        
    def thread_vp(self):
        self.viewport = tk.Tk()
        #####
        # Functions for Viewport
        self.font_type = "Times"
        self.configuration_viewport()
        self.datetime_label()
        self.spotify_label()
        self.sentences()
        self.weather()
        self.update_weather()
        self.update_list_value()
        self.upd_d()
        self.dec_data()
        self.sensor_data()
        self.cpu_temp()
        self.update_cpu_value()
        self.buttons()
        self.standby_check()
        ###
        self.viewport.mainloop()
        

    def __del__(self):
        pass

    def configuration_viewport(self):
        self.viewport.attributes('-fullscreen', True)
        self.viewport.configure(background='black')
        
    ########################################################
    ########################################################
    ########################################################
    #### Standby
        
    def standby_check(self):
        self.update_left_us = self.dec_data()[3]
        self.update_right_us = self.dec_data()[2]
        if int(self.update_left_us) < 70 or int(self.update_right_us) < 70:
            self.sens_text.configure(text="Room:")
            self.cpu.configure(text="CPU:")
            self.update_datetime()
            self.update_sentence()
            self.update_sensor_data()
            self.update_cpu_temp()
            self.show.place(relx=0.015, rely=0.7, anchor= 'nw')
            self.hide.place(relx=0.08, rely=0.7, anchor= 'nw')
            self.btn_end_tk.place(relx=0.015, rely=0.75, anchor= 'nw')
            self.btn_reboot.place(relx=0.08, rely=0.75, anchor= 'nw')
        else: 
            self.viewport.after(100, self.standby)
        self.viewport.after(100, self.standby_check)
    
    def standby(self):
        self.temp_inside.configure(text="")
        self.hum_inside.configure(text="")
        self.sens_text.configure(text="")
        self.day.configure(text="")
        self.mo_ye.configure(text="")
        self.time.configure(text="")
        self.nice_sentence.configure(text="")
        self.cpu.configure(text="")
        self.cpu_value.configure(text="")
        self.sp_text1.configure(text="")
        self.sp_text2.configure(text="")
        self.sp_text3.configure(text="")
        self.show.place_forget()
        self.hide.place_forget()
        self.btn_end_tk.place_forget()
        self.btn_reboot.place_forget()
        
        
    ########################################################
    ########################################################
    ########################################################
    #### Decoding serial
        
    def dec_data(self):
        hum = str("Hum.: ") + self.split[3] + str(" %")
        temp = str("Tem.: ") + self.split[2] + str(" °C")
        right_us = self.split[0]
        left_us = self.split[1]
        return hum, temp, right_us, left_us
    
    ########################################################
    ########################################################
    ########################################################
    #### Threads
    
    def thread_yt(self):
        if self.visible_subprocess == True:
            self.visible_subprocess = False
            self.t_yt = threading.Thread(target=self.start_yt)
            self.t_yt.start()
        else: pass

    def thread_sc(self):
        if self.visible_subprocess == True:
            self.visible_subprocess = False
            self.t_sc = threading.Thread(target=self.start_sc)
            self.t_sc.start()
        else: pass

    def thread_n(self):
        if self.visible_subprocess == True:
            self.visible_subprocess = False
            self.t_n = threading.Thread(target=self.start_n)
            self.t_n.start()
        else: pass

    def thread_cam(self):
        if self.visible_subprocess == True:
            self.visible_subprocess = False
            self.t_cam = threading.Thread(target=self.start_cam)
            self.t_cam.start()
        else: pass

    def thread_keyboard(self):
        if self.visible_subprocess == True:
            self.visible_subprocess = False
            self.t_keyboard = threading.Thread(target=self.start_keyboard)
            self.t_keyboard.start()
        else: pass
        

    ########################################################
    ########################################################
    ########################################################
    #### Start subprocesses
    
    def start_yt(self):
        self.state_yt = True
        self.sub_yt = subprocess.Popen(['python3', '/home/julian/Desktop/Reflectify/Scripts/Subscripts/Youtube.py'])
        while True:
            if self.sub_yt.poll() is None:
                subprocess.call(["wmctrl", "-a", "Youtube.py"])
            else:
                break
        
    def start_sc(self):
        self.state_sc = True
        self.sub_sc = subprocess.Popen(['python3', '/home/julian/Desktop/Reflectify/Scripts/Subscripts/Soundcloud.py'])
        while True:
            if self.sub_sc.poll() is None:
                subprocess.call(["wmctrl", "-a", "Soundcloud.py"])
            else:
                break
            
    def start_n(self):
        self.state_n = True
        self.sub_n = subprocess.Popen(['python3', '/home/julian/Desktop/Reflectify/Scripts/Subscripts/News.py'])
        while True:
            if self.sub_n.poll() is None:
                subprocess.call(["wmctrl", "-a", "News.py"])
            else:
                break
            
    def start_cam(self):
        self.state_cam = True
        self.sub_cam = subprocess.Popen(['python3', '/home/julian/Desktop/Reflectify/Scripts/Subscripts/Camera.py'])
        while True:
            if self.sub_cam.poll() is None:
                subprocess.call(["wmctrl", "-a", "Camera.py"])
            else:
                break
            
    def start_keyboard(self):
        self.state_keyboard = True
        self.sub_keyboard = subprocess.Popen(['python3', '/home/julian/Desktop/Reflectify/Scripts/Subscripts/VirtualKeyboard.py'])
        while True:
            if self.sub_keyboard.poll() is None:
                subprocess.call(["wmctrl", "-a", "VirtualKeyboard.py"])
            else:
                break
            
        
    ########################################################
    ########################################################
    ########################################################
    #### Stop subprocesses and close viewport

    def stop_sub(self):
        if self.state_sc == True:
            self.sub_sc.kill()
            self.state_sc = False
            self.visible_subprocess = True
        else: pass
        if self.state_yt == True:
            self.sub_yt.kill()
            self.state_yt = False
            self.visible_subprocess = True
        else: pass
        if self.state_n == True:
            self.sub_n.kill()
            self.state_n = False
            self.visible_subprocess = True
        else: pass
        if self.state_cam == True:
            self.sub_cam.kill()
            self.state_cam = False
            self.visible_subprocess = True
        else: pass
        try:
            self.sp_text1.configure(text="")
            self.sp_text2.configure(text="")
            self.sp_text3.configure(text="")
        except: pass
        
    def stop_keyboard(self):
        if self.state_keyboard == True:
            self.sub_keyboard.kill()
            self.state_keyboard = False
        else: pass
        
    def end_viewport(self):
        if self.state_sc == True:
            self.sub_sc.kill()
        if self.state_yt == True:
            self.sub_yt.kill()
        if self.state_n == True:
            self.sub_n.kill()
        if self.state_cam == True:
            self.sub_cam.kill()
        if self.state_keyboard == True:
            self.sub_keyboard.kill()
        self.viewport.destroy()
        
    def reboot(self):
        command = "sudo reboot"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
    ########################################################
    ########################################################
    ########################################################
    #### Tkinter functions

    def show_actions(self):
        self.btn_yt.place(relx=0.015, rely=0.8, anchor= 'nw')
        self.btn_ne.place(relx=0.08, rely=0.8, anchor= 'nw')
        self.btn_sc.place(relx=0.015, rely=0.85, anchor= 'nw')
        self.btn_sp.place(relx=0.08, rely=0.85, anchor= 'nw')
        self.btn_ca.place(relx=0.015, rely=0.9, anchor= 'nw')
        self.btn_cl.place(relx=0.08, rely=0.9, anchor= 'nw')
        self.btn_kb.place(relx=0.015, rely=0.95, anchor= 'nw')
        self.btn_cl_k.place(relx=0.08, rely=0.95, anchor= 'nw')

    def hide_actions(self):
        self.btn_yt.place_forget()
        self.btn_ne.place_forget()
        self.btn_sc.place_forget()
        self.btn_cl.place_forget()
        self.btn_ca.place_forget()
        self.btn_kb.place_forget()
        self.btn_cl_k.place_forget()
        self.btn_sp.place_forget()


    def buttons(self):
        self.show = tk.Button(self.viewport, text="Show Actions", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.show_actions)
        self.hide = tk.Button(self.viewport, text="Hide Actions", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.hide_actions)
        
        self.btn_yt = tk.Button(self.viewport, text="Youtube", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.thread_yt)
        self.btn_ne = tk.Button(self.viewport, text="News", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.thread_n)
        self.btn_sc = tk.Button(self.viewport, text="Soundcloud", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.thread_sc)
        self.btn_sp = tk.Button(self.viewport, text="Spotify", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command = self.update_spotify)
        self.btn_ca = tk.Button(self.viewport, text="Camera", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.thread_cam)
        self.btn_cl = tk.Button(self.viewport, text="Close Action", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.stop_sub)
        self.btn_kb = tk.Button(self.viewport, text="Keyboard", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.thread_keyboard)
        self.btn_cl_k = tk.Button(self.viewport, text="Close Keyboard", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.stop_keyboard)
        self.btn_end_tk = tk.Button(self.viewport, text="End Reflectify", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.end_viewport)
        self.btn_reboot = tk.Button(self.viewport, text="Reboot Pi", bg="black", activebackground="azure4", activeforeground="white", fg="white", width=9, command=self.reboot)
        
    
    def cpu_temp(self):
        self.cpu = tk.Label(self.viewport, text="CPU:", bg="black", fg="white",
                            font=(self.font_type, 25))
        self.cpu_value = tk.Label(self.viewport, text="", bg="black", fg="white",
                                    font=(self.font_type, 25))
        self.cpu.place(relx= 0.0, rely= 0.39, anchor= 'nw')
        self.cpu_value.place(relx= 0.0, rely= 0.42, anchor= 'nw')

    def sensor_data(self):
        self.sens_text = tk.Label(self.viewport, text="Room:", bg="black", fg="white",
                            font=(self.font_type, 25))
        self.temp_inside = tk.Label(self.viewport, text="", bg="black", fg="white",
                                    font=(self.font_type, 25))
        self.hum_inside = tk.Label(self.viewport, text="", bg="black", fg="white",
                                   font=(self.font_type, 25))
        self.sens_text.place(relx= 0.0, rely= 0.25, anchor= 'nw')
        self.temp_inside.place(relx= 0.0, rely= 0.28, anchor= 'nw')
        self.hum_inside.place(relx= 0.0, rely= 0.31, anchor= 'nw')    

    def datetime_label(self):
        self.day = tk.Label(self.viewport, text="", bg="black", fg="white",
                            font=(self.font_type, 50))
        self.mo_ye = tk.Label(self.viewport, text="", bg="black", fg="white",
                              font=(self.font_type, 50))
        self.time = tk.Label(self.viewport, text="", bg="black", fg="white",
                             font=(self.font_type, 60))
        self.day.place(relx=1.0, rely=0.0, anchor='ne')
        self.mo_ye.place(relx=1.0, rely=0.06, anchor='ne')
        self.time.place(relx=1.0, rely=0.12, anchor='ne')
        
    def spotify_label(self):
        self.sp_text1 = tk.Label(self.viewport, text="", bg="black", fg="green",
                            font=(self.font_type, 20))
        self.sp_text1.place(relx=1.0, rely=0.5, anchor='ne')
        self.sp_text2 = tk.Label(self.viewport, text="", bg="black", fg="green",
                            font=(self.font_type, 20))
        self.sp_text2.place(relx=1.0, rely=0.55, anchor='ne')
        self.sp_text3 = tk.Label(self.viewport, text="", bg="black", fg="white",
                            font=(self.font_type, 20, 'bold'))
        self.sp_text3.place(relx=1.0, rely=0.6, anchor='ne')
        
    def sentences(self):
        self.nice_sentence = tk.Label(self.viewport, text="", bg="black", fg="white",
                                  font=(self.font_type, 25))
        self.nice_sentence.place(relx = 0.5, rely = 0.95, anchor = 'center')

    def weather(self):
        self.city = tk.Label(self.viewport, text=self.model.weather_info()[0], bg="black", fg="white",
                                  font=(self.font_type, 50))
        self.current_weather = tk.Label(self.viewport, text=self.model.weather_info()[1], bg="black", fg="white",
                                  font=(self.font_type, 25))
        self.forecast_text = tk.Label(self.viewport, text="Tomorrow:", bg="black", fg="white",
                                  font=(self.font_type, 25))
        self.forecast = tk.Label(self.viewport, text=self.model.weather_info()[2], bg="black", fg="white",
                                  font=(self.font_type, 25))
        self.temperature = tk.Label(self.viewport, text=self.model.weather_info()[3], bg="black", fg="white",
                                  font=(self.font_type, 25))
        self.city.place(relx= 0.0, rely= 0.0, anchor= 'nw')
        self.current_weather.place(relx= 0.0, rely= 0.08, anchor= 'nw')
        self.forecast_text.place(relx= 0.0, rely= 0.11, anchor= 'nw')
        self.forecast.place(relx= 0.0, rely= 0.14, anchor= 'nw')
        self.temperature.place(relx= 0.0, rely= 0.17, anchor= 'nw')

    ########################################################
    ########################################################
    ########################################################
    #### Updating functions

    def update_weather(self):
        self.update_city = self.model.weather_info()[0]
        self.update_info = self.model.weather_info()[1]
        self.update_forecast = self.model.weather_info()[2]
        self.update_temp = self.model.weather_info()[3]
        self.city.configure(text=self.update_city)
        self.current_weather.configure(text=self.update_info)
        self.forecast.configure(text=self.update_forecast)
        self.temperature.configure(text=self.update_temp)
        self.viewport.after(1800000, self.update_weather)

    def update_spotify(self):
        self.sp_text1.configure(text="Open your Spotify")
        self.sp_text2.configure(text="Connect Device to:")
        self.sp_text3.configure(text="raspotify (mirror)")
        
    def update_list_value(self):
        self.sen = random.choice(self.model.sen_list)
        self.viewport.after(10000, self.update_list_value)

    def update_sentence(self):
        self.nice_sentence.configure(text=self.sen)
        
    def update_datetime(self):
        self.update_day = self.model.datetime_info()[0]
        self.update_mo_d_y = self.model.datetime_info()[1]
        self.update_time = self.model.datetime_info()[2]
        self.day.configure(text=self.update_day)
        self.mo_ye.configure(text=self.update_mo_d_y)
        self.time.configure(text=self.update_time)
        
    def update_sensor_data(self):
        self.update_temp_inside = self.dec_data()[1]
        self.update_hum_inside = self.dec_data()[0]
        self.update_left_us = self.dec_data()[3]
        self.update_right_us = self.dec_data()[2]
        
        self.temp_inside.configure(text=self.update_temp_inside)
        self.hum_inside.configure(text=self.update_hum_inside)
        
    def update_cpu_value(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            self.cpu_temperature = str(int(temp_file.read()) / 1000.0) + str(" °C")
        self.viewport.after(1000, self.update_cpu_value)
    
    def update_cpu_temp(self):
        self.cpu_value.configure(text=self.cpu_temperature)
        
    def upd_d(self):
        response = self.s.readline()
        self.split = response.split()
        for i in range(len(self.split)):
            self.split[i] = self.split[i].decode("utf-8")
        self.viewport.after(1000, self.upd_d)

# %%
