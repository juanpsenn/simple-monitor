# simple-monitor
1. Exportar archivos a .zip y subir al servidor correspondiente.
2. Crear nuevo entorno virtual con los requerimientos de `requirements.txt`
3. Crear archivo .env con las variables de entorno correspondientes.
4. Agregar al crontab la siguiente linea: `*/5 * * * * <path_env>/bin/python <path_simple_monitor>/main.py`
5. Chequear que funcione configurando parametros que disparen notificacion, ej. MAX_RAM=10
