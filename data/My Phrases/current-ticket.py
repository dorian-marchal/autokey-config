# current respawn ticket (require RESPAWN_PATH env var)
result = subprocess.check_output(['/bin/bash', '-i', '-c', 'cd $RESPAWN_PATH && git rev-parse --abbrev-ref HEAD | grep -o "[[:digit:]]*" | xargs echo -n'])
keyboard.send_keys(result)
