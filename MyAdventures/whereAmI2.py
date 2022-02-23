import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x= " + str(pos.x) + "y= " + str(pos.y) + "z= " + str(pos.z))