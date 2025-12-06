'''
Jacob Genereaux

FOLID:j_genereaux
Student#:1298774
CTN - computer techinician script
'''
from pathlib import Path
import os
def menu():
    print("-Macro-Maker-----------\n")
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
    print("12."+"Parking_Lot & Blackhole vlan\n")
    print("13."+"port security & Violation\n")
    print("14."+"dhcp snooping & arp inspection\n")
    print("15."+"show configured ports\n")
    print("16."+"finish & save config\n")
    print("17."+"delete startup-config & reload\n")
    print("Type EXIT to quit\n")
    print("-----------------------\n")
    selection = input('select option')
    return selection

def clock(hostname):
    hr = input('clock hour: ')
    mn = input('clock minutes: ')
    dy = input('clock day #: ')
    mon = input(('clock month: ').capitalize())
    yr = input('clock year: ')
    print(f'Setting clock to {hr}:{mn}:00 {dy} {mon} {yr}\n')
    configp = f"waitln '{hostname}(config)#'"
    clock_complete = f"sendln 'do clock set {hr}:{mn}:00 {dy} {mon} {yr}'"  
    with open('tempstart.ttl', 'at') as tempclock:
        tempclock.write(f'{configp}\n')
        tempclock.write(f'{clock_complete}\n')
        tempclock.write(f'{configp}\n')
        tempclock.flush()
        tempclock.close()
        return

