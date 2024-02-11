def C_Radio_Station(n, m, n_lines, m_lines):
    ip_name = {}
    for line in n_lines:
        name, ip = line.split()  
        ip_name[ip] = name
    result = []
    for line in m_lines:
        command, ip = line.strip(";").split()
        result.append(f"{command} {ip}; #{ip_name[ip]}")
    return result
        
n, m = map(int, input().strip().split())
n_lines = [input().strip() for _ in range(n)]
m_lines = [input().strip() for _ in range(m)]

result = C_Radio_Station(n, m, n_lines, m_lines)

for line in result:
    print(line)
