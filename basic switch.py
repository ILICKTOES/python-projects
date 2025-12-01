'''
Jacob Genereaux

FOLID:j_genereaux
Student#:1298774
CTN - computer techinician script
'''
from pathlib import Path
import os

def menu():
    print("-----------------------\n")
    print("1."+"Set clock\n")
    print("2."+"Hostname & EXEC password\n")
    print("3."+"Console line config")
    print("4."+"VTY line config\n")
    print("5."+"Create vlans\n")
    print("6."+"Assign ports to vlans\n")
    print("7."+"Add ip to vlans\n")
    print("8."+"Default gateway\n")
    print("9."+"Manual trunking\n")
    print("10."+"Etherchannel & Trunking\n")
    print("11."+"STP & PVST config\n")
    print("12."+"Port security & Violation")
    print()
    print("14."+"Save config\n")
    print("15."+"Show po\n")
    print("16."+"Exit\n")
    print("-----------------------")
    return

def clock():
    hr = input('clock hour: ')
    mn = input('clock minutes: ')
    dy = input('clock day #: ')
    mon = input('clock month: ').capitalize()
    yr = input('clock year: ')
    print(f'Setting clock to {hr}:{mn}:00 {dy} {mon} {yr}\n')
    wait = "waitln 'switch>'"
    
    clock_complete = f"sendln 'do clock set {hr}:{mn}:00 {dy} {mon} {yr}'"  
    with open('tempstart.ttl', 'at') as tempclock:
        tempclock.write(f'{wait}\n')
        tempclock.write(f'{clock_complete}\n')
        tempclock.write(f'{wait}\n')
        return

def s_cisco():
    wait = "waitln 'switch>'"
    hostname = input('hostname: ')
    password = input('enable secret password: ')
    hostname_command = f"sendln 'hostname {hostname}'"
    login = "sendln 'login'"
    passw_secret = f"sendln 'enable secret {password}'"
    with open('tempstart.ttl', 'at') as temphostname_secret_password:
        temphostname_secret_password.write(f'{wait}\n')
        temphostname_secret_password.write(f'{hostname_command}\n')
        temphostname_secret_password.write(f'{wait}\n')
        temphostname_secret_password.write(f'{passw_secret}\n')
        temphostname_secret_password.write(f'{wait}\n')
        temphostname_secret_password.write(f'{login}\n')
        temphostname_secret_password.write(f'{wait}\n')
        return hostname

def line_con():
    password = input('console line password: ')
    line_con = "sendln 'line console 0'"
    login = "sendln 'login'"
    logging_sync = "sendln 'logging synchronous'"
    passw_c = f"sendln 'password {password}'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvty_password:
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{line_con}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{passw_c}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{login}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{logging_sync}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{end}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{configt}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.flush()
        return

def vty_line():            
    password = input('vty lines password: ')
    line_vty = "sendln 'line vty 0 31'"
    login = "sendln 'login'"
    logging_sync = "sendln 'logging synchronous'"
    passw_v = f"sendln 'password {password}'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvty_password:
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{line_vty}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{passw_v}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{login}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{logging_sync}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{end}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.write(f'{configt}\n')
        tempvty_password.write(f'{wait}\n')
        tempvty_password.flush()
        return

def a_vlans():
    vname = input('vlan name ex. vlan 10: ')
    ports = input('enter range or port to assign vlan: ')
    port_ports = f"sendln 'interface range {ports}'"
    access = "sendln 'switchport mode access'"
    assign = f"sendln 'switchport access {vname}'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempassign_ports_vlan:
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.write(f'{port_ports}\n')
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.write(f'{access}\n')
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.write(f'{assign}\n')
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.write(f'{end}\n')
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.write(f'{configt}\n')
        tempassign_ports_vlan.write(f'{wait}\n')
        tempassign_ports_vlan.flush()
        return ports

