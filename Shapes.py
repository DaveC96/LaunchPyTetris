import time
class Shape:
    def __init__(self, colour, location):
        self.colour = colour
        self.location = location
        self.last = [None, None, None, None]

    def move_down(self):
        if not any(i < 19 for i in self.location):
            for i in range(len(self.location)):
                self.last[i] = self.location[i]
                self.location[i] = self.location[i]-10



    def move_left(self):
        for i in range(len(self.location)):
            self.last[i] = self.location[i]
            self.location[i] = self.location[i]-1
            # Converts to string and strips the Y position. This is way too hacky, I feel dirty for having written it.
            if int(str(self.location[i])[-1]) < 1:   # Hit right wall
                print("Hit right wall, clipping")
                for j in range(len(self.location)):
                    self.location[j] = self.location[j]+1


    def move_right(self):
        for i in range(len(self.location)):
            self.last[i] = self.location[i]
            self.location[i] = self.location[i]+1
            # Converts to string and strips the Y position. This is way too hacky, I feel dirty for having written it.
            if int(str(self.location[i])[-1]) > 8:   # Hit right wall
                print("Hit right wall, clipping")
                for j in range(len(self.location)):
                    self.location[j] = self.location[j]-1

    def rotate(self):
        pass    # Uhh... maybe later?
