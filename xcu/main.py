#!/usr/bin/env python3
"""
xpip - Un wrapper de pip para instalar paquetes desde el repositorio PyPI de Cuba
"""

import sys
import subprocess
import argparse

# Configuración del repositorio cubano
CUBA_INDEX_URL = "http://nexus.prod.uci.cu/repository/pypi-proxy/simple/"
CUBA_TRUSTED_HOST = "nexus.prod.uci.cu"

def run_pip_command(args):
    """
    Ejecuta un comando pip con la configuración del repositorio cubano
    """
    # Construir el comando pip base
    pip_cmd = [sys.executable, "-m", "pip"]
    
    # Agregar los argumentos del usuario
    pip_cmd.extend(args)
    
    # Agregar la configuración del repositorio cubano si es un comando install
    if args and args[0] == "install":
        pip_cmd.extend([
            "--index-url", CUBA_INDEX_URL,
            "--trusted-host", CUBA_TRUSTED_HOST
        ])
    
    try:
        # Ejecutar el comando
        result = subprocess.run(pip_cmd, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error ejecutando pip: {e}", file=sys.stderr)
        return 1

def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser(
        description="xcu - Instala paquetes de Python desde el repositorio de Cuba",
        add_help=False  # Deshabilitamos la ayuda por defecto para pasarla a pip
    )
    
    # Si no hay argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        print("xcu - Wrapper de pip para el repositorio PyPI de Cuba")
        print("\nUso:")
        print("  xcu install <paquete>     - Instalar un paquete")
        print("  xcu install <paquete1> <paquete2> - Instalar múltiples paquetes")
        print("  xcu list                  - Listar paquetes instalados")
        print("  xcu show <paquete>        - Mostrar información de un paquete")
        print("  xcu uninstall <paquete>   - Desinstalar un paquete")
        print("  xcu --help                - Mostrar ayuda completa de pip")
        print("\nEjemplos:")
        print("  xcu install requests")
        print("  xcu install numpy pandas matplotlib")
        print("  xcu install -r requirements.txt")
        print(f"\nRepositorio: {CUBA_INDEX_URL}")
        return 0
    
    # Pasar todos los argumentos a pip
    args = sys.argv[1:]
    
    # Mostrar información adicional para comandos install
    if args and args[0] == "install":
        print(f"🇨🇺 Instalando desde el repositorio cubano: {CUBA_INDEX_URL}")
        print("=" * 60)
    
    return run_pip_command(args)

if __name__ == "__main__":
    sys.exit(main())