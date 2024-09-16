#!/usr/bin/env python3

import socket

def send_equation(reactants, products, server_ip='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    # Prepare the data to send (reactants and products as comma-separated strings)
    data = ",".join(reactants) + "|" + ",".join(products)
    print("Sending data:", data)
    client_socket.sendall(data.encode())

    # Receive the balanced equation from the server
    balanced_equation = client_socket.recv(1024).decode()
    print(balanced_equation)

    client_socket.close()

if __name__ == "__main__":
    reagent = ["Pb(NO3)2", "KI"]
    product = ["PbI2", "KNO3"]
    send_equation(reagent, product)
