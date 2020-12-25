import ipaddress
import sys

def input_value_cast_to_ipv4network(input_ip):
  '''
  入力値をipaddressオブジェクトにキャストして戻す
  '''
  if input_ip:
    try:
      ipnetwork = ipaddress.ip_network(input_ip,strict=False)
      return ipnetwork
    except ValueError:
      print(f"Error: Value Error")
      sys.exit(1)
    except Exception as e:
      print(f"Error: {e}")
      sys.exit(1)
  else:
    value = input('IPアドレス入力[X.X.X.X/X]>> ')
    try:
      ipnetwork = ipaddress.ip_network(value,strict=False)
      return ipnetwork
    except ValueError:
      print(f"Error: Value Error")
      sys.exit(1)
    except Exception as e:
      print(f"Error: {e}")
      sys.exit(1)

def ipnetwork_information(ipnetwork):
  print(f'Prefix          : {ipnetwork.with_prefixlen}')
  print(f'SubnetMask      : {ipnetwork.netmask}')
  print(f'WildCardMask    : {ipnetwork.with_hostmask}')
  print(f'NetworkAddress  : {ipnetwork.network_address}')
  print(f'BroadCastAddress: {ipnetwork.broadcast_address}')