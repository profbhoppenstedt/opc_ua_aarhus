from opcua import Client
import time

# Connect to the server
client = Client("opc.tcp://localhost:4840/freeopcua/server/")

try:
    # Establish connection
    client.connect()
    print("Connected to the server")

    # Find the variable in the server's address space
    uri = "http://example.org"
    idx = client.get_namespace_index(uri)
    my_var = client.get_node(f"ns={idx};i=2")

    # Read and display the variable's value periodically
    while True:
        value = my_var.get_value()
        print(f"Variable value: {value}")
        time.sleep(1)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the server")
