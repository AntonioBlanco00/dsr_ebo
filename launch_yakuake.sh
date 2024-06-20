#!/bin/bash

# Abrir Yakuake
yakuake &

# Esperar un momento para que Yakuake se abra completamente
sleep 3

# Detectar la carpeta base automáticamente (la carpeta en la que se encuentra este script)
carpeta_base=$(dirname "$(realpath "$0")")

# Definir las rutas relativas a la carpeta base
ruta1="$carpeta_base/components/dsr-graph/components/idserver"
ruta2="$carpeta_base/agents/tts_agente"
ruta3="$carpeta_base/agents/emove_agent"
ruta4="$carpeta_base/agents/app_tts"

# Función para abrir una nueva pestaña en Yakuake y ejecutar un comando en ella
function abrir_nueva_pestania() {
    xdotool key ctrl+shift+t
    sleep 0.5
    xdotool type "$1"
    xdotool key Return
}

# Abrir las cuatro shells en distintas rutas
abrir_nueva_pestania "cd $ruta1"
abrir_nueva_pestania "cd $ruta2"
abrir_nueva_pestania "cd $ruta3"
abrir_nueva_pestania "cd $ruta4"