def c_vlans():
    cvlans = True
    while cvlans == True:
        wait = "waitln 'switch>'"
        configt = "sendln 'configure terminal'"
        end = "sendln 'end'"
        vlancr = input('do you want to create vlan? Y/N: ')
        if vlancr == 'Y' or vlancr == 'y':
            vname = input('name for vlan ex. guests: ')
            vnum = input('vlan number: ')
            vlan_create = f"sendln 'vlan {vnum}'"
            vlan_name = f"sendln 'name {vname}'"
            with open('tempstart.ttl', 'at') as tempcreate_vlan:
                tempcreate_vlan.write(f'{wait}\n')
                tempcreate_vlan.write(f'{vlan_create}\n')
                tempcreate_vlan.write(f'{wait}\n')
                tempcreate_vlan.write(f'{vlan_name}\n')
                tempcreate_vlan.write(f'{wait}\n')
                tempcreate_vlan.write(f'{end}\n')
                tempcreate_vlan.write(f'{wait}\n')
                tempcreate_vlan.write(f'{configt}\n')
                tempcreate_vlan.write(f'{wait}\n')
                tempcreate_vlan.flush()
                continue
            
        elif vlancr == 'N' or vlancr == 'n':
            cvlans = False
            return
        
        else:
            continue
    

def ip_gateway():
    ip_add = input('ip default-gateway: ')
    default_gateway = f"sendln 'ip default-gateway {ip_add}'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempdefault_gateway:
        tempdefault_gateway.write(f'{wait}\n')
        tempdefault_gateway.write(f'{default_gateway}\n')
        tempdefault_gateway.write(f'{wait}\n')
        tempdefault_gateway.write(f'{end}\n')
        tempdefault_gateway.write(f'{wait}\n')
        tempdefault_gateway.write(f'{configt}\n')
        tempdefault_gateway.write(f'{wait}\n')
        tempdefault_gateway.flush()
        return

def vlan_ip():
    vname = input('vlan name ex. vlan 10: ')
    ip_add = input('ip address: ')
    sub_net = input('subnet address: ')
    interface_vlan = f"sendln 'int vlan {vname}'"
    assign_ip = f"sendln 'ip address {ip_add} {sub_net}'"
    no_shutdown = "sendln 'no shutdown'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvlan_ip:
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.write(f'{interface_vlan}\n')
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.write(f'{assign_ip}\n')
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.write(f'{no_shutdown}\n')
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.write(f'{end}\n')
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.write(f'{configt}\n')
        tempvlan_ip.write(f'{wait}\n')
        tempvlan_ip.flush()
        return

def trunking_m():
    wait = "waitln 'switch>'"
    allowedp = input('allowed vlans seperate with comma do not MISSTYPE!!!: ') 
    native = input('native vlan: ')
    ports = input('enter range or port to trunk: ')
    port_ports = f"sendln 'int range {ports}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    trunk = f"sendln 'switchport mode trunk'"
    nonegociate = f"sendln 'switchport nonegociate'"
    trunk_native = f"sendln 'switchport trunk native vlan {native}'"              
    trunk_allowed = f"sendln 'switchport trunk allowed vlan {allowedp},{native}'"
    with open('tempstart.ttl', 'at') as tempmanual_trunking:
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{port_ports}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{trunk}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{nonegociate}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{trunk_native}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{trunk_allowed}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{end}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.write(f'{configt}\n')
        tempmanual_trunking.write(f'{wait}\n')
        tempmanual_trunking.flush()
        return ports

