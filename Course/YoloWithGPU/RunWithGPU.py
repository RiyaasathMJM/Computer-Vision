from openvino import Core

ie = Core()
print("Available devices:", ie.available_devices)