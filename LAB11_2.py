class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 0
        self.isOn = False

    def onTV(self):
        self.isOn = True

    def offTV(self):
        self.isOn = False

    def changeVolume(self, new_volume):
        self.volume = new_volume

    def changeChannel(self, new_channel):
        self.channel = new_channel

# TV 객체 생성
tv = TV()

#초기 채널 및 음량
print("<초기 채널 및 음량>")
print("TV의 채널:", tv.channel)
print("TV의 음량:", tv.volume)
print()

# 변경할 채널과 볼륨 입력 받기
new_channel = int(input("변경할 채널 입력: "))
new_volume = int(input("변경할 볼륨 입력: "))
print()

# 채널과 볼륨 변경
tv.changeChannel(new_channel)
tv.changeVolume(new_volume)

# 변경된 내용 출력
print("<변경 채널 및 음량>")
print("TV의 채널:", tv.channel)
print("TV의 음량:", tv.volume)