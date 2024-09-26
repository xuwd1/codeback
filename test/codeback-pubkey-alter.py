import sys
import os
import pathlib
import subprocess

class ParsedEnvvars:
    def __init__(self) -> None:
        self.reverse_port = '56789'
        self.local_ecdsa_pubkey = 'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF5'
        self.local_ed25519_pubkey = 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI'
        self.local_rsa_pubkey = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD'



def adjust_ssh_known_hosts(parsed_envvars, known_host_file_path = pathlib.Path("~/.ssh/known_hosts").absolute()):
    ssh_keygen_remove_cmommand = ["ssh-keygen", "-R", f"[localhost]:{parsed_envvars.reverse_port}"]
    subprocess.run(ssh_keygen_remove_cmommand, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pubkeys = [parsed_envvars.local_ecdsa_pubkey, parsed_envvars.local_ed25519_pubkey, parsed_envvars.local_rsa_pubkey]
    pubkeys = [pubkey for pubkey in pubkeys if pubkey is not None]
    with open(known_host_file_path, "a") as known_hosts_file:
        for pubkey in pubkeys:
            pubkey_record_string = f"[localhost]:{parsed_envvars.reverse_port} {pubkey}"
            known_hosts_file.write(pubkey_record_string + "\n")


adjust_ssh_known_hosts(ParsedEnvvars(), pathlib.Path("/home/david/workspace/pkgbuild-repo/codeback/test/known_hosts_testing"))