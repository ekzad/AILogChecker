import random
from datetime import datetime, timedelta
# NOTE: This whole script is just for creating fake logs to test out the application. if you're trying to test this thing out, go ahead and generate logs with this script

def random_timestamp(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

start = datetime(2026, 1, 1)
end = datetime(2026, 12, 31)

def generate(m):
    log_type = random.choice(['failed_login', 'port_scan', 'firewall_deny', 'potential_exploiting'])
    if log_type == 'failed_login':
        raw = 'An authentication attempt failed, likely due to an incorrect username/password or unauthorized access attempt.'
    elif log_type == 'port_scan':
        raw = 'A host probed multiple network ports to discover open services that could be targeted.'
    elif log_type == 'firewall_deny':
        raw = 'The firewall blocked a connection because it violated a security rule or policy.'
    elif log_type == 'potential_exploiting':
        raw = 'Activity matched patterns suggesting an attacker may be attempting to exploit a known vulnerability or system weakness.'
    ts=random_timestamp(start,end)
    log = {
        'log_num': m,
        'timestamp': ts.strftime("%Y-%m-%d %H:%M:%S"),
        'source_ip': f'19{random.randint(2,9)}.1{random.randint(1,9)}{random.randint(1,9)}.{random.randint(1,40)}.{random.randint(1,40)}',
        'log_type': log_type,
        'raw_log': raw
    }
    print(log)
    return log
if __name__ == '__main__':
    n = 0
    m = 0
    with open("logs.txt", "w") as f:
        while n < 10:
            m += 1
            n += 1
            log = generate(m)
            f.write(str(log) + "\n")