#!/usr/bin/python3
# -*- coding: latin1 -*-
blob = """          7G��9?K�6a�,��$��٣x��19-��:�{µLL/��SB8br0����ޟ�m
5<�>t�n!�1}dF"��M����E�̴��UQ+����:O&��wZ�����<���W���Tp��
"""
from hashlib import sha256
if sha256(blob.encode()).hexdigest() == "028df83c60316e59a2dbac1bfd3b5c2a5581730ed3cc5fa2a05deb46d5b07a10":
	print ("I am good and friendly.")
else:
	print("I am an evil payload, prepare to suffer.")
