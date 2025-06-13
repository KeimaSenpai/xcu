![xcu](https://github.com/user-attachments/assets/1c3e9cc6-645f-448f-85b6-476ae4095f66)
# xcu - Instalador de paquetes Python para Cuba 🇨🇺

`xcu` es un wrapper de pip que facilita la instalación de paquetes de Python desde el repositorio PyPI de Cuba, eliminando la necesidad de escribir comandos largos con parámetros de configuración.

## Características

- ✅ Compatible con Windows, macOS y Linux
- ✅ Interfaz simple y familiar (como pip)
- ✅ Configuración automática del repositorio cubano
- ✅ Soporte para todos los comandos de pip
- ✅ Instalación de paquetes sin gasto de megas
- ✅ Instalación sencilla
- ✅ Inicia proyecto con simples plantillas

## Instalación

### Opción 1: Desde el código fuente
```bash
git clone https://github.com/KeimaSenpai/xcu.git
cd xcu
pip install .
```

### Opción 2: Instalación desde pypi
```bash
pip install xcu
```

## Uso

Una vez instalado, puedes usar `xcu` como si fuera `pip`:

### Iniciar un proyecto
```bash
xcu init Mi-proyecto
```

### Para iniciarlo desde la carpeta inicial
```bash
xcu init .
```

### Instalar un paquete
```bash
xcu install requests
```

### Instalar múltiples paquetes
```bash
xcu install numpy pandas matplotlib
```

### Instalar desde requirements.txt
```bash
xcu install -r requirements.txt
```

### Otros comandos (funcionan igual que pip)
```bash
xcu list                    # Listar paquetes instalados
xcu show requests           # Mostrar información de un paquete
xcu uninstall requests      # Desinstalar un paquete
xcu --help                  # Mostrar ayuda
```

## ¿Qué hace por detrás?

Cuando ejecutas:
```bash
xcu install requests
```

En realidad se ejecuta:
```bash
python -m pip install requests --index-url http://nexus.prod.uci.cu/repository/pypi-proxy/simple/ --trusted-host nexus.prod.uci.cu
```

## Estructura del proyecto

```
xcu/
├── xcu/
│   ├── __init__.py
│   └── main.py
├── README.md
└── LICENSE
```

## Requisitos

- Python 3.6 o superior
- pip (incluido con Python)

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Repositorio PyPI de Cuba

- **URL**: http://nexus.prod.uci.cu/repository/pypi-proxy/simple/
- **Host de confianza**: nexus.prod.uci.cu

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor crea un issue en el repositorio de GitHub.
