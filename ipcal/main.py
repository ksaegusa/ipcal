from . import util
import click

@click.command()
@click.option('--ip',default='', type=str, help='ipaddress')
def main(ip):
  ipnetwork = util.input_value_cast_to_ipv4network(ip)
  util.ipnetwork_information(ipnetwork)

if __name__ == '__main__':
  main()