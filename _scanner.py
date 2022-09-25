import nmap
import json

def scan_now(target):
   #print(dir(nmap))
    nScan = nmap.PortScanner()
    

    nScan.scan(target, '23,445,3389')
    #nScan.scan(target, '22,25,80,111,443,3389')
    tcpList = []
    tcpDict = {}
    for host in nScan.all_hosts():
        #print('Host : %s (%s)' % (host, nScan[host].hostname()))
        #print('State : %s' % nScan[host].state())
        s1 = nScan[host].state()
        
        for proto in nScan[host].all_protocols():
            print('----------')
            #print('Protocol : %s' % proto)
            lport = nScan[host][proto].keys()
            #lport.sort()
            for port in lport:
                p1 = port
                s1 =  nScan[host][proto][port]['state']
                tcpList.append([p1, s1])
                #print ('port : %s\tstate : %s' % (port, nScan[host][proto][port]['state']))
            
    #final_list = [target,[tcpList]]
    tcpDict.update({'host':target})
    tcpDict.update({'tcp':tcpList})
    return tcpDict
    #return final_list
    #print(final_list)
    

    ## To export the data in Json
    # json_string = json.dumps(final_list)  
    # print(json_string)
    # with open("sample.json", "a") as outfile:
    #     json.dump(json_string, outfile, indent=4)
    # print("-- done ---")