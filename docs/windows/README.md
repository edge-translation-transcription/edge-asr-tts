## Prerequisites
1. Install WSL: wsl --install
2. Install [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
3. Install [Pulseaudio windows binary](https://pgaskin.net/pulseaudio-win32/)

## Setup
1. Add the following line (after line 64) in file 'C:\Program Files (x86)\PulseAudio\etc\pulse\default.pa' to:
```
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;<subnet_of_wsl> auth-anonymous=1
```

Note: Be sure to replace the IP subnet with the IP address of the WSL instance where the pulseaudio client will connect from, which can be found by:
  - Start terminal window as administrator
  - Open WSL: `wsl`
  - Get subnet: `ip a | grep brd | grep inet | grep 172 | awk '{print $2}'`
  - Use this result as the subnet value at line 66 of `default.pa`

2. Restart the PulseAudio service using Task Manager --> Services --> Restart

3. Open a windows powershell as admin to allow the firewall to enable traffic between WSL and the Windows Host:
```
Enable-NetFirewallRule -DisplayName 'Virtual Machine Monitoring (Echo Request - ICMPv4-In)'
Enable-NetFirewallRule -DisplayName 'Virtual Machine Monitoring (Echo Request - ICMPv6-In)'
```

4. Now within WSL, ensure these directories exist:
```
ls /mnt/wslg/runtime-dir/pulse/native
ls /run/user/1000/pulse/native
```

5. Create a symbolic link:
```
ln -f -s /mnt/wslg/runtime-dir/pulse/native /run/user/1000/pulse/native
```

6. Ensure these environment variables are set:
```
echo $PULSE_SERVER
```
  --> Should look like `/mnt/wslg/PulseServer` (export this if not set)
```
echo $R4ALL_DIR
```
  --> Should look like the cloned repo directory (export this if not set)

9. Finally, launch docker container:
```
docker run -it --privileged --name r4all-test \
--rm -v ${R4ALL_DIR}:/usr/app/src \
-e "PULSE_SERVER=${PULSE_SERVER}" \
-v /mnt/wslg/:/mnt/wslg/ \
--volume /var/www/metrics:/usr/app/src/csv \
--env-file=${HOME}/r4a_secrets.env \
-p 8501:8501 \
-e DISPLAY=$DISPLAY --user openvino -w /usr/app/src \
--group-add=audio r4all:0.0.1
```


