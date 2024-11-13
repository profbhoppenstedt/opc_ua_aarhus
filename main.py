from opcua import Server
from datetime import datetime
import time

# Create an OPC UA Server instance
server = Server()

# Set the server endpoint
server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

# Set the server name
server_name = "Simple OPC UA Server"
server.set_server_name(server_name)

# Register a new namespace
uri = "http://example.org"
idx = server.register_namespace(uri)

# Create an object and a variable in the server's address space
my_obj = server.nodes.objects.add_object(idx, "MyObject")
my_var = my_obj.add_variable(idx, "MyVariable", 0)

# Make the variable writable
my_var.set_writable()

# Start the server
server.start()

print(f"{server_name} started at opc.tcp://localhost:4840/freeopcua/server/")
try:
    while True:
        # Update the variable's value every second
        my_var.set_value(my_var.get_value() + 1)
        print(f"Variable updated: {my_var.get_value()}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping server...")
finally:
    server.stop()
    print("Server stopped")
