#!/usr/bin/bash
if [[ $(ls -A  ~/.ssh/*.pub | head -c1 | wc -c) -ne 0 ]]; then

  host_ips=`cat /etc/hosts | egrep -iv '(ip[v]*6|^$|^#)' | awk '{print $1}'`
  echo "Enter Password for $USER: "
  read -s password
  # echo "password: $password"
  
  for host_ip in $host_ips
  do
    $ip = `hostname -I`
    if [[ $host_ip != $ip ]];; then
      echo ssh-copy-id ${USER}@$host_ip
      sshpass -p $password ssh-copy-id -o StrictHostKeyChecking=no ${USER}@$host_ip
    else
      echo "Skipping host ip: $host_ip because current IP is $ip"
    fi
  done
else
  echo "You need to generate SSH keys for $USER, ssh-keygen -t rsa -b 4096"
fi
