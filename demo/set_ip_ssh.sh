ifconfig eth0 down
ifconfig eth0 140.113.225.248 netmask 255.255.255.0 up
route add default gw 140.113.225.248
echo "nameserver 1.1.1.1" > /etc/resolv.conf
PID=$(ps -e|grep dropbear | grep -v grep|awk '{print $1}')
kill ${PID}
/usr/sbin/dropbear -p 22
