import mido, yaml, threading


class Launchpad:
    def __init__(self):
        self.cfg = yaml.load(open("Config.yaml"))
        self.introAnim = mido.MidiFile("intro.mid")

        self.mOut = mido.open_output(self.cfg["hardware"]["midiport"])
        self.mIn  = mido.open_input(self.cfg["hardware"]["midiport"])
        self.mChl = self.cfg["hardware"]["midichannel"]
        self.board = {"height": 8, "width": 8}

        self.draw_ui()

    def draw_px(self, loc=int, velocity=int) -> None:
        try:
            self.mOut.send(mido.Message("note_on", channel=self.mChl, note=loc, velocity=velocity))
        except ValueError:
            pass

    def draw_board(self, velocity=int) -> None:
        for i in range(self.board["height"]):
            for j in range(self.board["width"]):
                self.mOut.send(mido.Message("note_on", channel=self.mChl, note=((i+1)*10+(j+1)), velocity=velocity))

    def draw_ui(self):
        for i in self.cfg["uilocations"]:
            print("drawing to "+str(self.cfg["uilocations"][i]))
            self.draw_px(int(self.cfg["uilocations"][i]), self.cfg["colours"]["cyan"])





