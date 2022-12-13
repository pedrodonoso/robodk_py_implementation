
from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

from robodk import *
from robolink import *

import os
import signal
import time
 


def connect_by_name(RDK: Robolink, name_robot: str, path_station: str, robot_ip: str):
    """
    Conectar a robot con IP.
    ----------
    RDK : Robolink
        Instancia Robolink.
    name_robot : str
        Nombre del robot importado en el archivo .rdk
    path_station : str
        Dirección del directorio del archivo .rdk de configuración.
    robot_ip : str
        IP del Robot.
    Returns
    -------
    RDK: Robolink
        Instancia Robolink.    
    robot: Item
        Instancia de Item del Robot.
    """
    print("INF: Conectando..")

    MAX_ATTEMPTS = int(os.environ['MAX_ATTEMPTS'])
    WAIT_CONNECTION = int(os.environ['WAIT_CONNECTION'])

    print("IP: ", robot_ip)

    try:
        exist_path = RDK.getParam(param=FILE_OPENSTATION, str_type=True)
        # print("exist: ", exist_path)
        if (type(exist_path) != 'str'):
            print("WAR: No existe variable de entorno.")
            RDK.AddFile(path_station)
            print("INF: Archivo de configuración cargado.")
        
        print("PATH STATION CHARGED: ",RDK.getParam(param=FILE_OPENSTATION, str_type=True))

        # cargamos el robot importado en .rdk
        robot = RDK.Item(name_robot, ITEM_TYPE_ROBOT)
        
        def handler(signum, frame):
            res = input("Ctrl-c presionado. Quieres salir? y/n ")
            if res == 'y':
                # exit(1)
                robot.Disconnect()
                RDK.CloseRoboDK()
                print("Terminado")
                quit(1)
        
        signal.signal(signal.SIGINT, handler)

        print("NAME ROBOT: ",robot.Name())

        print("ACTIVE_STATION: ", RDK.ActiveStation().Name())

        robot_connection = robot.ConnectSafe(robot_ip=robot_ip, max_attempts=MAX_ATTEMPTS, wait_connection=WAIT_CONNECTION)
        # robot_connection = robot.Connect(robot_ip=robot_ip)

        if not robot.Valid():
            raise Exception("Robot not selected or not valid")
            quit()

        if (robot_connection):
            print("INF: Conectado")
            # robot.Disconnect()
        else:
            print("INF: NO Conectado")
            raise Exception("Robot not selected or not valid")

        return RDK, robot
        # print("estado conexión: ", robot.ConnectedState()[1])  
        # RDK.CloseRoboDK()
        # print("Terminado")
    except:
        # robot.Disconnect()
        # RDK.CloseRoboDK()
        print("Terminado except")
        return RDK, robot
    finally:
        # robot.Disconnect()

        ## RDK.CloseRoboDK()
        print("Terminado")
        return RDK, robot
