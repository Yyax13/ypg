#!/bin/bash

sudo chmod 666 /root/.bashrc

add_alias() {
    local user="$1"
    local alias_line="alias ypg='python $script_dir/main.py'"
    local bashrc_file="/home/$user/.bashrc"

    if [ "$user" = "root" ]; then
        bashrc_file="/root/.bashrc"
    fi

    if [ -f "$bashrc_file" ]; then
        if ! grep -qF "$alias_line" "$bashrc_file"; then
            echo "$alias_line" >> "$bashrc_file"
            echo "Installed, run 'ypg' to see"
        else
            echo "Already installed at $user."
        fi
    else
        echo "The $bashrc_file from $user can't be created. Run install.sh with sudo"
    fi
}

if [[ "$(uname -s)" == "Linux" ]]; then
    # Obtém o diretório do script em execução
    script_dir="$(dirname "$(readlink -f "$0")")"
    
    echo "Installed, run 'ypg' to see"
    add_alias "$USER"
    add_alias "root"
  
elif [[ "$(uname -s)" == "MINGW"* ]]; then
    echo "Non-supported OS, pls use Unix distros"
else
    echo "Non-supported OS, pls use Unix distros"
fi
