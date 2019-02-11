import OSC
from Tkinter import Tk, Label, Scale, HORIZONTAL

print "*******"
print "This program sends 1 continuous input to Wekinator."
print "Default is port 6448, message name /wek/inputs"
print "If Wekinator is not already listening for OSC, we will get an error."
print "*******"

send_address = '127.0.0.1', 6448

# OSC basic client
c = OSC.OSCClient()
c.connect(send_address)  # set the address for all following messages


def showValues():
    label1.config(text=str(w1.get()))
    label1.after(100, showValues)
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wek/inputs")
    oscmsg.append(float(w1.get()))
    c.send(oscmsg)


master = Tk()
w1 = Scale(master, from_=100, to=0, length=400, tickinterval=10)
w1.set(0)
w1.pack()

label1 = Label(master, fg="green")
label1.pack()

showValues()

master.mainloop()