def line_con(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    waitl = f"waitln '{hostname}(config-line)#'"
    password = input('console line password: ')
    line_con = "sendln 'line console 0'"
    login = "sendln 'login'"
    logging_sync = "sendln 'logging synchronous'"
    passw_c = f"sendln 'password {password}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvty_password:
        tempvty_password.write(f'{configp}\n')
        tempvty_password.write(f'{line_con}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{passw_c}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{login}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{logging_sync}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{end}\n')
        tempvty_password.write(f'{waite}\n')
        tempvty_password.write(f'{configt}\n')
        tempvty_password.write(f'{configp}\n')
        tempvty_password.flush()
        tempvty_password.close()
        return

def vty_line(hostname):            
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    waitl = f"waitln '{hostname}(config-line)#'"
    password = input('vty lines password: ')
    line_vty = "sendln 'line vty 0 31'"
    login = "sendln 'login'"
    logging_sync = "sendln 'logging synchronous'"
    passw_v = f"sendln 'password {password}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvty_password:
        tempvty_password.write(f'{configp}\n')
        tempvty_password.write(f'{line_vty}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{passw_v}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{login}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{logging_sync}\n')
        tempvty_password.write(f'{waitl}\n')
        tempvty_password.write(f'{end}\n')
        tempvty_password.write(f'{waite}\n')
        tempvty_password.write(f'{configt}\n')
        tempvty_password.write(f'{configp}\n')
        tempvty_password.flush()
        tempvty_password.close()
        return

def a_vlans(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    vname = input('vlan name ex. 10: ')
    ports = input('enter range or port to assign vlan: ')
    port_ports = f"sendln 'interface range {ports}'"
    access = "sendln 'switchport mode access'"
    assign = f"sendln 'switchport access vlan {vname}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempassign_ports_vlan:
        tempassign_ports_vlan.write(f'{configp}\n')
        tempassign_ports_vlan.write(f'{port_ports}\n')
        tempassign_ports_vlan.write(f'{waiti}\n')
        tempassign_ports_vlan.write(f'{access}\n')
        tempassign_ports_vlan.write(f'{waiti}\n')
        tempassign_ports_vlan.write(f'{assign}\n')
        tempassign_ports_vlan.write(f'{waiti}\n')
        tempassign_ports_vlan.write(f'{end}\n')
        tempassign_ports_vlan.write(f'{waite}\n')
        tempassign_ports_vlan.write(f'{configt}\n')
        tempassign_ports_vlan.write(f'{configp}\n')
        tempassign_ports_vlan.flush()
        tempassign_ports_vlan.close()
        return ports

def c_vlans(hostname):
    waitv = f"waitln '{hostname}(config-vlan)#'"
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    vname = input('name for vlan ex. guests: ')
    vnum = input('vlan number: ')
    vlan_create = f"sendln 'vlan {vnum}'"
    vlan_name = f"sendln 'name {vname}'"
    with open('tempstart.ttl', 'at') as tempcreate_vlan:
        tempcreate_vlan.write(f'{configp}\n')
        tempcreate_vlan.write(f'{vlan_create}\n')
        tempcreate_vlan.write(f'{waitv}\n')
        tempcreate_vlan.write(f'{vlan_name}\n')
        tempcreate_vlan.write(f'{waitv}\n')
        tempcreate_vlan.write(f'{end}\n')
        tempcreate_vlan.write(f'{waite}\n')
        tempcreate_vlan.write(f'{configt}\n')
        tempcreate_vlan.write(f'{configp}\n')
        tempcreate_vlan.flush()
        tempcreate_vlan.close()
        return

def ip_gateway(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    ip_add = input('ip default-gateway: ')
    default_gateway = f"sendln 'ip default-gateway {ip_add}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempdefault_gateway:
        tempdefault_gateway.write(f'{configp}\n')
        tempdefault_gateway.write(f'{default_gateway}\n')
        tempdefault_gateway.write(f'{configp}\n')
        tempdefault_gateway.write(f'{end}\n')
        tempdefault_gateway.write(f'{waite}\n')
        tempdefault_gateway.write(f'{configt}\n')
        tempdefault_gateway.write(f'{configp}\n')
        tempdefault_gateway.flush()
        tempdefault_gateway.close()
        return

def vlan_ip(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    vname = input('vlan name ex. vlan 10: ')
    ip_add = input('ip address: ')
    sub_net = input('subnet address: ')
    interface_vlan = f"sendln 'int range vlan {vname}'"
    assign_ip = f"sendln 'ip address {ip_add} {sub_net}'"
    no_shutdown = "sendln 'no shutdown'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempvlan_ip:
        tempvlan_ip.write(f'{configp}\n')
        tempvlan_ip.write(f'{interface_vlan}\n')
        tempvlan_ip.write(f'{waiti}\n')
        tempvlan_ip.write(f'{assign_ip}\n')
        tempvlan_ip.write(f'{waiti}\n')
        tempvlan_ip.write(f'{no_shutdown}\n')
        tempvlan_ip.write(f'{waiti}\n')
        tempvlan_ip.write(f'{end}\n')
        tempvlan_ip.write(f'{waite}\n')
        tempvlan_ip.write(f'{configt}\n')
        tempvlan_ip.write(f'{configp}\n')
        tempvlan_ip.flush()
        tempvlan_ip.close()
        return

def trunking_m(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
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
        tempmanual_trunking.write(f'{configp}\n')
        tempmanual_trunking.write(f'{port_ports}\n')
        tempmanual_trunking.write(f'{waiti}\n')
        tempmanual_trunking.write(f'{trunk}\n')
        tempmanual_trunking.write(f'{waiti}\n')
        tempmanual_trunking.write(f'{nonegociate}\n')
        tempmanual_trunking.write(f'{waiti}\n')
        tempmanual_trunking.write(f'{trunk_native}\n')
        tempmanual_trunking.write(f'{waiti}\n')
        tempmanual_trunking.write(f'{trunk_allowed}\n')
        tempmanual_trunking.write(f'{waiti}\n')
        tempmanual_trunking.write(f'{end}\n')
        tempmanual_trunking.write(f'{waite}\n')
        tempmanual_trunking.write(f'{configt}\n')
        tempmanual_trunking.write(f'{configp}\n')
        tempmanual_trunking.flush()
        tempmanual_trunking.close()
        return ports

def etherchannel(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    active_LACP = "active=LACP unconditionally\n"
    auto_PAgP = "auto=PAgP if another PAgP device is connected\n"
    desireable_PAgP = "desireable=PAgP unconditionally\n"
    on_enable = "on, or enable=Etherchannel only\n"
    passive_LACP = "passive=LACP if another LACP device is connected\n"
    exit_ = "sendln 'exit'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    mode = input(f'{active_LACP}{auto_PAgP}{desireable_PAgP}{on_enable}{passive_LACP}enter etherchannel mode: ')
    native = input('native vlan: ')
    allowedp = input('allowed vlans seperate with comma do not MISSTYPE!!!: ')
    ports = input('enter range or port to etherchannel: ')
    channel = input('channel group & port-channel number: ')
    port_ports = f"sendln 'int range {ports}'"
    channel_group = f"sendln 'channel-group {channel} mode {mode}'"
    port_channel = f"sendln 'int port-channel {channel}'"
    trunk = f"sendln 'switchport mode trunk'"
    trunk_native = f"sendln 'switchport trunk native vlan {native}'"              
    trunk_allowed = f"sendln 'switchport trunk allowed vlan {allowedp},{native}'"
    nonegociate = f"sendln 'switchport nonegociate'"
    with open('tempstart.ttl', 'at') as tempetherchannel:
        tempetherchannel.write(f'{configp}\n')
        tempetherchannel.write(f'{port_ports}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{channel_group}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{exit_}\n')
        tempetherchannel.write(f'{configp}\n')
        tempetherchannel.write(f'{port_channel}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{trunk}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{nonegociate}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{trunk_native}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{trunk_allowed}\n')
        tempetherchannel.write(f'{waiti}\n')
        tempetherchannel.write(f'{end}\n')
        tempetherchannel.write(f'{waite}\n')
        tempetherchannel.write(f'{configt}\n')
        tempetherchannel.write(f'{configp}\n')
        tempetherchannel.flush()
        tempetherchannel.close()
        return ports              

def port_sec(hostname):
    security = True
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    wait = f"waitln '{hostname}>'"
    while security == True:
        security_mode = input('enter mode or EXIT > manual, sticky, dynamic or shutdown & violation-aging: ')
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
                tempmanual.write(f'{configp}\n')
                tempmanual.write(f'{port_ports}\n')
                tempmanual.write(f'{waiti}\n')
                tempmanual.write(f'{access}\n')
                tempmanual.write(f'{waiti}\n')
                tempmanual.write(f'{enable_port_security}\n')
                tempmanual.write(f'{waiti}\n')
                tempmanual.write(f'{mac_address_limit}\n')
                tempmanual.write(f'{waiti}\n')
                tempmanual.write(f'{manual}\n')
                tempmanual.write(f'{waiti}\n')
                tempmanual.write(f'{end}\n')
                tempmanual.write(f'{waite}\n')
                tempmanual.write(f'{configt}\n')
                tempmanual.write(f'{configp}\n')
                tempmanual.flush()
                tempmanual.close()
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
                tempsticky.write(f'{configp}\n')
                tempsticky.write(f'{port_ports}\n')
                tempsticky.write(f'{waiti}\n')
                tempsticky.write(f'{access}\n')
                tempsticky.write(f'{waiti}\n')
                tempsticky.write(f'{enable_port_security}\n')
                tempsticky.write(f'{waiti}\n')
                tempsticky.write(f'{mac_address_limit}\n')
                tempsticky.write(f'{waiti}\n')
                tempsticky.write(f'{sticky}\n')
                tempsticky.write(f'{waiti}\n')
                tempsticky.write(f'{end}\n')
                tempsticky.write(f'{waite}\n')
                tempsticky.write(f'{configt}\n')
                tempsticky.write(f'{configp}\n')
                tempsticky.flush()
                tempsticky.close()
                continue

        elif security_mode == 'dynamic' or security_mode == 'Dynamic':
            ports = input('enter range or port for dynamic aging: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            port_ports = f"sendln 'int range {ports}'"
            access = "sendln 'switchport mode access'"
            dynamic = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            with open('tempstart.ttl', 'at') as tempdynamic:
                tempdynamic.write(f'{configp}\n')
                tempdynamic.write(f'{port_ports}\n')
                tempdynamic.write(f'{waiti}\n')
                tempdynamic.write(f'{access}\n')
                tempdynamic.write(f'{waiti}\n')
                tempdynamic.write(f'{dynamic}\n')
                tempdynamic.write(f'{waiti}\n')
                tempdynamic.write(f'{mac_address_limit}\n')
                tempdynamic.write(f'{waiti}\n')
                tempdynamic.write(f'{end}\n')
                tempdynamic.write(f'{waite}\n')
                tempdynamic.write(f'{configt}\n')
                tempdynamic.write(f'{configp}\n')
                tempdynamic.flush()
                tempdynamic.close()
                continue

        elif security_mode == 'shutdown' or security_mode == 'Shutdown':
            ports = input('enter range or port for shutdown: ')
            port_ports = f"sendln 'int range {ports}'"
            shutdown = "sendln 'shutdown'"
            with open('tempstart.ttl', 'at') as tempshutdown:
                tempshutdown.write(f'{configp}\n')
                tempshutdown.write(f'{port_ports}\n')
                tempshutdown.write(f'{waiti}\n')
                tempshutdown.write(f'{shutdown}\n')
                tempshutdown.write(f'{waiti}\n')
                tempshutdown.write(f'{end}\n')
                tempshutdown.write(f'{waite}\n')
                tempshutdown.write(f'{configt}\n')
                tempshutdown.write(f'{configp}\n')
                tempshutdown.flush()
                tempshutdown.close()
                continue  

        elif security_mode == 'violation.aging' or security_mode == 'Violation.aging':
            ports = input('enter range or port for violation & aging: ')
            aging_mode = input('enter aging mode static or time: ')
            port_ports = f"sendln 'int range {ports}'"
            if aging_mode == 'time' or aging_mode == 'Time':
                time_in_minutes = input('enter time in minutes: ')
                port_aging = f"sendln 'switchport port-security aging time {time_in_minutes}'"
                with open('tempstart.ttl', 'at') as temptime:
                    temptime.write(f'{configp}\n')
                    temptime.write(f'{port_ports}\n')
                    temptime.write(f'{waiti}\n')
                    temptime.write(f'{port_aging}\n')
                    temptime.write(f'{waiti}\n')
                    temptime.write(f'{end}\n')
                    temptime.write(f'{waite}\n')
                    temptime.write(f'{configt}\n')
                    temptime.write(f'{configp}\n')
                    violation_mode = input('enter violation mode > protect,restrict,shutdown: ')
                    port_violation = f"sendln 'switchport port-security violation {violation_mode}'"
                    temptime.write(f'{port_ports}\n')
                    temptime.write(f'{waiti}\n')
                    temptime.write(f'{port_violation}\n')
                    temptime.write(f'{waiti}\n')
                    temptime.write(f'{end}\n')
                    temptime.write(f'{waite}\n')
                    temptime.write(f'{configt}\n')
                    temptime.write(f'{configp}\n')
                    temptime.flush()
                    temptime.close()
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
                    tempstatic.close()
                    continue

        elif security_mode == 'EXIT' or security_mode == 'exit':
            security = False
            return

        else:
            continue
                


def mitigate_dhcp_attacks_and_arp(hostname):
    configp = f"waitln '{hostname}(config)#'"
    mitigate_dhcp_attacks_and_arp = True
    while mitigate_dhcp_attacks_and_arp == True:
        arp_or_dhcp = input('enter dhcp-snooping or arp-inspection or EXIT: ')
        if arp_or_dhcp == 'dhcp-snooping' or arp_or_dhcp == 'Dhcp-snooping':
            waiti = f"waitln '{hostname}(config-if-range)#'"
            enable_snooping = "sendln 'ip dhcp snooping'"
            ports_router = input('enter port for router/dhcp server: ')
            ports_trusted = input('enter trusted ports for dhcp snooping : ')
            limit = input('enter snooping rate #: ')
            vlans = input('enter vlans for snooping seperated by (,): ')
            snooping_switch = f"sendln 'int range {ports_trusted}'"
            snooping_router = f"sendln 'int range {ports_router}'"
            snooping_vlans = f"sendln 'ip dhcp snooping vlan {vlans}'"
            router_trust = "sendln 'ip dhcp snooping trust'"
            snooping_limit = f"sendln 'ip dhcp snooping limit rate {limit}'"
            exit_ = "sendln 'exit'" 
            with open('tempstart.ttl', 'at') as tempdhcp_snooping:
                tempdhcp_snooping.write(f'{configp}\n')
                tempdhcp_snooping.write(f'{enable_snooping}\n')
                tempdhcp_snooping.write(f'{configp}\n')
                tempdhcp_snooping.write(f'{snooping_router}\n')
                tempdhcp_snooping.write(f'{waiti}\n')
                tempdhcp_snooping.write(f'{router_trust}\n')
                tempdhcp_snooping.write(f'{waiti}\n')
                tempdhcp_snooping.write(f'{exit_}\n')
                tempdhcp_snooping.write(f'{configp}\n')
                tempdhcp_snooping.write(f'{snooping_switch}\n')
                tempdhcp_snooping.write(f'{waiti}\n')
                tempdhcp_snooping.write(f'{snooping_limit}\n')
                tempdhcp_snooping.write(f'{waiti}\n')
                tempdhcp_snooping.write(f'{exit_}\n')
                tempdhcp_snooping.write(f'{configp}\n')
                tempdhcp_snooping.write(f'{snooping_vlans}\n')
                tempdhcp_snooping.write(f'{configp}\n')
                tempdhcp_snooping.flush()
                tempdhcp_snooping.close()
                continue
        
        elif arp_or_dhcp == 'arp-inspection':
            vlans = input('enter vlans for arp inspection seperated by (,): ')
            enable_arp = f"sendln 'ip arp inspection vlan {vlans}'"
            with open('tempstart.ttl', 'at') as temparp_inspection:
                temparp_inspection.write(f'{configp}\n')
                temparp_inspection.write(f'{enable_arp}\n')
                temparp_inspection.write(f'{configp}\n')
                temparp_inspection.flush()
                temparp_inspection.close()
                continue
            
        elif arp_or_dhcp == 'EXIT' or arp_or_dhcp == 'exit':
            mitigate_dhcp_attacks_and_arp = False
            return
        
        else:
            continue        
                

def stp_(hostname):    
    ports = input('enter range or port for spanning tree: ')
    mode = input('enter rapid-pvst, pvst or mst: ')
    waite = f"waitln '{hostname}#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    configp = f"waitln '{hostname}(config)#'"
    port_mode = f"sendln 'spanning-tree mode {mode}'"
    port_ports = f"sendln 'int range {ports}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    portfast = "sendln 'spanning-tree portfast'"
    bpduguard = "sendln 'spanning-tree bpduguard enable'"
    with open('tempstart.ttl', 'at') as tempstp:
        tempstp.write(f'{configp}\n')
        tempstp.write(f'{port_mode}\n')
        tempstp.write(f'{configp}\n')
        tempstp.write(f'{port_ports}\n')
        tempstp.write(f'{waiti}\n')
        tempstp.write(f'{portfast}\n')
        tempstp.write(f'{waiti}\n')
        tempstp.write(f'{bpduguard}\n')
        tempstp.write(f'{waiti}\n')
        tempstp.write(f'{end}\n')
        tempstp.write(f'{waite}\n')
        tempstp.write(f'{configt}\n')
        tempstp.write(f'{configp}\n')
        tempstp.flush()
        tempstp.close()
        return ports

def start_(hostname):
    connect = "connect '/C=3'"
    setsync = "setsync 1"                                                     
    password = input('enable secret password: ')
    passw_secret = f"sendln 'enable secret {password}'"
    login = "sendln 'login'"
    waite = f"waitln 'Switch#'"
    wait = f"waitln 'Switch>'"
    enable = "sendln 'enable'"
    configt = "sendln 'configure terminal'"
    configp = f"waitln 'Switch(config)#'"
    configp_w_host = f"waitln '{hostname}(config)#"
    hostname_command = f"sendln 'hostname {hostname}'"
    with open('tempstart.ttl', 'w+') as tempstart:
        tempstart.write(f'{setsync}\n')
        tempstart.write(f'{connect}\n')
        tempstart.write(f'{wait}\n')
        tempstart.write(f'{enable}\n')
        tempstart.write(f'{waite}\n')
        tempstart.write(f'{configt}\n')
        tempstart.write(f'{configp}\n')
        tempstart.write(f'{hostname_command}\n')
        tempstart.write(f'{configp_w_host}\n')
        tempstart.write(f'{passw_secret}\n')
        tempstart.write(f'{configp_w_host}\n')
        tempstart.write(f'{login}\n')
        tempstart.write(f'{configp_w_host}\n')
        tempstart.flush()
        tempstart.close()
        return 

def finish_(hostname):
    name_of_file = input('enter name for log file without .log: ')
    Desktop = Path.home() / "Desktop"
    log_file = Desktop / f"{name_of_file}.log"
    start_logging = f"logopen '{str(log_file)}'"
    stop_logging = "logclose"
    configp = f"waitln '{hostname}(config)#'"
    save = "sendln 'do copy running-config startup-config'"
    save_prompt = "waitln 'Destination filename [startup-config]?'"
    show = "sendln 'do show start'"
    terminal_length = "sendln 'terminal length 0'"
    carriage_return = "sendln ''"
    with open('tempfinish.ttl', 'w+') as tempfinish:
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
        tempfinish.flush()
        tempfinish.close()
        return
        
        

def delete_save(hostname):
    starting_prompt = f"waitln 'Press RETURN to get started!: '"
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
    reload = "sendln 'do reload in 0'"
    enable = "sendln 'enable'"
    configt = "sendln 'configure terminal'"
    configp = f"waitln '{hostname}(config)#'"
    vlan_dat_delete_prompt = "waitln 'Delete filename [vlan.dat]?'"
    vlan_dat_delete_prompt_confirm = "waitln '[confirm]'"
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
        tempdelete.write(f'{reload}\n')
        tempdelete.write(f'{reload_prompt}\n')
        tempdelete.write(f'{carriage_return}\n')
        tempdelete.write(f'{reload_confirm}\n')
        tempdelete.write(f'{reload_confirm_no}\n')
        tempdelete.flush()
        tempdelete.close()
        return 
    

def ParkingLot_Blackhole(hostname, port_result1, port_result2, port_result3):
    print(f'vlan ports: {port_result1}')
    print(f'etherchannel & trunking ports: {port_result2}')
    print(f'stp enabled ports: {port_result3}')
    blackhole = input('please enter Parking or Blackhole vlan: ')
    park_ports = input('enter ports for Parking_Lot: ')
    port_ports = f"sendln 'int range {park_ports}'"
    access = "sendln 'switchport mode access'"
    access_vlan = f"sendln 'switchport access {blackhole}'"
    end = "sendln 'end'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    configp = f"waitln '{hostname}(config)#'"
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
        tempBlackhole_ParkingLot.close()
        return park_ports

def clear_screen():
    os.system('cls')
    return

def filecheck():
    try:
        with open('tempstart.ttl') as check:
            check.close()
            return 'y'
    
    except FileNotFoundError:
        print('tempstart not found')
        input('press enter to continue:')
        return 

'''
while loop, checking value of 'menu_Input' if value is on list then continue the loop
each 'elif' is checking for specific input value to call respective functions
includes an exit and "mysterious values" or "unknown" check at the bottom of the loop 
'''
print('use start. to initialize Macro file.')
print('finish and delete are seperate files, and can be chosen after macro is set.')
pause = input('press return: ')
hostname = input('enter machines hostname: ')
program_running = True
while program_running is True:    
    clear_screen()
    tempstart = filecheck()
    menu_input = menu()
    while menu_input == '1':
        start_(hostname)
        break 
    
    while menu_input == '2':
        if tempstart == 'y':
            clock(hostname)
            break
        
        else:
            break
            
    while menu_input == '3':
        if tempstart == 'y':
            line_con(hostname)
            break
        
        else:
            break

    while menu_input == '4':
        if tempstart == 'y':
            vty_line(hostname)
            break
        
        else:
            break

    while menu_input == '5':
        if tempstart == 'y':
            c_vlans(hostname)   
            break
        
        else:
            break

    while menu_input == '6':
        if tempstart == 'y':
            port_result1 = a_vlans(hostname)
            break
        
        else:
            break

    while menu_input == '7':
        if tempstart == 'y':
            vlan_ip(hostname)
            break
        
        else:
            break

    while menu_input == '8':
        if tempstart == 'y':
            ip_gateway(hostname)
            break
        
        else:
            break

    while menu_input == '9':
        if tempstart == 'y':
            port_result2 = trunking_m(hostname)
            break

        else:
            break

    while menu_input == '10':
        if tempstart == 'y':
            port_result2 = etherchannel(hostname)
            break
        
        else:
            break

    while menu_input == '11':
        if tempstart == 'y':
            port_result3 = stp_(hostname)
            break
        
        else:
            break

    while menu_input == '12':
        if tempstart == 'y':
            Blackhole_ports = ParkingLot_Blackhole(hostname, port_result1, port_result2, port_result3)
            break
        
        else:
            break

    while menu_input == '13':
        if tempstart == 'y':
            port_sec(hostname)
            break
        
        else:
            break

    while menu_input == '14':
        if tempstart == 'y':
            mitigate_dhcp_attacks_and_arp(hostname)
            break

        else:
            break

    while menu_input == '15':
        print(f'vlan ports: {port_result1}')
        print(f'etherchannel & trunking ports: {port_result2}')
        print(f'stp enabled ports: {port_result3}')
        print(f'Parking_Lot or Blackhole ports: {Blackhole_ports}')
        print(f'hostname: {hostname}')
        pause = input('press ENTER to continue...')
        break

    while menu_input == '16':
        finish_(hostname)
        break
        
    while menu_input == '17':
        delete_save(hostname)
        os.remove('tempfinish.ttl')
        os.remove('tempstart.ttl')
        break

    if menu_input == 'EXIT' or menu_input == 'exit':
        print("Goodbye!!!?")
        os.remove('tempdelete.ttl')
        continue

    else:
        continue                
                        
'''
switch config script generator
by: @ILICKTOES 
version: 2.0
This script generates a .ttl file to be used with Tera Term to automate the configuration of Cisco switches.
Usage: Run the script and follow the prompts to input configuration details. Select the desired configuration options from the menu.
The script will create a temporary .ttl file with the specified configurations.
'''