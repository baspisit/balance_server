# Chemical Equation Balancing Server
This project calculates balanced chemical equations using a server-based approach. The server is coded in `server.py`, and clients can modify the reactants and products through `client.py`.

## Getting Started
### Prerequisites

Make sure you have Docker installed on your system for containerizing the server.

### Step 1: Create Docker Image for the Server
1. First, you need to create a Docker image for the server. 

Build the Docker image by running the following command:
```bash
docker build -t chemical-equation-balancer .
```
Step 2: Run the Server in a Container
Once the image is built, run the Docker container using the command below:
```bash
docker run -d -p 65432:65432 chemical-equation-balancer
```
This will start the server and bind it to port 65432. The server is now running and ready to process requests for balancing chemical equations.

Step 3: Modify Reactants and Products in `client.py`
Open `client.py` and modify the chemical reactants and products as needed. For example, update the variables representing the chemical equation to be balanced.
Example of modifying reactants/products:
```python
# In client.py
reactants = ['H2', 'O2']
products = ['H2O']
```
Run `client.py` to send the modified reactants and products to the server for balancing.
```bash
python client.py
```
The client script will send the reactants and products to the server, which will calculate and return the balanced equation.
