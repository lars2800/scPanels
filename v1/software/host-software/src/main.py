from emulater import emulate_mouse_scroll,emulate_keys,emulate_mouse_press,check_process_running
from connection import runServer
import traceback
import os
import json

SC_PROCESS_NAME = "starCitizen.exe"
SERVER_ADDR = ("127.0.0.1",8123)

def main() -> None:

    # Check if star citizen is running
    if ( check_process_running( SC_PROCESS_NAME ) == False ):
        print("Star citizen not detected or not running")
        print("Continou when running")
        os.system("pause")
    
    def eventCallback(eventJson:str):

        def genPressFunc(*keys:tuple[str]):

            def _r() -> None:
                emulate_keys(*keys)
            
            return _r
        
        def genLongPressFunc(*keys:tuple[str],duration:float = 3.5):

            def _r() -> None:
                emulate_keys(*keys,duration)
            
            return _r

        def genClickFunc(type:str):
            def _r() -> None:
                emulate_keys(type)
            
            return _r
        
        def genLongClickFunc(type:str,duration:float = 3.5):

            def _r() -> None:
                emulate_mouse_press(type,duration)
            
            return _r

        eventLookup = {
            "switchCruiseControl":genPressFunc("c",),
            "switchControlMode":genLongClickFunc("b",),
            "switchMasterMode":genClickFunc("middle",),
            "switchMiningMode":genLongPressFunc("m",),
            "activatePing":genLongPressFunc("tab",duration=1,),
            "switchPowerMain":genPressFunc("u",),
            "switchPowerEngines":genPressFunc("i",),
            "switchPowerWeapons":genPressFunc("p",),
            "switchPowerShield":genPressFunc("o",),
            "switchGear":genPressFunc("n",),
            "activateQtDrive":genLongClickFunc("left",2,)
        }

        # Convert packet data into json
        eventDict = json.loads(eventJson)

        # Lookup the correct function and call it
        eventLookup[eventDict["name"]]()
    
    runServer( SERVER_ADDR, eventCallback )

if __name__ == "__main__":


    if ( os.name != "nt" ):
        print("Warning system not running nt(windows os), this os is not tested and may not work")

    try:

        main()

    except Exception:

        # Log exception
        print(f"An error occured whilst running main")
        traceback.print_exc()

        # Wait until key press till quit
        os.system("pause")
        quit()