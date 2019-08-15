import pygatt

# The BGAPI backend will attempt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
adapter = pygatt.BGAPIBackend()

try:
    adapter.start()
    device = adapter.connect('80:E1:26:00:68:58')
    value = device.char_read("0xc000")
finally:
    adapter.stop()
