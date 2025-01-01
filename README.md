
IP Subnet Calculator

This program is a simple tool to help you subnet a network IP address. By providing a network IP address in CIDR notation and the number of hosts required, you can calculate subnets, their subnet masks, and default gateways.

Features
* Accepts a network IP address with CIDR notation.
* Calculates the required number of subnets based on the specified number of hosts.
* Displays each subnet along with its subnet mask and default gateway.

Requirements
* Python 3.6 or higher.

Installation
1. Ensure you have Python installed on your system.
2. Clone or download the script file subnet_calculator.py.

Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the program using the command:
* For Windows “python subnet_calculator.py” for Mac “python3 subnet_calculator.py” 

Follow the prompts:
    * Enter a network IP address in CIDR notation (e.g., 192.168.1.0/24).
    * Enter the number of hosts to subnet the IP address for.
The program will calculate and display the subnets, their subnet masks, and default gateways.

Example

Input:

Welcome to the IP Calculator!
Enter a network IP address with CIDR notation (e.g. 192.168.1.0/24): 192.168.1.0/24
Enter the number of hosts to subnet the IP address for: 62

Output:

Subnetting Results...:

Subnet 1: 192.168.1.0/26
 Subnet Mask: 255.255.255.192
 Default Gateway: 192.168.1.1

Subnet 2: 192.168.1.64/26
 Subnet Mask: 255.255.255.192
 Default Gateway: 192.168.1.65

Subnet 3: 192.168.1.128/26
 Subnet Mask: 255.255.255.192
 Default Gateway: 192.168.1.129

And so on…


Notes
* Ensure the IP address and CIDR notation you provide are valid.
* The program calculates subnets assuming the largest block of usable IP addresses for the specified number of hosts.
* For optimal results, use realistic values for the number of hosts required.

Troubleshooting
If you encounter an error:
* Ensure that the network IP address is in valid CIDR notation (e.g., 192.168.0.0/24).
* Ensure that the number of hosts is a valid integer.

Author:
Ibrahim Barrie
