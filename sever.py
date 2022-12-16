# -*- coding: utf-8 -*-
import os
import hashlib
import requests
import sys
from rich.console import Console
console = Console()
output = os.popen('hostname').read()
output = output[:-1]
if output == 'localhost':
    output = os.popen('whoami')
    output = str(output)[:-1]
    output = hashlib.md5(output.encode('utf-8')).hexdigest()
output = output.upper()

order_id = '196629'
response = requests.get(f'https://tool.yenpro.net/check/key.php?'
                        f'code={output}&order_id={order_id}').json()
if response['code'] == 0:
    console.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. '
                  'Thiết Bị Của Bạn Chưa Được Kích Hoạt')
    console.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào '
                  'https://tool.yenpro.net/ Để Được Kích Hoạt')
    console.print(f'\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {output} '
                  f'(Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)')
    sys.exit()
elif response['code'] == 1:
    console.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. '
                  'Thiết Bị Của Bạn Đã Được Kích Hoạt')
else:
    console.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. '
                  'Thiết Bị Của Bạn Đã Hết Hạng Sử Dụng')
    console.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào '
                  'https://tool.yenpro.net/ Để Gia Hạn Thiết Bị')
    console.print(f'\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {output} '
                  f'(Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)')
    sys.exit()
