class TV:
    # constructor
    def __init__(self):
        self._on = False
        self._channel = 2
        self._volumeLevel = 1
    def turnOn(self):
        self._on = True
    def turnOff(self):
        self._on = False
    def setChannel(self, newChannel):
        if (newChannel >=1 and newChannel <=120):
            self._channel = newChannel
    def setVolume (self, newVolume):
        if (newVolume >= 1 and newVolume <= 7):
            self._volumeLevel = newVolume
    def channelUp (self):
        if (self._channel < 120):
            self._channel += 1
    def channeldown (self):
        if (self._channel > 1):
            self._channel -= 1
    def volumeup (self):
        if (self._volumeLevel < 7):
            self._volumeLevel += 1
    def volumedown (self):
        if (self._volumeLevel > 1):
            self._volumeLevel -= 1
    def __str__ (self):
        if (self._on):
            s = 'TV On\n'
        else:
            s = 'TV Off\n'
        s+= 'Channel ' + str(self._channel) + ' Volume at ' + str(self._volumeLevel) + '\n'
        return s
   
def main ():
    livingRoom = TV()
    livingRoom.turnOn()
    livingRoom.setChannel(80)
    livingRoom.setVolume(5)
    print("Living Room TV")
    print (livingRoom)

    kitchen = TV()
    kitchen.turnOn()
    kitchen.channelUp
    kitchen.channelUp
    print("Kitchen TV")
    print (kitchen)
 
if __name__ == '__main__':
    main()