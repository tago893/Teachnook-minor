import tkinter as tk
import datetime as dt
import winsound as ws

# Creating a timer

class Timer(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self.seconds_passed=0
        self._timer_on=False

    def show_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.resume.pack()
        self.reset.pack()

    def create_widgets(self):
        self.label=tk.Label(self,text="Enter the time in seconds")
        self.entry=tk.Entry(self,justify="center")
        self.entry.focus_set()
        self.reset=tk.Button(self,text="Reset",command=self.reset_button)
        self.stop=tk.Button(self,text="Stop",command=self.stop_button)
        self.start=tk.Button(self,text="Start",command=self.start_button)
        self.resume=tk.Button(self,text="Resume",command=self.resume_button)

    def countdown(self):
        """
         Function for countdown
        """
        self.label["text"]=self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left-=1
            self.seconds_passed+=1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False
            ws.PlaySound("sound",ws.SND_FILENAME)


    def reset_button(self):
         """
         Function to invoke reset_timer the countdown
         """
         self.seconds_left=0
         self.stop_timer()
         self._timer_on=False
         self.label["text"]="Enter the time in seconds"
         self.start.forget()
         self.stop.forget()
         self.reset.forget()
         self.start.pack()
         self.stop.pack()
         self.reset.pack()

    def stop_button(self):
         """
        Function to invoke the stop_timer function
        """
         self.seconds_left = int(self.entry.get())
         self.stop_timer()
        
    def resume_button(self):
        """
        Function to resume the timer in case the timer is paused
        """
        self.seconds_left = int(self.entry.get()) - self.seconds_passed
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        
    def start_button(self):
          """
          Function that starts the countdown
          """
          self.seconds_left=int(self.entry.get())
          self.stop_timer()
          self.countdown()
          self.start.forget()
          self.stop.forget()
          self.reset.forget()
          self.start.pack()
          self.stop.pack()
          self.reset.pack()
          
    def stop_timer(self):
           if self._timer_on:
               self.after_cancel(str(self._timer_on))
               self._timer_on=False

    def convert_seconds_left_to_time(self):
           return dt.timedelta(seconds=self.seconds_left)


if __name__=='__main__':
    root=tk.Tk()
    root.geometry("600x300")
    count = Timer(root)
    count.pack()
    root.mainloop()
        
