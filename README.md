# xpip-cu - Instalador de paquetes Python para Cuba 🇨🇺

`xpip-cu` es un wrapper de pip que facilita la instalación de paquetes de Python desde el repositorio PyPI de Cuba, eliminando la necesidad de escribir comandos largos con parámetros de configuración.

## Características

- ✅ Compatible con Windows, macOS y Linux
- ✅ Interfaz simple y familiar (como pip)
- ✅ Configuración automática del repositorio cubano
- ✅ Soporte para todos los comandos de pip
- ✅ Instalación sencilla

## Instalación

### Opción 1: Desde el código fuente
```bash
git clone https://github.com/tuusuario/xpip-cu.git
cd xpip-cu
pip install .
```

### Opción 2: Instalación en modo desarrollo
```bash
git clone https://github.com/tuusuario/xpip-cu.git
cd xpip-cu
pip install -e .
```

## Uso

Una vez instalado, puedes usar `xpip-cu` como si fuera `pip`:

### Instalar un paquete
```bash
xpip-cu install requests
```

### Instalar múltiples paquetes
```bash
xpip-cu install numpy pandas matplotlib
```

### Instalar desde requirements.txt
```bash
xpip-cu install -r requirements.txt
```

### Otros comandos (funcionan igual que pip)
```bash
xpip-cu list                    # Listar paquetes instalados
xpip-cu show requests           # Mostrar información de un paquete
xpip-cu uninstall requests      # Desinstalar un paquete
xpip-cu --help                  # Mostrar ayuda
```

## ¿Qué hace por detrás?

Cuando ejecutas:
```bash
xpip-cu install requests
```

En realidad se ejecuta:
```bash
python -m pip install requests --index-url http://nexus.prod.uci.cu/repository/pypi-proxy/simple/ --trusted-host nexus.prod.uci.cu
```

## Estructura del proyecto

```
xpip-cu/
├── xpip-cu/
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