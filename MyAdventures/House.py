import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
FOUNDATION_SIZE = 12
FLOOR_SIZE = 11
SIZE = 10
x = pos.x + 2
y = pos.y
z = pos.z
midx = x + FOUNDATION_SIZE/2
midy = y + FOUNDATION_SIZE/2
c = random.randint(0, 15)

def build_house():
#Foundation + Floor + Roof
    mc.setBlocks(x, y, z, x+FOUNDATION_SIZE, y, z+FOUNDATION_SIZE, block.STONE_BRICK.id)
    mc.setBlocks(x, y, z, x+FLOOR_SIZE, y, z+FLOOR_SIZE, block.WOOD_PLANKS.id)
    mc.setBlocks(x, y, z, x + 12, y, z, block.STONE_BRICK.id)
    mc.setBlocks(x, y, z, x, y, z + 12, block.STONE_BRICK.id)
    mc.setBlocks(x + 2, y + 5, z + 2, x + 10, y + 5, z + 10, block.GLASS.id)
#Walls
    mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 4, z +11, block.WOOD.id)
    mc.setBlocks(x + 2, y + 1, z + 2, x + 10, y + 4, z +10, block.AIR.id)
    mc.setBlocks(x + 11, y + 1, z + 2, x + 11, y + 3, z +10, block.GLASS_PANE.id)
    mc.setBlocks(x + 2, y + 1, z + 1, x + 10, y + 3, z +1, block.WOOD_PLANKS.id)
    mc.setBlocks(x + 2, y + 1, z + 11, x + 11, y + 3, z +11, block.WOOD_PLANKS.id)
    mc.setBlocks(x + 1, y + 1, z + 2, x + 1, y + 3, z + 10, block.WOOD_PLANKS.id)
    mc.setBlocks(x + 1, y + 1, z + 5, x + 1, y + 2, z + 3, block.AIR.id)
    mc.setBlock(x + 1, y + 3, z + 4, block.AIR.id)
    mc.setBlocks(x + 3, y + 2, z + 1, x + 9, y + 2, z + 1, block.GLASS_PANE.id)
    mc.setBlocks(x + 3, y + 2, z + 11, x + 9, y + 2, z + 11, block.GLASS_PANE.id)
#Carpet Enter
    mc.setBlocks(x + 1, y, z + 5, x + 1, y, z + 3, block.WOOL.id, c)

build_house()