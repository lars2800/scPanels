import socket
import time

PIN_BUTTON_MAINPOWER_MAIN = 0
PIN_BUTTON_MAINPOWER_ENG  = 0
PIN_BUTTON_MAINPOWER_WPN  = 0
PIN_BUTTON_MAINPOWER_SHLD = 0

PIN_LED_MAINPOWER_MAIN = 0
PIN_LED_MAINPOWER_ENG  = 0
PIN_LED_MAINPOWER_WPN  = 0
PIN_LED_MAINPOWER_SHLD = 0

PIN_BUTTON_OPERATORMODES_MIS  = 0
PIN_BUTTON_OPERATORMODES_SCAN = 0
PIN_BUTTON_OPERATORMODES_MINE = 0
PIN_BUTTON_OPERATORMODES_GUN  = 0
PIN_BUTTON_OPERATORMODES_NAV  = 0

PIN_LED_OPERATORMODES_MIS  = 0
PIN_LED_OPERATORMODES_SCAN = 0
PIN_LED_OPERATORMODES_MINE = 0
PIN_LED_OPERATORMODES_GUN  = 0
PIN_LED_OPERATORMODES_NAV  = 0

PIN_SWITCH_SHIPMAIN_GEAR  = 0
PIN_BUTTON_SHIPMAIN_ABORT = 0
PIN_LED_SHIPMAIN_ABORT = 0
PIN_BUTTON_SHIPMAIN_RESET = 0
PIN_BUTTON_SHIPMAIN_SCANPING = 0
PIN_BUTTON_SHIPMAIN_ENGEAGEQUANTOMTRAVEL = 0
PIN_BUTTON_SHIPMAIN_TOGGLEVTOL = 0

MESSAGE_DISCONECT = b"CONNECTION-DISCONECTED"

clientSocket = socket.socket()
clientSocket.connect( ("127.0.0.1",8008) )

clientSocket.send( MESSAGE_DISCONECT )