# Enter script code

result = subprocess.check_output("cd /data/projects/jvc-respawn && git current-branch | xargs echo -n", shell=True)
keyboard.send_keys(result)