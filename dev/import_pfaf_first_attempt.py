#! /usr/bin/env python

def swap_dict(a_dict):
    return dict([(v,k) for (k,v) in a_dict.items()])

def db_login():
    db_details = coop.settings.DATABASES['default']
    print db_details
    dbname = db_details['NAME']
    host = db_details['HOST']
    usr = db_details['USER']
    password = db_details['PASSWORD']
    import psycopg2
    connect = "dbname="+dbname+" host="+host+" user="+usr+" password="+password+""
    print connect
    try:
        conn = psycopg2.connect("dbname="+dbname+" host="+host+" user="+usr+" password="+password+"")
    except:
        print "Unable to connect to the database."
    cur = conn.cursor()
    return conn, cur

def csv_to_dict(csvfile, mapping):
    import csv
    print "mapping:"
    print mapping
    file = open(csvfile)
    dialect = csv.Sniffer().sniff(file.read())
    file.seek(0)
    reader = csv.reader(file, dialect)
    headers = reader.next()
    print "headers:"
    print headers
    mapped_headers = []
    for header in headers:
        if mapping.keys().count(header) > 0: mapped_headers.append(mapping[header])
    print "mapped headers:"
    print mapped_headers
    #rowdicts = [dict(zip(mapped_headers, row)) for row in reader if row[0] != '']
    rowdicts = [dict(zip(mapped_headers, row)) for row in reader]
    return rowdicts

def insert_dictionary(d, conn, cur, table):
    print d
    existing = 0
    inserts = 0
    rec_id= None
    fields = ', '.join(d.keys())
    values = ', '.join(['%%(%s)s' % rec for rec in d])
    rec_id = in_table(d, conn, cur, fields, values, table)
    if not rec_id : 
        query = 'INSERT INTO '+table+' (%s) VALUES (%s) RETURNING id;' % (fields, values)
        print(query, d)
        cur.execute(query, d)
        rec_id = cur.fetchone()[0]
        inserts += 1
    else:
        existing += 1
    print str(inserts) +" records added. "+ str(existing)+" already in database."
    return rec_id, inserts, existing

def insert_products(rowdicts, table):
    s_details, s_type, s_address  = get_source_details() 
    conn, cur = db_login()
    inserts = 0
    existing = 0
    pid = None
    for d in rowdicts:
        pid, i, e = insert_dictionary(d, conn, cur, table)
        inserts += i
        existing += e
        if conn: conn.commit()
        # insert into source_products
        global SOURCE_ID
        if not SOURCE_ID:
            print "NO SOURCE"
            exit()
        conn, cur = db_login()
        join_table = "coop_web_"+s_type+"_products"
        ids = {s_type+'_id': SOURCE_ID, 'product_id': pid}
        source_pid, i, e = insert_dictionary(ids, conn, cur, join_table)
        print "JOIN TABLE ID: "+str(source_pid)
        if conn: conn.commit()
    print str(inserts) +" records added. "+ str(existing)+" already in database."
    cur.close()
    conn.close()

def in_table(rec, conn, cur, fields, values, table):
    if not fields and not values:
        print "no values"
        return True;
    else:
        query = 'SELECT id FROM '+table+' WHERE (%s) = (%s)' % (fields, values)
        if DEBUG: print(query, rec)
        cur.execute(query, rec)
        res = cur.fetchone()
        sql = cur.mogrify(query, rec)
        if DEBUG: print str(sql)+"\n||"
        if DEBUG: print str(res)+"\n\n"
        if not res:
            return False 
        else:
            return res[0]

if __name__ == '__main__':
    import sys
    # update = False
    if len(sys.argv) > 1: csvfile = sys.argv[1]
    else:
        print "You must provide a csv file for processing."
        exit()
    mapping = swap_dict(SETTINGS_MODULE.CSV_HEADER_MAPPING)
    rowdicts = csv_to_dict(csvfile, mapping)
    insert_products(rowdicts, "pdt_product")
