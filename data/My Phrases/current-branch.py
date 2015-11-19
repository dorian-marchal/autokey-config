# gcb = current respawn branch (require RESPAWN_PATH env var)
result = subprocess.check_output(['/bin/bash', '-i', '-c', 'cd $RESPAWN_PATH && git current-branch | xargs echo -n'])
keyboard.send_keys(result)
