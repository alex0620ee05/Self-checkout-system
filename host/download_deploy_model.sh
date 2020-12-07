wget --load-cookies cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1n4QKbIZ8AxF_X80ReYuWx1tLMMPlXavv' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1n4QKbIZ8AxF_X80ReYuWx1tLMMPlXavv" -O deploy_model.pb && rm -rf cookies.txt
mkdir ssd_mobilenet
mv deploy_model.pb ssd_mobilenet
