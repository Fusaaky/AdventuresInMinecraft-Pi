from ast import While
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 9 and pos.z == 1:
        mc.postToChat("WelcomeHome")