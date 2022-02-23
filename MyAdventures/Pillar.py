import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

for a in range (50):
    mc.setBlock(pos.x, pos.y+a, pos.z, block.STONE_BRICK.id)
    mc.player.setPos(pos.x, pos.y+a, pos.z)

for b in range (50):
    time.sleep(0.5)
    mc.setBlock(pos.x, pos.y+b, pos.z, block.AIR.id)