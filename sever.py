H='code'
import os,hashlib as D,requests as E,sys
from rich.console import Console as F
B=F()
A=os.popen('hostname').read()
A=A[:-1]
if A=='localhost':A=os.popen('whoami');A=A[:-1]
A=D.md5(A.encode('utf-8')).hexdigest()
A=A.upper()
G='196629'
C=E.get(f"https://tool.yenpro.net/check/key.php?code={A}&order_id={G}").json()
if C[H]==0:B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Chưa Được Kích Hoạt');B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Được Kích Hoạt');B.print(f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {A} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys.exit()
elif C[H]==1:B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Đã Được Kích Hoạt')
else:B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Đã Hết Hạng Sử Dụng');B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Gia Hạn Thiết Bị');B.print(f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {A} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys.exit()