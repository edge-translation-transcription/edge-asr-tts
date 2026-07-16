#!/usr/bin/bash

script_name=$(basename -- "$0")

if [ "$EUID" -ne 0 ]
  then echo "This script must be run as root, restart like: sudo ./$script_name"
  exit -1 
fi

if [ -z ${R4ALL_DIR+x} ]; then 
	echo "You must set env variable: 'R4ALL_DIR' to the github clone directory of r4a";
	exit -1
fi

if [ -z ${GRAFANA_ADMIN_PASSWORD+x} ]; then
        echo "You must set env variable: 'GRAFANA_ADMIN_PASSWORD' to the admin password for grafana";
        exit -1
fi


export ANSIBLE_HOST_KEY_CHECKING=False

apt-add-repository -y ppa:ansible/ansible

apt update -y
apt upgrade -y

# Install tools for use
apt install -y git expect software-properties-common openssh-server
apt install -y ansible ssh-askpass

# Install ansible roles
ansible-galaxy role install geerlingguy.docker
ansible-galaxy collection install prometheus.prometheus
ansible-galaxy collection install community.grafana
