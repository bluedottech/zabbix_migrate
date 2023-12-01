#!/usr/bin/env python3
import sys, getopt
import os
import argparse
import zabbix5
import zabbix6
import zabbix6dot4

try:
    import psycopg2, psycopg2.extras
except:
    print("Please install psycopg2-binary")
    sys.exit()
import shelve

def retrieve_data(name):
    if os.path.isfile(name):
        try:
            s = shelve.open(name)
        except Exception as e:
            print(f"Failed to open file {name}. Continuing...")
            return None
        return s[name]
    else:
        return None
    
def save_to_file(data, name):
    try:
        s = shelve.open("./data/"+name)
    except Exception as e:
        sys.exit(f"Failed to open file {name} for saving")
    s[name] = data
    s.close()

def delete_data(cur, table, action):
    if action == 'load':
        print(f"Deleting data from table {table}")
        try:
            cur.execute(f"DELETE FROM {table}")
        except Exception as e:
                cur.connection.rollback()
                print(f"Failed to delete existing data from database table {table}. {e}")
        cur.connection.commit()

def select_data(cur, table, action):
    dbrec = getattr(zabbix6, table)

    if action == 'dump':
        try:
            sql = f"SELECT * FROM {table}"
            cur.execute(sql)
            res = cur.fetchall()
        except psycopg2.DatabaseError as e:
            print(f"Error selecting data from table {table}. {e}")
            cur.connection.rollback()
        #save_to_file(res, table)  
        dbrows = list()
        for row in res:
            rec = dbrec()
            for col in row.keys():
                setattr(rec, col, row[col])
            dbrows.append(rec)
        fname = f"./data/{table}"
        with shelve.open(fname)as shelve_file:
            shelve_file[table] = dbrows
        

        
    if action == 'load':
        res = retrieve_data(table)
        if res is not None:
            try:
                for r in res:
                    cur.execute(f"INSERT INTO {table} VALUES {r}")
            except Exception as e:
                cur.connection.rollback()
                print(f"Failed to insert new data into table {table}. {e}")
            cur.connection.commit()
        else:
            pass

def main(args):
    table_list=['actions', 'applications', 'conditions', 'role', 'users', 'usrgrp', 'auditlog', 'auditlog_details', 'maintenances', 'hosts', 'autoreg_host', 'events', 'acknowledges', 'correlation', 'corr_condition', 'corr_condition_group', 'config_autoreg_tls', 'corr_condition_tag', 'corr_condition_tagpair', 'corr_condition_tagvalue', 'corr_operation', 'media_type', 'alerts', 'dashboard', 'dashboard_user', 'dashboard_usrgrp', 'drules', 'dhosts', 'dchecks', 'event_recovery', 'escalations', 'event_suppress', 'event_tag', 'valuemaps', 'valuemap','interface', 'items', 'triggers', 'graphs', 'dservices', 'functions', 'globalvars', 'graphs_items', 'graph_theme', 'trigger_queue', 'hstgrp', 'config', 'group_prototype', 'group_discovery', 'host_discovery', 'host_inventory', 'history_str', 'host_tag', 'hosts_groups', 'hosts_templates', 'globalmacro', 'regexps', 'expressions', 'hostmacro', 'httptest', 'httpstep', 'httpstep_field', 'httpstepitem', 'httptestitem', 'ids', 'httptest_field', 'interface_discovery', 'item_condition', 'item_preproc', 'item_rtdata', 'maintenance_tag', 'timeperiods', 'lld_macro_path', 'maintenances_windows', 'maintenances_groups', 'maintenances_hosts', 'media', 'media_type_param', 'operations', 'scripts', 'opcommand', 'screens', 'screens_items', 'item_discovery', 'opcommand_hst', 'opconditions', 'opgroup', 'opcommand_grp', 'opinventory', 'opmessage', 'opmessage_grp', 'opmessage_usr', 'optemplate', 'problem', 'rights', 'problem_tag', 'proxy_autoreg_host', 'proxy_dhistory', 'profiles', 'services', 'sysmaps', 'services_links', 'sysmaps_elements', 'services_times', 'sessions', 'sysmap_element_trigger', 'sysmap_element_url', 'sysmap_url', 'sysmap_user', 'sysmap_usrgrp', 'sysmaps_links', 'sysmaps_link_triggers', 'sysmap_shape', 'tag_filter', 'task', 'task_acknowledge', 'task_check_now', 'task_close_problem', 'task_remote_command_result', 'task_remote_command', 'trigger_tag', 'users_groups', 'trigger_depends', 'trigger_discovery', 'dashboard_page', 'widget', 'service_alarms', 'widget_field', 'media_type_message', 'task_data', 'task_result', 'interface_snmp', 'module', 'graph_discovery','lld_override', 'lld_override_operation', 'lld_override_condition', 'lld_override_opperiod', 'lld_override_opstatus', 'lld_override_opdiscover', 'lld_override_ophistory', 'lld_override_optrends', 'lld_override_opseverity', 'lld_override_optag', 'lld_override_optemplate', 'lld_override_opinventory', 'trends_uint', 'httptest_tag', 'item_tag', 'sysmaps_element_tag', 'report', 'report_param', 'report_user', 'report_usrgrp', 'token', 'script_param', 'valuemap_mapping', 'item_parameter', 'role_rule']
    
    if args.dump:
        action = "dump"
        if not args.source or not args.source_user or not args.source_pass:
            sys.exit("Source IP, user, and password are required for dumping Zabbix data")
        source_conn_string = f"dbname='zabbix' user='{args.source_user}' host='{args.source}' password='{args.source_pass}' port='{args.source_port}' "
        source_conn = psycopg2.connect(source_conn_string)
        source_conn.readonly=True
        scur = source_conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        for table in table_list:
            try:
                select_data(scur, table, action)
            except:
                continue
        
        scur.close()
        print("Saved source data to files")

        
    elif args.load:
        del_tables = table_list.copy()
        del_tables.reverse()
        action = "load"
        if not args.dest or not args.dest_user or not args.dest_pass:
            sys.exit("Destination IP, user, and password are required for loading Zabbix data")
        dest_conn_string = f"dbname='zabbix' user='{args.dest_user}' host='{args.dest}' password='{args.dest_pass}' port='{args.dest_port}'"
        dest_conn = psycopg2.connect(dest_conn_string)
        dcur = dest_conn.cursor()
        for table in del_tables:
            delete_data(dcur, table, action)
        for table in table_list:
            select_data(dcur, table, action)
    else:
        sys.exit(f"Please select either --dump to backup zabbix data, or --load to copy into new databaes.")
        



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", help="Save table data to external file for import in new database", action="store_true")
    parser.add_argument("--load", help="Load table data from external file into new database", action="store_true")
    parser.add_argument("--source", help="The IP address of the source database")
    parser.add_argument("--source-port", help="The Postgresql port of the source database if not the default 5432", default=5432)
    parser.add_argument("--source-user", help="The zabbix user name of the source database")
    parser.add_argument("--source-pass", help="The source database user's password")
    parser.add_argument("--dest", help="The IP address of the destination database")
    parser.add_argument("--dest-port", help="The Postgresql port of the destination database if not the default 5432", default=5432)
    parser.add_argument("--dest-user", help="The zabbix user name of the destination database")
    parser.add_argument("--dest-pass", help="The destination database user's password")
    
    args = parser.parse_args()
    if args.dump and args.load:
        print("Both dump and load are selected. Please choose only one")
        sys.exit()
    main(args)