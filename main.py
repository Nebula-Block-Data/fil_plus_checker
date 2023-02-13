import json
import subprocess
import asyncio
import sys
import time


deal_id = sys.argv[1]
time_str = time.strftime("%Y%m%d-%H%M%S")

get_deal_cmd = ['lotus', 'state', 'get-deal', str(deal_id)]

result = subprocess.run(get_deal_cmd, stdout=subprocess.PIPE)
result = json.loads(result.stdout)
piece_CID = result["Proposal"]['PieceCID']["/"]
label = result["Proposal"]['Label']
provider = result["Proposal"]['Provider']
output_file = time_str + ".file"
print(piece_CID, label, provider)

deal_log = 'log/'+str(deal_id) + '.log'
get_retrieve_cmd = ['lotus', 'client', 'retrieve', '--provider', str(provider), '--pieceCid', str(piece_CID), label,
                    str(output_file), '>>', deal_log]

f = open(deal_log, "a")
f.write(" ".join(get_retrieve_cmd))
f.close()

print(get_retrieve_cmd)

result = subprocess.Popen(" ".join(get_retrieve_cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

f = open(deal_log, "ab")
f.write(result.stderr.readline())
f.close()

print(result.stderr.readline())
