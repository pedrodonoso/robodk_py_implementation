from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

from robodk import *
from robolink import *

import signal
import os
from dotenv import load_dotenv

from classes.Link import Link
from classes.Moves import Moves

sys.path.append('src/')

load_dotenv() # carga variables de entorno

PATH_STATION = os.environ['PATH_STATION']
ROBOT_IP = os.environ['ROBOT_IP']
ROBOT_NAME = os.environ['ROBOT_NAME']
MAX_ATTEMPTS = int(os.environ['MAX_ATTEMPTS'])
WAIT_CONNECTION = int(os.environ['WAIT_CONNECTION'])

try:
    # RDK = Robolink(args=['/NOSPLASH','/NOSHOW']) 
    RDK = Robolink() 
    # RDK.setRunMode(RUNMODE_RUN_ROBOT)
    RDK.setRunMode(RUNMODE_SIMULATE )

    # crea link RDK
    link = Link(rdk=RDK, robot_name=ROBOT_NAME, path_station=PATH_STATION, robot_ip=ROBOT_IP, m_a=MAX_ATTEMPTS, w_c=WAIT_CONNECTION)

    # establece variables de entorno para RDK
    link.create_station()

    # crea instancia Item Robot 
    link.create_robot()

    # imprime nombre del Robot y estación activa de trabajo
    link.print_robot()

    # genera conexión con robot
    link.connection_robot()

    # instancia la clase para realizar movimientos
    # moves = Moves(robot=link.robot)

    # realiza movimiento de prueba
    # moves.movement_test()

except Exception as e:
    print("Terminado except: {}".format(e))
    exit()
    # quit(1)

