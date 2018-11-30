import wx
import EventHandler


class OpenGui(wx.App):

    def OnInit(self):
        myframe = EventHandler.eventHandler(None)
        myframe.Show(True)
        return True


def main():

    app = OpenGui()
    app.MainLoop()

    pass


if __name__ == "__main__":
    main()
