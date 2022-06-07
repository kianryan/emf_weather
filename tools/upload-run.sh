sudo python3 tools/pyboard.py --no-soft-reset -d /dev/ttyS10 -f mkdir /apps/weather
sudo python3 tools/pyboard.py --no-soft-reset -d /dev/ttyS10 -f cp src/__init__.py :/apps/weather/__init__.py
sudo python3 tools/pyboard.py --no-soft-reset -d /dev/ttyS10 
