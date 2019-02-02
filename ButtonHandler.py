import threading

class ButtonHandler(threading.Thread):
    def __init__(self, hw, callbacks):
        super(ButtonHandler, self).__init__()
        self.hw = hw
        self.callbacks = callbacks

    def run(self):
        while True:
            m = self.hw.mIn.receive()
            if m.type == "control_change" and m.value == 127:
                for i in self.callbacks:
                    if m.control == i:
                        self.callbacks[i]()
            else:
                pass