def etherchannel():
    active_LACP = "active=LACP unconditionally\n"
    auto_PAgP = "auto=PAgP if another PAgP device is connected\n"
    desireable_PAgP = "desireable=PAgP unconditionally\n"
    on_enable = "on, or enable=Etherchannel only\n"
    passive_LACP = "passive=LACP if another LACP device is connected\n"
    exit_ = "sendln 'exit'"
    wait = "waitln 'switch>'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    mode = input(f'{active_LACP}{auto_PAgP}{desireable_PAgP}{on_enable}{passive_LACP}enter etherchannel mode: ')
    native = input('native vlan: ')
    allowedp = input('allowed vlans seperate with comma do not MISSTYPE!!!: ')
    ports = input('enter range or port to etherchannel: ')
    channel = input('channel group & port-channel number: ')
    ports_range = f"sendln 'int range {ports}'"
    channel_group = f"sendln 'channel-group {channel} mode {mode}'"
    port_channel = f"sendln 'int port-channel {channel}'"
    trunk = f"sendln 'switchport mode trunk'"
    trunk_native = f"sendln 'switchport trunk native vlan {native}'"              
    trunk_allowed = f"sendln 'switchport trunk allowed vlan {allowedp},{native}'"
    nonegociate = f"sendln 'switchport nonegociate'"
    with open('tempstart.ttl', 'at') as tempetherchannel:
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{ports_range}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{channel_group}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{exit_}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{port_channel}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{trunk}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{nonegociate}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{trunk_native}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{trunk_allowed}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{end}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.write(f'{configt}\n')
        tempetherchannel.write(f'{wait}\n')
        tempetherchannel.flush()
        return ports              

