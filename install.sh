#!/bin/bash

# Dê permissão de escrita ao arquivo /root/.bashrc
sudo chmod 666 /root/.bashrc

# Função para adicionar o alias em um arquivo .bashrc
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
            echo "Alias 'ypg' adicionado ao $bashrc_file do usuário $user."
        else
            echo "O alias 'ypg' já existe no $bashrc_file do usuário $user."
        fi
    else
        echo "O arquivo $bashrc_file do usuário $user não foi encontrado. O alias não pôde ser adicionado."
    fi
}

# Verifica se o sistema operacional é Linux
if [[ "$(uname -s)" == "Linux" ]]; then
    # Obtém o diretório do script em execução
    script_dir="$(dirname "$(readlink -f "$0")")"
    
    # Define o comando 'ypg' como um alias para 'python main.py' no diretório do script
    echo "Alias 'ypg' será adicionado aos perfis do usuário atual e do usuário root."
    add_alias "$USER"
    add_alias "root"
  
# Verifica se o sistema operacional é Windows (usando o Windows Subsystem for Linux)
elif [[ "$(uname -s)" == "MINGW"* ]]; then
    echo "Sistema operacional não suportado, por favor use Linux"
else
    echo "Sistema operacional não suportado, por favor use Linux"
fi
