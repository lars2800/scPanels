import socket
from typing import Callable
import keyboard
import time
import mouse

# Styling ex use: f"{red}Somthing went wrong{white}" or f"{green}Very good!{white}"
black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"

# Constants
DISCONECT_MEASEGE = b"CONNECTION-DISCONECTED" # sync to server

# Main code
class HostServer:
    def __init__(self,hostAddr:tuple[str,int] = ("127.0.0.1",8008)) -> None:
        
        self.hostAddr = hostAddr # Address of server
        self.dataBuffferSize = 32768 # The buffer size of the socket when receving

        # Init server socket
        self.hostSock = socket.socket(  )
        self.hostSock.bind(self.hostAddr)

    def onData(self,data:bytes) -> None:
        """
        Function called when data is recived from client

        Args:
            data (bytes): The data recived

        Returns:
            NoneType: Does not return anything
        """        

        # Function generators

        def genKeyClickFunc(key:str|int) -> Callable:
            """
            Createzs an function which sends the key given

            Args:
                key (str|int): Key code or combination of key codes to press

            Returns:
                Callable: The function when called will send a key or key presses defined
            """            

            def r() -> None:
                keyboard.send(key)

            return r
        
        def genKeyLongFunc(key:str|int) -> Callable:

            def r() -> None:
                keyboard.press( key )
                time.sleep(0.5)
                keyboard.release( key )

            return r
        
        def genClickLongFunc(mouseBtn) -> Callable:

            def r() -> None:
                mouse.press( mouseBtn )
                time.sleep(0.5)
                mouse.release( mouseBtn )

            return r

        self.events = {
            "KEY_CLICK_U":genKeyClickFunc("u"), # Power Main
            "KEY_CLICK_I":genKeyClickFunc("i"), # Power Engine
            "KEY_CLICK_P":genKeyClickFunc("p"), # Power Weapon
            "KEY_CLICK_O":genKeyClickFunc("o"), # Power Shield

            "KEY_CLICK_F8":genKeyClickFunc("f8"), # Power reset
            "KEY_CLICK_F7":genKeyClickFunc("f7"), # Power shield
            "KEY_CLICK_F6":genKeyClickFunc("f6"), # Power engine
            "KEY_CLICK_F5":genKeyClickFunc("f5"), # Power weapon

            "KEY_CLICK_N":genKeyClickFunc("n"), # Gear toggle
            "KEY_CLICK_K":genKeyClickFunc("k"), # Toggle VTOL

            "KEY_LONG_BACKSPACE":genKeyLongFunc("backspace"), # Self destruct

            "MOUSE_LONG_LEFT":genClickLongFunc("left"), # QT engeage
            "KEY_LONG_B":genKeyLongFunc("b"), # Master mode toggle
            "MOUSE_LONG_MIDDLE":genClickLongFunc("middle"), # Switch operater mode toggle

            "KEY_LONG_M":genKeyLongFunc("b"), # MINE mode ONLY IN SCM

            "KEY_LONG_TAB":genKeyLongFunc("tab"), # Ping ( scan )
        }

        if ( data.decode() in self.events.keys()  ):
            print(f"\n{green}Data recived: {data.decode()}{white}")
            self.events[data.decode()]()
        
        else:
            print(f"\n{red}INVAILID Data recived: {data.decode()}{white}")
    
    def run(self) -> None:

        print("Listining host sokcet")
        self.hostSock.listen()
        
        print("waiting for client")
        self.clientSock, self.clientAddr = self.hostSock.accept()
        print(f"Client accepted from: {self.clientAddr}")

        print("Disabeling client blocking")
        self.clientSock.setblocking(False)


        running = True
        
        try:

            while (running):
                
                try:
                    
                    data = self.clientSock.recv(self.dataBuffferSize)

                    if data:

                        self.onData(data)

                        if data == b"CONNECTION-DISCONECTED":
                            raise ConnectionAbortedError


                except BlockingIOError:
                    pass

                except (ConnectionAbortedError):
                    running = False
                    print(f"{red}Client disconnected!{white}")

        except KeyboardInterrupt:
            running = False
        


if __name__ == "__main__":
    server = HostServer()
    server.run()