import ipaddress
import math

def calculate_subnets(network_ip, num_hosts):
  try:
    network = ipaddress.ip_network(network_ip, strict=False)
    needed_subnets = math.ceil(math.log2(num_hosts + 2))
    new_prefix = 32 - needed_subnets
    
    subnets = list(network.subnets(new_prefix=new_prefix))
    print("\nSubnetting Results...:\n")
    for i, subnet in enumerate(subnets):
      gatewaye = list(subnet.hosts())[0]
      print(f"subnet {i + 1}: {subnet}")
      print(f" Subnet Mask: {subnet.netmask}")
      print(f" Default Gateway: {gatewaye}")
      print()
      
  except ValueError as e:
    print(f"Error: {e}")
    
def main():
  print("Welcome to the IP Calculator!")
  network_ip = input("Enter a network IP address with CIDR notation (e.g. 192.168.1.0/24: ").strip()
  try:
    num_hosts = int(input("Enter the number of hosts to subnet the IP address for: ").strip())
    calculate_subnets(network_ip, num_hosts)
  except ValueError:
    print("Invalid input. Please enter a number of hosts.")
    
if __name__ == "__main__":
  main()