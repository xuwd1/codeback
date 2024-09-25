# Codeback

## Usage

1. On your local machine:
```zsh

connect remote-host 
# !! It is expected that your ssh config/key is properly setup that a username is not needed
# Now you can see you are ssh connected to the remote host
```

2. On the remote host:
```zsh
codeback ./workspace
# !! It is also expected that your remote host has a proper ssh config/key setup
# Now a vscode window should open up on your local machine with the remote workspace dir opened
```

## Installation

Arch Linux users can just build and install the `codeback` package using the provided `PKGBUILD`:

1. `makepkg -i`

## The `connect` python script

The `connect` script works as the following:
1. Given the remote hostname, it first ssh connects to it and try to find a free port for establishing a reverse ssh tunnel. The free port is found by executing `netstat -tln` on the remote host.
2. Once the free port is found, the script substitutes itself using `execvpe` with an actual ssh connection to the remote host with the reverse tunnel established.
  - Alongwith the ssh connection, several envvars are passed to the remote host using ssh -oSendEnv, including:
    - `CODEBACK_XAUTHORITY`: contains a copy of local machine's `XAUTHORITY` envvar
    - `CODEBACK_XDISPLAY`: contains the local machine's `DISPLAY` envvar
    - `CODEBACK_WAYLAND_DISPLAY`: contains the local machine's `WAYLAND_DISPLAY` envvar
    - `CODEBACK_SOURCE_ADDR` : contains the hostname that the local used for connecting to the remote host
    - `CODEBACK_REVERSE_PORT`: contains the port number on the remote host where the reverse tunnel is established

  - For the remote host to accept the envvars, `99-codeback.conf` has to be put inside `/etc/ssh/sshd_config.d/` directory.

## The `codeback` python script

The `codeback` script, when executed on the remote host, opens up a **local** vscode remote window which connects to the remote host and opens the workspace dir specified in the remote command line.

This script works as the following:
1. It first tries to gather the above listed envvars.
2. It then ssh connect back through the ssh tunnel at localhost:`CODEBACK_REVERSE_PORT` to the local machine.
3. Finally, it launches a `code` ssh session window on the local machine that opens up the given workspace dir. The local window can be broughtup correctly since the script would automaticaly set the necessary`XAUTHORITY`, `DISPLAY` and `WAYLAND_DISPLAY` envvars.



