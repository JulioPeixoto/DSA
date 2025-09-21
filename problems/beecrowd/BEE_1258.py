import sys
from typing import NamedTuple, List

class ShirtOrder(NamedTuple):
    color: str
    size_value: int
    name: str

def process_shirt_orders(data: List[str]) -> List[str]:
    output_lines = []
    
    index = 0
    first_case = True
    while index < len(data):
        N = int(data[index])
        if N == 0:
            break
        index += 1
        
        orders = []
        for _ in range(N):
            name = data[index].strip()
            index += 1
            color_size = data[index].strip().split()
            index += 1
            color = color_size[0]
            size = color_size[1]
            size_value = {'P': 1, 'M': 2, 'G': 3}[size]
            orders.append(ShirtOrder(color, size_value, name))
        
        orders.sort(key=lambda x: (x.color, x.size_value, x.name))
        
        if not first_case:
            output_lines.append("")
        first_case = False
        
        for order in orders:
            size_str = {1: 'P', 2: 'M', 3: 'G'}[order.size_value]
            output_lines.append(f"{order.color} {size_str} {order.name}")
            
    return output_lines

if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    result_lines = process_shirt_orders(input_data)
    for line in result_lines:
        print(line)
