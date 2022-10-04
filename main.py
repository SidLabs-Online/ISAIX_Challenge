import _scanner as sn
import time
begin = time.time()
from colorama import Fore, Back, Style, init
init()
ports = [23,445,3389]
the_target = input("Enter Target IP :")

test = sn.scan_now(the_target, ports)

end = time.time()
print(Fore.BLUE + "\nScan completed in " + f"{round(((end - begin)%60), 2)}"+ " secs"+Style.RESET_ALL)


print(test)

# print("\nVulnerability Threat Level\n")
# if test[1][0][1][1] == "open":
#     print("\t"+Back.RED + " high "+Style.RESET_ALL+Fore.RED ,f"RDP Server Detected overTCP."+ Style.RESET_ALL)
# elif test[1][0][0][1] == "open":
#     print("\t"+Back.MAGENTA + " critical "+Style.RESET_ALL+Fore.RED ,f"FTP Service Detected."+ Style.RESET_ALL)
# elif test[1][0][2][1] == "open":
#     print("\t"+Back.YELLOW + " medium "+Style.RESET_ALL+Fore.RED ,f"SMB Ports are Open Over TCP."+ Style.RESET_ALL)
# else:
#     print("\t\tNone\n")


