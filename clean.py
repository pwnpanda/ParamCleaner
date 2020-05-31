import sys
import re
import urllib.parse as urlparse
from urllib.parse import parse_qs as pq


unique = {}
# unique {
#    base_url: [
#        url-1,
#        url-2
#    ],
#}

def readfile(infile):
    lines = 0
    with open(infile, "r") as file:
        #print(F"file: {infile}")
        #line = file.readline().strip()
        for line in file:
            line = line.strip()
            if not line:
                continue
            lines += 1
            #print(F"Line: {line}")
            if "?" in line:
                base = line.split("?")[0]
                # add base url
                if base not in unique:
                    unique[base] = []
                
                # Parse new url
                parsed_url = urlparse.urlparse(line)
                params = pq(parsed_url.query)
                
                # If no values in the array
                if not unique[base]:
                    unique[base].append(line)
                    #print("Valid and first entry")
                else:
                    # if found once, do not add. if never found, add
                    not_found = True
                    # Loop through old results
                    for url in unique[base]:
                        old_params = pq(urlparse.urlparse(url).query)
                        # If found, continue without adding
                        old_list = list(old_params.keys())
                        old_list.sort()
                        new_list = list(params.keys())
                        new_list.sort()
                        #print(F"Old params: {old_params} list: {list(old_params.keys())} sorted: {old_list}")
                        #print(F"Old: {old_list} New: {new_list} Equal: {old_list == new_list}")
                        # Good debug
                        #print(F"Difference: {set(old_list).symmetric_difference(set(new_list))}")
                        if old_list == new_list:
                            #print(F"[-] Exists!")
                            not_found = False
                            break
                    # Not found in whole dict, add!
                    if not_found:
                        #print(F"[+] Add line: {line}")
                        unique[base].append(line)
            # Continue reading
            line = file.readline().strip()
    return lines


if len(sys.argv) > 1:
    #print(sys.argv)
    filename = sys.argv[1]
    org_len = readfile(filename)
    #print(F"Results: {unique}")
    
    new_len = 0
    with open(".".join(filename.split(".")[:-1]) + "_clean." + filename.split(".")[-1], "w") as tofile:
        for url in unique:
            tofile.write('\n'.join(unique[url]) + '\n')
            new_len += len(unique[url])
    print(F"Original length: {org_len} - New length: {new_len} = Removed {org_len-new_len} duplicates")
