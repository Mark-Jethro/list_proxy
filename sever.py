import os ,hashlib as D ,requests as E ,sys #line:1
from rich .console import Console as A #line:2
B =A ()#line:3
def C ():#line:4
	OOOO0000O0OOOOO0O ='code';OO0000OO00OO0O000 =os .popen ('hostname').read ();OO0000OO00OO0O000 =str (OO0000OO00OO0O000 )[:-1 ]#line:5
	if OO0000OO00OO0O000 =='localhost':OO0000OO00OO0O000 =os .popen ('whoami').read ();OO0000OO00OO0O000 =OO0000OO00OO0O000 [:-1 ]#line:6
	OO0000OO00OO0O000 =D .md5 (OO0000OO00OO0O000 .encode ('utf-8')).hexdigest ();OO0000OO00OO0O000 =OO0000OO00OO0O000 .upper ();O000OOOOOOOO00OO0 ='196629';OO00O0000O0000000 =E .get (f"https://tool.yenpro.net/check/key.php?code={OO0000OO00OO0O000}&order_id={O000OOOOOOOO00OO0}").json ()#line:7
	if OO00O0000O0000000 [OOOO0000O0OOOOO0O ]==0 :B .print ('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Chưa Được Kích Hoạt');B .print ('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Được Kích Hoạt');B .print (f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {OO0000OO00OO0O000} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys .exit ()#line:8
	elif OO00O0000O0000000 [OOOO0000O0OOOOO0O ]==1 :0 #line:9
	else :B .print ('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Hệ Thống Thông Báo. Thiết Bị Của Bạn Đã Hết Hạng Sử Dụng');B .print ('\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]Vui Lòng Truy Cập Vào https://tool.yenpro.net/ Để Gia Hạn Thiết Bị');B .print (f"\n[bold][bold yellow][[bold red]![bold yellow]] [bold dim cyan]CODE Thiết Bị: {OO0000OO00OO0O000} (Vui Lòng Không Chia Sẻ CODE Cho Bất Cứ Ai)");sys .exit ()#line:10
if __name__ =='__main__':C ()
