import nmap
import json

def scan_now(target):
   #print(dir(nmap))
    nScan = nmap.PortScanner()
    

    nScan.scan(target, '23,445,3389')
    tcpList = []
    for host in nScan.all_hosts():
        print('Host : %s (%s)' % (host, nScan[host].hostname()))
        print('State : %s' % nScan[host].state())
        s1 = nScan[host].state()
        
        for proto in nScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nScan[host][proto].keys()
            #lport.sort()
            for port in lport:
                p1 = port
                s1 =  nScan[host][proto][port]['state']
                tcpList.append([p1, s1])
                print ('port : %s\tstate : %s' % (port, nScan[host][proto][port]['state']))
            
    final_list = [target,[tcpList]]
    return final_list
    #print(final_list)
    


    # json_string = json.dumps(final_list)  
    # print(json_string)
    # with open("sample.json", "a") as outfile:
    #     json.dump(json_string, outfile, indent=4)
    # print("-- done ---")