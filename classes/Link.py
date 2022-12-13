from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

from robodk import *
from robolink import *

import signal

class Link:
    rdk: Robolink
    path_station: str
    robot: Item
    robot_name: str
    robot_ip: str
    m_a: int
    w_c: int

    def __init__(self, rdk: Robolink, robot_name: str, path_station: str, robot_ip: str, m_a: int, w_c: int):
        """
        #### Instanciar clase Link.
        ----------
        RDK : Robolink
            Instancia Robolink.
        robot_name : str
            Nombre del robot importado en el archivo .rdk
        path_station : str
            Dirección del directorio del archivo .rdk de configuración.
        robot_ip : str
            IP del Robot.
        m_a: str
            Máximo de intentos de conexión.
        w_c: str
            Tiempo de espera en segundos entre cada intento de conexión.
        """
        self.rdk = rdk
        self.robot_name = robot_name
        self.path_station = path_station
        self.robot_ip = robot_ip
        self.m_a = m_a
        self.w_c = w_c
        
        # ejecuta la señal que inicia el handler de interrupción
        signal.signal(signal.SIGINT, self.handler) 
        return None

    def set_path_station(self, path_station: str):
        self.path_station = path_station
    def set_robot_name(self, robot_name: str):
        self.robot_name = robot_name
    def set_robot_ip(self, robot_ip: str):
        self.robot_ip = robot_ip
    def set_m_a(self, m_a: int):
        self.m_a = m_a
    def set_w_c(self, w_c: int):
        self.w_c = w_c
        
    def create_robot(self):
        """
        #### Instancia y crea el Item que representa al Robot.
        ----------
        Requiere:
            - RDK.
            - Nombre del Robot(robot_name).
            - constante ITEM_TYPE_ROBOT
        """
        self.robot = self.rdk.Item(self.robot_name, ITEM_TYPE_ROBOT)
        valid = self.robot.Valid()
        if (not valid):
            raise Exception("Robot no se pudo cargar.")
        print("INF: Robot cargado correctamente.")
        return True
    
    def create_station(self):
        """
        #### Crea el parametro que guarda la dirección del archivo de configuración .rdk.
        ----------
        Requiere:
            - RDK.
            - Dirección de la Estación(path_station).
            - constante FILE_OPENSTATION
        """
        exist_path = self.rdk.getParam(param=FILE_OPENSTATION, str_type=True)
        print(exist_path == None, type(exist_path) != str, exist_path)
        if ( type(exist_path) != 'str' ):
            print("WAR: No existe variable de entorno.")
            self.rdk.AddFile(self.path_station)
            print("INF: Archivo de configuración cargado.")
        else:
            print("INF: Archivo ya existe.")

        print("INF: Archivo cargado -> ",self.rdk.getParam(param=FILE_OPENSTATION, str_type=True))
        return True

    def connection_robot(self):
        """
        #### Conectar con el Robot generando en la instancia Item.
        ----------
        Requiere:
            - Item del robot(self.robot).
            - Dirección IP del Robot(robot_ip).
            - Máximo de intentos de la conexión(m_a).
            - Tiempo de espera entre cada intento en segundos(w_c).
        """
        robot_connection = self.robot.ConnectSafe(robot_ip=self.robot_ip, max_attempts=self.m_a, wait_connection=self.w_c)
        if (robot_connection): 
            print("INF: Conectado")
        else: 
            print("INF: NO Conectado")
            raise Exception("Robot no seleccionado o no válido.")
        return True

    def disconnnect(self):
        """
        #### Desconecta el Robot generando en la instancia Item.
        ----------
        Requiere:
            - Item del robot(self.robot).
            - RDK.
        """
        self.robot.Disconnect()
        self.rdk.CloseRoboDK()
        return True

    def print_robot(self):
        """
        #### Imprime el estado del Robot.
        ----------
        Requiere:
            - Instancia del Robot(self.robot).
            - RDK.
        """
        name = self.robot.Name()
        active_station = self.rdk.ActiveStation().Name()
        print("NAME: {} \t STATION: {}".format(name, active_station))
        return True
    
    def handler(self, signum, frame): 
        """
        #### Handler que ayuda a la interrupción del programa.
        ----------
        """
        res = input("Ctrl-c presionado. Quieres salir? y/n ")
        if res == 'y':
            self.disconnnect()
            print("INF: Terminado")
            quit(1)
        return True
