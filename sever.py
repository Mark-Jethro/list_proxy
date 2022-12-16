import os,hashlib as D,requests as E,sys
from rich.console import Console as A
B=A()
def C():
	H='code';A=os.popen('hostname').read();A=str(A)[:-1]
	if A=='localhost':A=os.popen('whoami').read();A=A[:-1]
	A=D.md5(A.encode('utf-8')).hexdigest();A=A.upper();F='196629';C=E.get(f"https://tool.yenpro.net/check/key.php?code={A}&order_id={F}").json()
	if C[H]==0:B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Chưa Được Kích Hoạt');B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Được Kích Hoạt');B.print(f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {A} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys.exit()
	elif C[H]==1:G='\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Đã Được Kích Hoạt';return G
	else:B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Đã Hết Hạng Sử Dụng');B.print('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Gia Hạn Thiết Bị');B.print(f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {A} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys.exit()
if __name__=='__main__':C()
