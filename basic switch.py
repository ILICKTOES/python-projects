'''
Jacob Genereaux

FOLID:j_genereaux
Student#:1298774
CTN - computer technician script
'''
from datetime import datetime as dt
from pathlib import Path
import os.path as file
import calendar as cal
import os


def menu():
    print("-Macro-Maker-----------\n")
    print("1."+"Hostname & EXEC password\n")
    print("2."+"Set clock\n")
    print("3."+"Console line config\n")
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
    return input('select option: ')

def clock(hostname):
    class time_now():
        def __init__(self):
            self.time = str(dt().time()).replace('.', ':').replace(' ', ':').split(':')

        def hr(self):
            return str(self.time[1])

        def yr(self):
            return str(self.time[0].split('-')[0])

        def mn(self):
            return str(cal.month_name(int(self.time[0].split('-')[1])))
            
        def min(self):
            return str(self.time[2])
        
        def dy(self):
            return str(self.time[0].split('-')[2])
        
    print(f'Setting clock to {time_now().hr()}:{time_now().min()}:00 {time_now().dy()} {time_now().mn()} {time_now().yr()}\n')
    configp = f"waitln '{hostname}(config)#'"
    clock_complete = f"sendln 'do clock set {time_now().hr()}:{time_now().min()}:00 {time_now().dy()} {time_now().mn()} {time_now().yr()}'"  
    with open('tempstart.ttl', 'at') as tempclock:
        commands = [
                    configp,
                    clock_complete,
                    configp,
                    ]
        tempclock.writelines(f'{commands}\n'\
        for com in commands)
        tempclock.flush()
        print('clock finished!')
        input('press enter to continue: ')
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
        commands = [
                    configp,
                    line_con,
                    waitl,
                    passw_c,
                    waitl,
                    login,
                    waitl,
                    logging_sync,
                    waitl,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempvty_password.writelines(f'{commands}\n'\
        for com in commands)
        tempvty_password.flush()
        print('line con done!')
        input('press enter to continue: ')
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
        commands = [
                    configp,
                    line_vty,
                    waitl,
                    passw_v,
                    waitl,
                    login,
                    waitl,
                    logging_sync,
                    waitl,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempvty_password.writelines(f'{commands}\n'\
        for com in commands)
        tempvty_password.flush()
        print('vty-lines done!')
        input('press enter to continue: ')
        return

def a_vlans(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    vname = input('vlan name ex. 10: ')
    ports = input('enter range or port to assign vlan: ')
    port_ports = f"sendln 'interface range G{ports}'"
    access = "sendln 'switchport mode access'"
    assign = f"sendln 'switchport access vlan {vname}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempassign_ports_vlan:
        commands = [
                    configp,
                    port_ports,
                    waiti,
                    access,
                    waiti,
                    assign,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempassign_ports_vlan.writelines(f'{commands}\n'\
        for com in commands)
        tempassign_ports_vlan.flush()
        print('assigned ports to vlans!')
        input('press enter to continue: ')
        return ports
        
def c_vlans(hostname):
    waitv = f"waitln '{hostname}(config-vlan)#'"
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    vnum = input('vlan number: ')
    vname = input('name for vlan ex. guests: ')
    vlan_create = f"sendln 'vlan {vnum}'"
    vlan_name = f"sendln 'name {vname}'"
    with open('tempstart.ttl', 'at') as tempcreate_vlan:
        commands = [
                    configp,
                    vlan_create,
                    waitv,
                    vlan_name,
                    waitv,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempcreate_vlan.writelines(f'{commands}\n'\
        for com in commands)
        tempcreate_vlan.flush()
        print('vlan created!')
        input('press enter to continue: ')
        return
        
def ip_gateway(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waite = f"waitln '{hostname}#'"
    ip_add = input('ip default-gateway: ')
    default_gateway = f"sendln 'ip default-gateway {ip_add}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    with open('tempstart.ttl', 'at') as tempdefault_gateway:
        commands = [
                    configp,
                    default_gateway,
                    configp,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempdefault_gateway.writelines(f'{commands}\n'\
        for com in commands)
        tempdefault_gateway.flush()
        print('default-gateway done!')
        input('press enter to continue: ')
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
        commands = [
                    configp,
                    interface_vlan,
                    waiti,
                    assign_ip,
                    waiti,
                    no_shutdown,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempvlan_ip.writelines(f'{commands}\n'\
        for com in commands)
        tempvlan_ip.flush()
        print('vlan ip done!')
        input('press enter to continue: ')
        return

def trunking_m(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    allowedp = input('allowed vlans separate with comma do not MISTYPE!!!: ') 
    native = input('native vlan: ')
    ports = input('enter range or port to trunk: ')
    port_ports = f"sendln 'int range G{ports}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    trunk = f"sendln 'switchport mode trunk'"
    nonegotiate = f"sendln 'switchport nonegotiate'"
    trunk_native = f"sendln 'switchport trunk native vlan {native}'"              
    trunk_allowed = f"sendln 'switchport trunk allowed vlan {allowedp},{native}'"
    with open('tempstart.ttl', 'at') as tempmanual_trunking:
        commands = [
                    configp,
                    port_ports,
                    waiti,
                    trunk,
                    waiti,
                    nonegotiate,
                    waiti,
                    trunk_native,
                    waiti,
                    trunk_allowed,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempmanual_trunking.writelines(f'{commands}\n'\
        for com in commands)
        tempmanual_trunking.flush()
        print('manual trunking done!')
        input('press enter to continue: ')
        return ports

def etherchannel(hostname):
    configp = f"waitln '{hostname}(config)#'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    active_LACP = "active=LACP unconditionally\n"
    auto_PAgP = "auto=PAgP if another PAgP device is connected\n"
    desirable_PAgP = "desirable=PAgP unconditionally\n"
    on_enable = "on, or enable=Etherchannel only\n"
    passive_LACP = "passive=LACP if another LACP device is connected\n"
    exit_ = "sendln 'exit'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    mode = input(f'{active_LACP}{auto_PAgP}{desirable_PAgP}{on_enable}{passive_LACP}enter etherchannel mode: ')
    native = input('native vlan: ')
    allowedp = input('allowed vlans separate with comma do not MISTYPE!!!: ')
    ports = input('enter range or port to etherchannel: ')
    channel = input('channel group & port-channel number: ')
    port_ports = f"sendln 'int range G{ports}'"
    channel_group = f"sendln 'channel-group {channel} mode {mode}'"
    port_channel = f"sendln 'int port-channel {channel}'"
    trunk = f"sendln 'switchport mode trunk'"
    trunk_native = f"sendln 'switchport trunk native vlan {native}'"              
    trunk_allowed = f"sendln 'switchport trunk allowed vlan {allowedp},{native}'"
    nonegotiate = f"sendln 'switchport nonegotiate'"
    with open('tempstart.ttl', 'at') as tempetherchannel:
        commmands =[
                    configp,
                    port_ports,
                    waiti,
                    channel_group,
                    waiti,
                    exit_,
                    configp,
                    port_channel,
                    waiti,
                    trunk,
                    waiti,
                    nonegotiate,
                    waiti,
                    trunk_native,
                    waiti,
                    trunk_allowed,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempetherchannel.writelines(f'{commmands}\n'\
        for com in commmands)
        tempetherchannel.flush()
        print('etherchannel done!')
        input('press enter to continue: ')
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
            port_ports = f"sendln 'int range G{ports}'"
            access = "sendln 'switchport mode access'"
            enable_port_security = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            manual = f"sendln 'switchport port-security mac-address {mac_address}'"
            with open('tempstart.ttl', 'at') as tempmanual:
                commands = [
                            configp,
                            port_ports,
                            waiti,
                            access,
                            waiti,
                            enable_port_security,
                            waiti,
                            mac_address_limit,
                            waiti,
                            manual,
                            waiti,
                            end,
                            waite,
                            configt,
                            configp,
                            ]
                tempmanual.writelines(f'{commands}\n'\
                for com in commands)
                tempmanual.flush()
                print('manual aging done!')
                input('press enter to continue: ')
                continue       

        elif security_mode == 'sticky' or security_mode == 'Sticky':
            ports = input('enter range or port for sticky aging: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            port_ports = f"sendln 'int range G{ports}'"
            access = "sendln 'switchport mode access'"
            enable_port_security = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            sticky = "sendln 'switchport port-security mac-address sticky'"
            with open('tempstart.ttl', 'at') as tempsticky:
                commands = [
                            configp,
                            port_ports,
                            waiti,
                            access,
                            waiti,
                            enable_port_security,
                            waiti,
                            mac_address_limit,
                            waiti,
                            sticky,
                            waiti,
                            end,
                            waite,
                            configt,
                            configp,
                            ]
                tempsticky.writelines(f'{commands}\n'\
                for com in commands)
                tempsticky.flush()
                ('sticky aging done!')
                input('press enter to continue: ')
                continue

        elif security_mode == 'dynamic' or security_mode == 'Dynamic':
            ports = input('enter range or port for dynamic aging: ')
            number_of_mac = input('enter maximum amount of mac addressess: ')
            port_ports = f"sendln 'int range G{ports}'"
            access = "sendln 'switchport mode access'"
            dynamic = "sendln 'switchport port-security'"
            mac_address_limit = f"sendln 'switchport port-security maximum {number_of_mac}'"
            with open('tempstart.ttl', 'at') as tempdynamic:
                commands = [
                            configp,
                            port_ports,
                            waiti,
                            access,
                            waiti,
                            dynamic,
                            waiti,
                            mac_address_limit,
                            waiti,
                            end,
                            waite,
                            configt,
                            configp,
                            ]
                tempdynamic.writelines(f'{commands}\n'\
                for com in commands)
                tempdynamic.flush()
                print('dynamic aging done!')
                input('press enter to continue: ')
                continue

        elif security_mode == 'shutdown' or security_mode == 'Shutdown':
            ports = input('enter range or port for shutdown: ')
            port_ports = f"sendln 'int range G{ports}'"
            shutdown = "sendln 'shutdown'"
            with open('tempstart.ttl', 'at') as tempshutdown:
                commands = [
                            configp,
                            port_ports,
                            waiti,
                            shutdown,
                            waiti,
                            end,
                            waite,
                            configt,
                            configp,
                            ]                                      
                tempshutdown.writelines(f'{commands}\n'\
                for com in commands)
                tempshutdown.flush()
                print('shutdown done!')
                input('press enter to continue: ')
                continue  
                

        elif security_mode == 'violation.aging' or security_mode == 'Violation.aging':
            ports = input('enter range or port for violation & aging: ')
            aging_mode = input('enter aging mode static or time: ')
            port_ports = f"sendln 'int range G{ports}'"
            if aging_mode == 'time' or aging_mode == 'Time':
                time_in_minutes = input('enter time in minutes: ')
                port_aging = f"sendln 'switchport port-security aging time {time_in_minutes}'"
                with open('tempstart.ttl', 'at') as temptime:
                    commands = [
                                configp,
                                port_ports,
                                waiti,
                                port_aging,
                                waiti,
                                end,
                                waite,
                                configt,
                                configp,
                                ]
                    temptime.writelines(f'{commands}\n'\
                    for com in commands)
                    violation_mode = input('enter violation mode > protect,restrict,shutdown: ')
                    port_violation = f"sendln 'switchport port-security violation {violation_mode}'"
                    commands = [
                                port_ports,
                                waiti,
                                port_violation,
                                waiti,
                                end,
                                waite,
                                configt,
                                configp,
                                ]
                    temptime.writelines(f'{commands}\n'\
                    for com in commands)
                    temptime.flush()
                    print('aging time done!')
                    input('press enter to continue: ')
                    continue
        
            elif aging_mode == 'static' or aging_mode == 'Static':
                ports = input('enter range or port for static aging: ')
                port_ports = f"sendln 'int range G{ports}'"
                port_aging = "sendln 'switchport port-security aging static'"
                with open('tempstart.ttl', 'at') as tempstatic:
                    commands = [
                                wait,
                                port_ports,
                                wait,
                                port_aging,
                                wait,
                                ]
                    violation_mode = input('enter violation mode > protect,restrict,shutdown: ')
                    port_violation = f"sendln 'switchport port-security violation {violation_mode}'"
                    commands = [            
                                wait,
                                port_violation,
                                wait,
                                end,
                                wait,
                                configt,
                                wait,
                                ]
                    tempstatic.writelines(f'{commands}\n'\
                    for com in commands)
                    tempstatic.flush()
                    print('aging static done!')
                    input('press enter to continue: ')
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
            ports_trusted = input('enter trusted ports for dhcp snooping: ')
            limit = input('enter snooping rate #: ')
            vlans = input('enter vlans for snooping separated by (,): ')
            snooping_switch = f"sendln 'int range G{ports_trusted}'"
            snooping_router = f"sendln 'int range G{ports_router}'"
            snooping_vlans = f"sendln 'ip dhcp snooping vlan {vlans}'"
            router_trust = "sendln 'ip dhcp snooping trust'"
            snooping_limit = f"sendln 'ip dhcp snooping limit rate {limit}'"
            exit_ = "sendln 'exit'" 
            with open('tempstart.ttl', 'at') as tempdhcp_snooping:
                commands = [
                            configp,
                            enable_snooping,
                            configp,
                            snooping_router,
                            waiti,
                            router_trust,
                            waiti,
                            exit_,
                            configp,
                            snooping_switch,
                            waiti,
                            snooping_limit,
                            waiti,
                            exit_,
                            configp,
                            snooping_vlans,
                            configp,
                            ]
                tempdhcp_snooping.writelines(f'{commands}\n'\
                for com in commands)
                tempdhcp_snooping.flush()
                print('dhcp-snooping done!')
                input('press enter to continue: ')
                continue
        
        elif arp_or_dhcp == 'arp-inspection':
            vlans = input('enter vlans for arp inspection separated by (,): ')
            ports_trusted = input('enter trusted ports for arp inspection: ')
            enable_arp = f"sendln 'ip arp inspection vlan {vlans}'"
            enable_trust = f"sendln'ip arp inspection trust'"
            with open('tempstart.ttl', 'at') as temparp_inspection:
                commands = [
                            configp,
                            enable_arp,
                            configp,
                            enable_trust,
                            configp
                            ]
                temparp_inspection.writelines(f'{commands}\n'\
                for com in commands)
                temparp_inspection.flush()
                print('arp-inspection done')
                input('press enter to continue: ')
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
    port_ports = f"sendln 'int range G{ports}'"
    configt = "sendln 'configure terminal'"
    end = "sendln 'end'"
    portfast = "sendln 'spanning-tree portfast'"
    bpduguard = "sendln 'spanning-tree bpduguard enable'"
    with open('tempstart.ttl', 'at') as tempstp:
        commands = [
                    configp,
                    port_mode,
                    configp,
                    port_ports,
                    waiti,
                    portfast,
                    waiti,
                    bpduguard,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempstp.writelines(f'{commands}\n'\
        for com in commands)
        tempstp.flush()
        print('stp done!')
        input('press enter to continue: ')
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
    configp_w_host = f"waitln '{hostname}(config)#'"
    hostname_command = f"sendln 'hostname {hostname}'"
    with open('tempstart.ttl', 'w+') as tempstart:
        commands = [
                    setsync,
                    connect,
                    wait,
                    enable,
                    waite,
                    configt,
                    configp,
                    hostname_command,
                    configp_w_host,
                    passw_secret,
                    configp_w_host,
                    login,
                    configp_w_host,
                    ]
        tempstart.writelines(f'{commands}\n'\
        for com in commands)
        tempstart.flush()
        try:
            os.remove('tempstart.ttl')
        
        except FileNotFoundError:
            pass
        
        print('initialization done!')
        input('press enter to continue: ')
        return 

def finish_(hostname):
    name_of_file = input('enter name for log file without .log: ')
    Desktop = Path.home() / "OneDrive" / "Desktop"
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
        commands = [
                    terminal_length,
                    configp,
                    save,
                    save_prompt,    
                    carriage_return,
                    configp,
                    start_logging,
                    show,
                    configp,
                    stop_logging,
                    ]
        tempfinish.writelines(f'{commands}\n'\
        for com in commands)
        tempfinish.flush()
        print('finish macro done!')
        input('press enter to continue: ')
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
        commands = [
                    setsync,
                    connect,
                    starting_prompt,
                    carriage_return,
                    waitp,
                    passw_c,
                    wait,
                    enable,
                    waitp,
                    passw_e,
                    waite,
                    configt,
                    configp,
                    delete_startup,
                    delet_startup_prompt,      
                    carriage_return,
                    configp,
                    delete_vlan_dat,
                    vlan_dat_delete_prompt,
                    carriage_return,
                    vlan_dat_delete_prompt_confirm,
                    carriage_return,        
                    configp,
                    reload,
                    reload_prompt,
                    carriage_return,
                    reload_confirm,
                    reload_confirm_no,
                    ]
        tempdelete.writelines(f'{commands}\n'\
        for com in commands)
        tempdelete.flush()
        try:
            os.remove('tempstart.ttl')
            os.remove('tempfinish.ttl')
        
        except FileNotFoundError:
            pass
       
        print('delete macro done!')
        input('press enter to continue: ')
        return 
    

def ParkingLot_Blackhole(hostname, port_result1, port_result2, port_result3):
    print(f'vlan ports: {port_result1}')
    print(f'etherchannel & trunking ports: {port_result2}')
    print(f'stp enabled ports: {port_result3}')
    blackhole = input('please enter Parking or Blackhole vlan: ')
    park_ports = input('enter ports for Parking_Lot: ')
    port_ports = f"sendln 'int range G{park_ports}'"
    access = "sendln 'switchport mode access'"
    access_vlan = f"sendln 'switchport access vlan {blackhole}'"
    end = "sendln 'end'"
    waiti = f"waitln '{hostname}(config-if-range)#'"
    waite = f"waitln '{hostname}#'"
    configp = f"waitln '{hostname}(config)#'"
    configt = "sendln 'configure terminal'"
    with open('tempstart.ttl', 'at') as tempBlackhole_ParkingLot:
        commands = [ 
                    configp,
                    port_ports,
                    waiti,
                    access,
                    waiti,
                    access_vlan,
                    waiti,
                    end,
                    waite,
                    configt,
                    configp,
                    ]
        tempBlackhole_ParkingLot.writelines(f'{commands}\n'\
        for com in commands)
        tempBlackhole_ParkingLot.flush()
        print('parking lot done!')
        input('press enter to continue: ')
        return park_ports

def show_ports(port_result1='None', port_result2='None', port_result3='None', Blackhole_ports='None', hostname='None'):
        print(f'vlan ports: {port_result1}')
        print(f'etherchannel & trunking ports: {port_result2}')
        print(f'stp enabled ports: {port_result3}')
        print(f'Parking_Lot or Blackhole ports: {Blackhole_ports}')
        print(f'hostname: {hostname}')
        input('press ENTER to continue...')
        return
    

def clear_screen():
    os.system('cls')
    return


def filecheck():
    if file.exists('tempstart.ttl'):
            return 'y'
    
    else:
        print('tempstart not found')
        input('press enter to continue:')
        return 'n'

'''
while loop, checking value of 'menu_Input' if value is on list then continue the loop
each 'elif' is checking for specific input value to call respective functions
includes an exit and "mysterious values" or "unknown" check at the bottom of the loop 
'''
print('use \'start\'. to initialize Macro file.')
print('if file already exists, do not use start. and it will add to the file with a correct hostname.')
print('finish and delete are seperate files, and can be chosen after macro is set.')
pause = input('press return: ')
clear_screen()
hostname = input('enter machines hostname: ')
program_running = True
while program_running is True:    
    tempstart_file = filecheck()
    clear_screen()
    menu_input = menu()
    if menu_input == '1':
        start_(hostname)
    
    if menu_input == '2':
        if tempstart_file == 'y':
            clock(hostname)
                
    if menu_input == '3':
        if tempstart_file == 'y':
            line_con(hostname)
               
    if menu_input == '4':
        if tempstart_file == 'y':
            vty_line(hostname)
        
    if menu_input == '5':
        if tempstart_file == 'y':
            c_vlans(hostname)   
        
    if menu_input == '6':
        if tempstart_file == 'y':
            port_result1 = a_vlans(hostname)

    if menu_input == '7':
        if tempstart_file == 'y':
            vlan_ip(hostname)

    if menu_input == '8':
        if tempstart_file == 'y':
            ip_gateway(hostname)

    if menu_input == '9':
        if tempstart_file == 'y':
            port_result2 = trunking_m(hostname)

    if menu_input == '10':
        if tempstart_file == 'y':
            port_result2 = etherchannel(hostname)        
        
    if menu_input == '11':
        if tempstart_file == 'y':
            port_result3 = stp_(hostname)
        
    if menu_input == '12':
        if tempstart_file == 'y':
            Blackhole_ports = ParkingLot_Blackhole(hostname, port_result1, port_result2, port_result3)
        
    if menu_input == '13':
        if tempstart_file == 'y':
            port_sec(hostname)
        
    if menu_input == '14':
        if tempstart_file == 'y':
            mitigate_dhcp_attacks_and_arp(hostname)
       
    if menu_input == '15':
        show_ports(port_result1, port_result2, port_result3, Blackhole_ports, hostname)

    if menu_input == '16':
        finish_(hostname)

    if menu_input == '17':
        delete_save(hostname)           
    
    if menu_input == 'EXIT' or menu_input == 'exit':
        print("Goodbye!!!?")
        break
    
    continue                
                        
'''
switch config script generator
by: @ILICKTOES
version: 3.5f
This script generates a .ttl file to be used with Tera Term to automate the configuration of Cisco switches.
Usage: Run the script and follow the prompts to input configuration details. Select the desired configuration options from the menu.
The script will create a temporary .ttl file with the specified configurations.
'''