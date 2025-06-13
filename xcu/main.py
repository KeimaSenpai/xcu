#!/usr/bin/env python3
"""
xpip - Un wrapper de pip para instalar paquetes desde el repositorio PyPI de Cuba
"""

import os
import sys
import subprocess
import argparse
import shutil

# Configuración del repositorio cubano
CUBA_INDEX_URL = "http://nexus.prod.uci.cu/repository/pypi-proxy/simple/"
CUBA_TRUSTED_HOST = "nexus.prod.uci.cu"
# Repositorios de templates
TEMPLATES = {
    "telegram-bot": {
        "python-telegram-bot": {
            "simple": "https://github.com/KeimaSenpai/xcu/plantillas/telegram-bot/python-telegram-bot/simple",
            "mongodb": "https://github.com/KeimaSenpai/xcu/plantillas/telegram-bot/python-telegram-bot/mongodb"
        },
        "kurigram": {
            "simple": "https://github.com/KeimaSenpai/xcu/plantillas/telegram-bot/kurigram/simple",
            "mongodb": "https://github.com/KeimaSenpai/xcu/plantillas/telegram-bot/kurigram/mongodb"
        }
    }
}

# Clonado de repos de github con las plantillas
def clone_template(repo_url, destination):
    """
    Clona un repositorio template en el destino
    """
    try:
        subprocess.run(["git", "clone", repo_url, destination], check=True)
        # Eliminar el directorio .git para empezar limpio
        shutil.rmtree(os.path.join(destination, ".git"), ignore_errors=True)
        print(f"✅ Proyecto creado en: {destination}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al clonar el repositorio: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def init_project(args):
    """
    Inicializa un nuevo proyecto
    """
    if len(args) < 1:
        print("❌ Error: Debes especificar un nombre para el proyecto")
        print("Uso: xcu init <nombre|.>")
        return 1

    project_name = args[0]
    
    # Si es ".", usar el directorio actual
    if project_name == ".":
        project_path = os.getcwd()
    else:
        project_path = os.path.join(os.getcwd(), project_name)
        # Verificar si el directorio ya existe
        if os.path.exists(project_path) and project_name != ".":
            print(f"❌ Error: El directorio {project_name} ya existe")
            return 1

    print("🚀 Iniciando nuevo proyecto...")
    print("\n📋 Selecciona el tipo de proyecto:")
    print("1) Telegram Bot")
    print("2) Web")
    
    try:
        type_choice = input("\nSelección (1-2): ").strip()
        
        if type_choice == "1":
            print("\n📱 Selecciona el framework para el bot:")
            print("1) python-telegram-bot")
            print("2) Kurigram")
            
            framework = input("\nSelección (1-2): ").strip()
            
            print("\n💾 ¿Quieres incluir base de datos?")
            print("1) Simple (sin base de datos)")
            print("2) MongoDB")
            
            db_choice = input("\nSelección (1-2): ").strip()
            
            # Determinar el template a usar
            framework_name = "python-telegram-bot" if framework == "1" else "kurigram"
            db_type = "simple" if db_choice == "1" else "mongodb"
            
            template_url = TEMPLATES["telegram-bot"][framework_name][db_type]
            
            # Clonar el repositorio
            if clone_template(template_url, project_path):
                print("\n📦 Instalando dependencias...")
                requirements_path = os.path.join(project_path, "requirements.txt")
                if os.path.exists(requirements_path):
                    subprocess.run(["xcu", "install", "-r", requirements_path])
                print("\n🎉 ¡Proyecto creado exitosamente!")
                return 0
            return 1
            
        elif type_choice == "2":
            print("\n🌐 Selecciona el framework web:")
            print("1) FastAPI")
            print("2) Flask")
            
            framework = input("\nSelección (1-2): ").strip()
            
            print("🚧 Templates web en desarrollo...")
            return 1
            
        else:
            print("❌ Opción inválida")
            return 1
            
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada")
        return 1


# Inicio de las instalaciones con xcu
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
        print("  xcu init <nombre>         - Inicializar un nuevo proyecto")
        print("  xcu init .                - Inicializar un nuevo proyecto en el directorio actual")
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