def port_sec():
    security = True
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    wait = "waitln 'switch>'"
    security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')    
    while security == True:
        if security_mode == 'manual' or security_mode == 'Manual':
            ports = input('enter range or port for manual assignment of mac: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            mac_address = input('enter mac address to manually assign: ')
            port_ports = f"sendln 'int range {ports}'"
            access = "sendln 'switchport mode access'"
            enable_port_security = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            manual = f"sendln 'switchport port-security mac-address {mac_address}'"
            with open('tempstart.ttl', 'at') as tempmanual:
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{port_ports}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{access}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{enable_port_security}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{mac_address_limit}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{manual}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{end}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.write(f'{configt}\n')
                tempmanual.write(f'{wait}\n')
                tempmanual.flush()
                security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                continue       

        elif security_mode == 'sticky' or security_mode == 'Sticky':
            ports = input('enter range or port for sticky aging: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            port_ports = f"sendln 'int range {ports}'"
            access = "sendln 'switchport mode access'"
            enable_port_security = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            sticky = "sendln 'switchport port-security mac-address sticky'"
            with open('tempstart.ttl', 'at') as tempsticky:
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{port_ports}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{access}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{enable_port_security}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{mac_address_limit}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{sticky}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{end}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.write(f'{configt}\n')
                tempsticky.write(f'{wait}\n')
                tempsticky.flush()
                security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                continue

        elif security_mode == 'dynamic' or security_mode == 'Dynamic':
            ports = input('enter range or port for dynamic aging: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            port_ports = f"sendln 'int range {ports}'"
            access = "sendln 'switchport mode access'"
            dynamic = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            with open('tempstart.ttl', 'at') as tempdynamic:
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{port_ports}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{access}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{dynamic}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{mac_address_limit}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{end}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.write(f'{configt}\n')
                tempdynamic.write(f'{wait}\n')
                tempdynamic.flush()
                security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                continue

        elif security_mode == 'shutdown' or security_mode == 'Shutdown':
            ports = input('enter range or port for shutdown: ')
            port_ports = f"sendln 'int range {ports}'"
            shutdown = "sendln 'shutdown'"
            with open('tempstart.ttl', 'at') as tempshutdown:
                tempshutdown.write(f'{wait}\n')
                tempshutdown.write(f'{port_ports}\n')
                tempshutdown.write(f'{wait}\n')
                tempshutdown.write(f'{shutdown}\n')
                tempshutdown.write(f'{wait}\n')
                tempshutdown.write(f'{end}\n')
                tempshutdown.write(f'{wait}\n')
                tempshutdown.write(f'{configt}\n')
                tempshutdown.write(f'{wait}\n')
                tempshutdown.flush()
                security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                continue  

        elif security_mode == 'violation.aging' or security_mode == 'Violation.Aging':
            ports = input('enter range or port for violation & aging: ')
            aging_mode = input('enter aging mode static or time: ')
            port_ports = f"sendln 'int range {ports}'"
            if aging_mode == 'time' or aging_mode == 'Time':
                time_in_minutes = input('enter time in minutes: ')
                port_aging = f"sendln 'switchport port-security aging time {time_in_minutes}'"
                with open('tempstart.ttl', 'at') as temptime:
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{port_ports}\n')
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{port_aging}\n')
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{end}\n')
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{configt}\n')
                    temptime.write(f'{wait}\n')
                    temptime.flush()
                    violation_mode = input('enter violation mode > protect,restrict,shutdown: ')
                    port_violation = f"sendln 'switchport port-security violation {violation_mode}'"
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{port_violation}\n')
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{end}\n')
                    temptime.write(f'{wait}\n')
                    temptime.write(f'{configt}\n')
                    temptime.write(f'{wait}\n')
                    temptime.flush()
                    security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                    continue
        
            elif aging_mode == 'static' or aging_mode == 'Static':
                ports = input('enter range or port for static aging: ')
                port_ports = f"sendln 'int range {ports}'"
                port_aging = "sendln 'switchport port-security aging static'"
                with open('tempstart.ttl', 'at') as tempstatic:
                    tempstatic.write(f'{wait}\n')
                    tempstatic.write(f'{port_ports}\n')
                    tempstatic.write(f'{wait}\n')
                    tempstatic.write(f'{port_aging}\n')
                    tempstatic.write(f'{wait}\n')
                    tempstatic.flush()
                    violation_mode = input('enter violation mode > protect,restrict,shutdown: ')
                    port_violation = f"sendln 'switchport port-security violation {violation_mode}'"
                    tempstatic.write(f'{wait}\n')
                    tempstatic.write(f'{port_violation}\n')
                    tempstatic.write(f'{wait}\n')
                    tempstatic.write(f'{end}\n')
                    tempstatic.write(f'{wait}\n')
                    tempstatic.write(f'{configt}\n')
                    tempstatic.write(f'{wait}\n')
                    tempstatic.flush()
                    security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
                    continue

        elif security_mode == 'EXIT' or security_mode == 'exit':
            security = False
            return

        else:
            security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
            continue
                

def mitigate_dhcp_attacks_and_arp():
    wait = "waitln 'switch>'"
    enable_snooping = "sendln 'ip dhcp snooping'"
    ports_router = input('enter port for router/dhcp server: ')
    ports_trusted = input('enter trusted ports for dhcp snooping: ')
    limit = input('enter snooping rate #: ')
    vlans = input('enter vlans for snooping seperated: ')
    snooping_switch = f"sendln 'int range {ports_trusted}'"
    snooping_router = f"sendln 'int range {ports_router}'"
    snooping_vlans = f"sendln 'ip dhcp snooping vlan {vlans}'"
    router_trust = "sendln 'ip dhcp snooping trust'"
    snooping_limit = f"sendln 'ip dhcp snooping limit rate {limit}'"
    exit_ = "sendln 'exit'" 
    with open('tempstart.ttl', 'at') as tempdhcp_snooping:
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{enable_snooping}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{snooping_router}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{router_trust}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{exit_}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{snooping_switch}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{snooping_limit}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{exit_}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.write(f'{snooping_vlans}\n')
        tempdhcp_snooping.write(f'{wait}\n')
        tempdhcp_snooping.flush()
        arp_inspection = input('do you want to enable arp inspection Y/N: ')
        while arp_inspection:
            if arp_inspection == 'Y' or arp_inspection == 'y':
                enable_arp = "sendln 'ip arp inspection vlan {vlans}'"
                with open('tempstart.ttl', 'at') as temparp_inspection:
                    temparp_inspection.write(f'{wait}\n')
                    temparp_inspection.write(f'{enable_arp}\n')
                    temparp_inspection.write(f'{wait}\n')
                    temparp_inspection.flush()
                    return
            
            elif arp_inspection == 'N' or arp_inspection == 'n':
                return
            
            else:
                arp_inspection = input('do you want to enable arp inspection Y/N: ')
                continue
                
def stp_():    
    ports = input('enter range or port for spanning tree: ')
    mode = input('enter rapid-pvst, pvst or stp: ')
    wait = "waitln 'switch>'"
    port_mode = f"sendln 'spanning-tree mode {mode}'"
    port_ports = f"sendln 'int range {ports}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    portfast = "sendln 'spanning-tree portfast'"
    bpduguard = "sendln 'spanning-tree bpduguard enable'"
    with open('tempstart.ttl', 'at') as tempstp:
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{port_mode}\n')
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{port_ports}\n')
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{portfast}\n')
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{bpduguard}\n')
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{end}\n')
        tempstp.write(f'{wait}\n')
        tempstp.write(f'{configt}\n')
        tempstp.write(f'{wait}\n')
        tempstp.flush()
        return ports

def start_():
    connect = "connect '/C=3'"
    setsync = "setsync 1"
    waite = "waitln 'switch#'"
    wait = "waitln 'switch>'"
    enable = "sendln 'enable'"
    configt = "sendln 'configure terminal'"
    configp = f"waitln '{hostname}(config)#"
    with open('tempstart.ttl', 'w+') as tempstart:
        tempstart.write(f'{setsync}\n')
        tempstart.write(f'{wait}\n')
        tempstart.write(f'{connect}\n')
        tempstart.write(f'{enable}\n')
        tempstart.write(f'{waite}\n')
        tempstart.write(f'{configt}\n')
        tempstart.write(f'{configp}\n')
        tempstart.write(f'{wait}\n')
        tempstart.flush()
        return

def finish_(hostname):
    name_of_file = input('enter name for log file without .log: ')
    Desktop = Path.home() / "Desktop"
    log_file = Desktop / f"{name_of_file}.log"
    start_logging = f"logopen '{str(log_file)}'"
    stop_logging = "logclose"
    carriage_return = "sendln ''"
    configp = f"waitln '{hostname}(config)#"
    save = "sendln 'do copy running-config startup-config'"
    save_prompt = "waitln 'Destination filename [startup-config]?'"
    show = "sendln 'do show start'"
    terminal_length = "sendln 'do terminal length 0'"
    with open('tempfinish.ttl', 'w+') as tempfinish:
        tempfinish.write(f'{configp}\n')
        tempfinish.write(f'{terminal_length}\n')
        tempfinish.write(f'{configp}\n')
        tempfinish.write(f'{save}\n')
        tempfinish.write(f'{save_prompt}\n')
        tempfinish.write(f'{carriage_return}\n')
        tempfinish.write(f'{configp}\n')
        tempfinish.write(f'{start_logging}\n')
        tempfinish.write(f'{show}\n')
        tempfinish.write(f'{configp}\n')
        tempfinish.write(f'{stop_logging}\n')
        tempfinish.write(f'{configp}\n')
        tempfinish.flush()
        return
        

def delete_save(hostname):
    starting_prompt = f"waitln 'Press RETURN to get started!'"
    waite = f"waitln '{hostname}#'"
    wait = f"waitln '{hostname}>'"
    waitp = "waitln 'Password:'"
    password_con = input('enter console password: ')
    password_en = input('enter EXEC password: ')
    passw_c = f"sendln '{password_con}'"
    passw_e = f"sendln '{password_en}'"
    connect = "connect '/C=3'"
    setsync = "setsync 1"
    carriage_return = "sendln ''"
    delete_startup = "sendln 'do erase startup-config'"
    delet_startup_prompt = "waitln 'Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]'"
    delete_vlan_dat = "sendln 'do delete flash:/vlan.dat'"
    enable = "sendln 'enable'"
    configt = "sendln 'configure terminal'"
    configp = f"waitln '{hostname}(config)#"
    vlan_dat_delete_prompt = "waitln 'Delete filename [vlan.dat]?'"
    vlan_dat_delete_prompt_confirm = "waitln '[confirm]'"
    reload_ = "sendln 'do reload in 0'"
    reload_prompt = "waitln 'Proceed with reload? [confirm]'"
    reload_confirm = "waitln 'Would you like to save the current configuration? [yes/no]:'"
    reload_confirm_no = "sendln 'no'"
    with open('tempdelete.ttl', 'w+') as tempdelete:
        tempdelete.write(f'{setsync}\n')
        tempdelete.write(f'{connect}\n')
        tempdelete.write(f'{starting_prompt}\n')
        tempdelete.write(f'{carriage_return}\n')
        tempdelete.write(f'{waitp}\n')
        tempdelete.write(f'{passw_c}\n')
        tempdelete.write(f'{wait}\n')
        tempdelete.write(f'{enable}\n')
        tempdelete.write(f'{waitp}\n')
        tempdelete.write(f'{passw_e}\n')
        tempdelete.write(f'{waite}\n')
        tempdelete.write(f'{configt}\n')
        tempdelete.write(f'{configp}\n')
        tempdelete.write(f'{delete_startup}\n')
        tempdelete.write(f'{delet_startup_prompt}\n')      
        tempdelete.write(f'{carriage_return}\n')
        tempdelete.write(f'{configp}\n')
        tempdelete.write(f'{delete_vlan_dat}\n')
        tempdelete.write(f'{vlan_dat_delete_prompt}\n')
        tempdelete.write(f'{carriage_return}\n')
        tempdelete.write(f'{vlan_dat_delete_prompt_confirm}\n')
        tempdelete.write(f'{carriage_return}\n')        
        tempdelete.write(f'{configp}\n')
        tempdelete.write(f'{reload_}\n')
        tempdelete.write(f'{reload_prompt}\n')
        tempdelete.write(f'{carriage_return}\n')
        tempdelete.write(f'{reload_confirm}\n')
        tempdelete.write(f'{reload_confirm_no}\n')
        tempdelete.flush()
        return 
    

def ParkingLot_Blackhole(port_result1, port_result2, port_result3, hostname):
    print(f'vlan ports: {port_result1}')
    print(f'etherchannel & trunking ports: {port_result2}')
    print(f'stp enabled ports: {port_result3}')
    blackhole = input('please enter Parking or Blackhole vlan: ')
    park_ports = input('enter ports for Parking_Lot: ')
    port_ports = f"sendln 'int range {park_ports}'"
    access = "sendln 'switchport mode access'"
    access_vlan = f"sendln 'switchport access {blackhole}'"
    end = "sendln 'end'"
    waiti = f"send '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    configp = f"waitln '{hostname}(config)#"
    configt = "sendln 'configure terminal'"
    with open('tempstart.ttl', 'at') as tempBlackhole_ParkingLot:
        tempBlackhole_ParkingLot.write(f'{configp}\n')
        tempBlackhole_ParkingLot.write(f'{port_ports}\n')
        tempBlackhole_ParkingLot.write(f'{waiti}\n')
        tempBlackhole_ParkingLot.write(f'{access}\n')
        tempBlackhole_ParkingLot.write(f'{waiti}\n')
        tempBlackhole_ParkingLot.write(f'{access_vlan}\n')
        tempBlackhole_ParkingLot.write(f'{waiti}\n')
        tempBlackhole_ParkingLot.write(f'{end}\n')
        tempBlackhole_ParkingLot.write(f'{waite}\n')
        tempBlackhole_ParkingLot.write(f'{configt}\n')
        tempBlackhole_ParkingLot.write(f'{configp}\n')
        tempBlackhole_ParkingLot.flush()
        return park_ports




menu_input = input("Please enter a number or EXIT: ")
'''
while loop, checking value of 'menu_Input' if value is not '0' then continue the loop
each 'elif' is checking for specific input value to call respective functions
includes an exit and "mysterious values" or "unknown" check at the bottom of the loop 
'''

while menu_input != '0':
    start_()
    hostname = 'Switch'
    port_result1 = 'none'
    port_result2 = 'none'
    port_result3 = 'none'
    Blackhole_ports = 'none'
        
    if menu_input == '1':
        clock()
        menu()
        menu_input = input("Please enter a number or EXIT: ") 

    elif menu_input == '2':
        hostname = s_cisco()
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '3':
        line_con()
        menu()
        menu_input = input("Please enter a number or EXIT: ")
        

    elif menu_input == '4':
        vty_line()
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '5':
        c_vlans()   
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '6':
        port_result1 = a_vlans()
        menu()
        
        menu_input = input("Please enter a number or EXIT: ")
        
    elif menu_input == '7':
        vlan_ip()
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '8':
        ip_gateway()
        menu()
        menu_input = input("Please enter a number or EXIT: ")
        
    elif menu_input == '9':
        port_result2 = trunking_m()
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '10':
        port_result2 = etherchannel()
        menu()
        menu_input = input("Please enter a number or EXIT: ")
    
    elif menu_input == '11':
        port_result3 = stp_()
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '12':
        Blackhole_ports = ParkingLot_Blackhole(f'{port_result1}', 
        f'{port_result2}', f'{port_result3}',f'{hostname}')
        menu()
        menu_input = input("Please enter a number or EXIT: ")
        
    elif menu_input == '13':
        port_sec()
        menu()
        menu_input = input("Please enter a number or EXIT: ")
        
    elif menu_input == '14':
        mitigate_dhcp_attacks_and_arp()
        menu()
        menu_input = input("Please enter a number or EXIT: ")
    
    elif menu_input == '15':
        print(f'vlan ports: {port_result1}')
        print(f'etherchannel & trunking ports: {port_result2}')
        print(f'stp enabled ports: {port_result3}')
        print(f'Parking_Lot or Blackhole ports: {Blackhole_ports}')
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    elif menu_input == '16':
        finish_(f'{hostname}')
        os.remove('tempstart.ttl')
        menu()
        menu_input = input("Please enter a number or EXIT: ")
        
    elif menu_input == '17':
        delete_save(f'{hostname}')
        os.remove('tempfinish.ttl')
        menu()
        menu_input = input("Please enter a number or EXIT: ")

    
    elif menu_input == 'EXIT' or menu_input == 'exit':
         print("Goodbye!!!?")
         os.remove('tempdelete.ttl')
         break

    else:
        print('invalid input!!!')
        menu()
        menu_input = input("Please enter a number or EXIT: ")


def menu():
    print("-----------------------\n")
    print("1."+"Set clock\n")
    print("2."+"Hostname & EXEC password\n")
    print("3."+"Console line config")
    print("4."+"VTY line config\n")
    print("5."+"Create vlans\n")
    print("6."+"Assign ports to vlans\n")
    print("7."+"Add ip to vlans\n")
    print("8."+"Default gateway\n")
    print("9."+"Manual trunking\n")
    print("10."+"Etherchannel & Trunking\n")
    print("11."+"STP & PVST config\n")
    print(d
    print("13."+"port security & Violation\n")
    print("14."+"dhcp snooping & arp inspection\n")
    print("15."+"show configured ports\n")
    print("16."+"finish & save config\n")
    print("17."+"delete startup-config & reload\n")
    print("Type EXIT to quit\n")
    print("-----------------------")
    return
                        
'''
switch config script generator
by: @ILICKTOES 
version: 1.2
This script generates a .ttl file to be used with Tera Term to automate the configuration of Cisco switches.
Usage: Run the script and follow the prompts to input configuration details. Select the desired configuration options from the menu.
The script will create a temporary .ttl file with the specified configurations.

'''
