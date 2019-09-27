from threading import Timer,Thread,Event


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

def printer():
    print('ipsem lorem')
    global x
    global stopIt
    x = x + 1
    print(x)
    if x == 5:
        stopIt = True
        print("論 stop")
    print(stopIt)

x = 0
stopIt = False
t = perpetualTimer(0.5, printer)
t.start()
while not stopIt:
    pass

print("hey stop")
t.cancel()
