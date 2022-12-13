> **Importante**
> - Proyecto no testeado
> - Proyecto testeado se encuentra en repositorio funcional referenciado al final de este README.

# Install virtualenv

```bash
    $ pip install virtualenv 
```

# Configurate virtualenv

- Crear directorio virtualenv: 
    ```bash
        $ virtualenv -p /path/python venv
    ```

- Activar directorio virtual:
    ```bash
        $ source venv/bin/activate
    ```

- Desactivar directorio virtual:

    ```bash
        $ (venv) deactivate
    ``` 
# Install requirements

Para instalar las librerías necesarias utilizar:

```bash
    $ (venv) pip install -r requirements.txt
```

ó

```bash
    $ (venv) pip install robodk
    $ (venv) pip install python-dotenv
```

# LINUX

- Es necesario configurar las variables de entorno del proyecto en el archivo dentro del directorio raiz del proyecto, llamado `.env`.
    - `ROBOT_IP` : IP del Robot.
    - `MAX_ATTEMPTS` : Máximo de intentos para la conexión con el Robot.
    - `WAIT_CONNECTION` : Tiempo que transcurre entre cada intento de conexión en segundos. 
    - `PATH_STATION` : Ruta del archivo de configuración del Robot con extensión `.rdk`.
  
- Es necesario configurar las variables de entorno, ya sea por linea de comandos o en el archivo `~/.profile` en el directorio `/home` del SO.

    ```bash
    ROBODK_ROOT=$HOME/RoboDK/
    export LD_LIBRARY_PATH="$ROBODK_ROOT/bin/lib"
    export QT_PLUGIN_PATH="$ROBODK_ROOT/bin/plugins/"
    export QT_QPA_PLATFORM_PLUGIN_PATH="$ROBODK_ROOT/bin/plugins"
    ```
- Recargar el archivo profile con las variables de entorno, ejecutar `source ~/.profile` o ejecutarlas por lineas de comando.

- Ejecutar `python main.py`.
# References

- [RodoDK API Python](https://robodk.com/doc/en/PythonAPI/index.html)
- [RoboDK](https://robodk.com/doc/es/Basic-Guide.html)
- [Repositorio Funcional - pdonoso ](https://github.com/pedrodonoso/robodk_arqui_project)
