def min_energy(t, cases):
    for case in cases:
        n, x1, y1, x2, y2 = case
        
        
        layer1 = min(x1 - 1, y1 - 1, n - x1, n - y1)
        layer2 = min(x2 - 1, y2 - 1, n - x2, n - y2)
        
        
        dist_between_layers = abs(layer2 - layer1)
        
        energy_required = dist_between_layers
        print(energy_required)


t = int(input().strip())


cases = []
for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().strip().split())
    cases.append((n, x1, y1, x2, y2))


min_energy(t, cases)
