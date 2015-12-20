#!/usr/bin/env python

import sys
import gzip
import struct
import pandalog_pb2
import csv

def read_log(name):
    entries = []

    with gzip.GzipFile(name, 'rb') as f:
        while True:
            le = pandalog_pb2.LogEntry()
            sz = f.read(8)
            if not sz: break
            sz = struct.unpack("<Q", sz)[0]
            data = f.read(sz)
            try:
                # print data
                le.ParseFromString(data)
                entries.append(le)
            except Exception as e:
                print e
                pass
    return entries

def write_data(log_entry_list, file_name):
    with open(file_name+'.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(log_entry_list)
    return None

if __name__ == "__main__":
    log_entry_list = [['pc', 'instr', 'call_name', 'pid', 'name', 'new_pid', 
                        'new_name', 'file_name', 'keyname', 'target_pid',
                        'target_name', 'section_id', 'section_name',
                        'port_id', 'port_name', 'client_pid', 'client_name',
                        'server_pid', 'server_name']]
    new_file = open(sys.argv[1].split('.')[0]+".txt","w")
    for entry in read_log(sys.argv[1]):
        new_file.write(str(entry))
    new_file.close()
    #     if getattr(entry, "new_pid").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("new_pid")
    #         log_entry.append(getattr(entry, "new_pid").pid)
    #         log_entry.append(getattr(entry, "new_pid").name.strip())
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_create_user_process"), "cur_p").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_user_process")
    #         log_entry.append(getattr(getattr(entry, "nt_create_user_process"), "cur_p").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_user_process"), "cur_p").name)
    #         log_entry.append(getattr(getattr(entry, "nt_create_user_process"), "new_p").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_user_process"), "new_p").name)
    #         log_entry.append(getattr(entry, "nt_create_user_process").new_long_name)
    #         log_entry_list.append(log_entry)
    #     if getattr(getattr(entry, "nt_terminate_process"), "cur_p").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_terminate_process")
    #         log_entry.append(getattr(getattr(entry, "nt_terminate_process"), "cur_p").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_terminate_process"), "cur_p").name)
    #         log_entry.append(getattr(getattr(entry, "nt_terminate_process"), "term_p").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_terminate_process"), "term_p").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_create_file"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_file")
    #         log_entry.append(getattr(getattr(entry, "nt_create_file"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_file"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_create_file").filename)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_read_file"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_read_file")
    #         log_entry.append(getattr(getattr(entry, "nt_read_file"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_read_file"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_read_file").filename)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_write_file"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_write_file")
    #         log_entry.append(getattr(getattr(entry, "nt_write_file"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_write_file"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_write_file").filename)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_delete_file"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_delete_file")
    #         log_entry.append(getattr(getattr(entry, "nt_delete_file"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_delete_file"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_delete_file").filename)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_query_key"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_query_key")
    #         log_entry.append(getattr(getattr(entry, "nt_query_key"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_query_key"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_query_key").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_delete_key"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_delete_key")
    #         log_entry.append(getattr(getattr(entry, "nt_delete_key"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_delete_key"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_delete_key").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_create_key"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_create_key"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_key"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_create_key").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_create_key_transacted"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_create_key_transacted"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_key_transacted"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_create_key_transacted").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_open_key"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_open_key"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_open_key"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_open_key").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_open_key_ex"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_ex"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_ex"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_open_key_ex").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_open_key_transacted"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_transacted"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_transacted"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_open_key_transacted").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_open_key_transacted_ex"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_key")
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_transacted_ex"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_open_key_transacted_ex"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_open_key_transacted_ex").keyname)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_read_virtual_memory"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_read_virtual_memory")
    #         log_entry.append(getattr(getattr(entry, "nt_read_virtual_memory"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_read_virtual_memory"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_read_virtual_memory"), "target").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_read_virtual_memory"), "target").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_write_virtual_memory"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_write_virtual_memory")
    #         log_entry.append(getattr(getattr(entry, "nt_write_virtual_memory"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_write_virtual_memory"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_write_virtual_memory"), "target").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_write_virtual_memory"), "target").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_create_section"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_section")
    #         log_entry.append(getattr(getattr(entry, "nt_create_section"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_create_section"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append('')
    #         log_entry.append('')
    #         log_entry.append(getattr(entry, "nt_create_section").section_id)
    #         log_entry.append(getattr(entry, "nt_create_section").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_open_section"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_open_section")
    #         log_entry.append(getattr(getattr(entry, "nt_open_section"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_open_section"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append('')
    #         log_entry.append('')
    #         log_entry.append(getattr(entry, "nt_open_section").section_id)
    #         log_entry.append(getattr(entry, "nt_open_section").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(getattr(entry, "nt_map_view_of_section"), "section"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_map_view_of_section")
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_map_view_of_section"), "section"), "proc").pid)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_map_view_of_section"), "section"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_map_view_of_section"), "target").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_map_view_of_section"), "target").name)
    #         log_entry.append(getattr(getattr(entry, "nt_map_view_of_section"), "section").section_id)
    #         log_entry.append('')
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(getattr(entry, "nt_create_port"), "port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_create_port")
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_create_port"), "port"), "proc").pid)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_create_port"), "port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_create_port"), "port").id)
    #         log_entry.append(getattr(entry, "nt_create_port").port_name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_connect_port")
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "proc").pid)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_connect_port"), "port").id)
    #         log_entry.append(getattr(entry, "nt_connect_port").port_name)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "client").pid)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "client").name)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "server").pid)
    #         log_entry.append(getattr(getattr(getattr(entry, "nt_connect_port"), "port"), "server").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_accept_connect_port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_accept_connect_port")
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_accept_connect_port").id)
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "client").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "client").name)
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "server").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_accept_connect_port"), "server").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_request_port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_request_port")
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_request_port").id)
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "client").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "client").name)
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "server").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_port"), "server").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_request_wait_reply_port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_request_wait_reply_port")
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_request_wait_reply_port").id)
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "client").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "client").name)
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "server").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_request_wait_reply_port"), "server").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_reply_port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_reply_port")
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_reply_port").id)
    #         log_entry.append("")
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "client").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "client").name)
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "server").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_reply_port"), "server").name)
    #         log_entry_list.append(log_entry)
    #         continue
    #     if getattr(getattr(entry, "nt_reply_wait_receive_port"), "proc").pid != 0:
    #         log_entry = []
    #         log_entry.append(getattr(entry, "pc"))
    #         log_entry.append(getattr(entry, "instr"))
    #         log_entry.append("nt_reply_wait_receive_port")
    #         log_entry.append(getattr(getattr(entry, "nt_reply_wait_receive_port"), "proc").pid)
    #         log_entry.append(getattr(getattr(entry, "nt_reply_wait_receive_port"), "proc").name)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append(getattr(entry, "nt_reply_wait_receive_port").id)
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry.append("")
    #         log_entry_list.append(log_entry)
    #         continue
    # print 'finished parsing'
    # write_data(log_entry_list, sys.argv[1].split('.')[0])
