target_distance = 3.0
throw_strength = 2.0
learning_rate = 0.2
input_strength = 1.0
num_throws = 30

print("Step | Distance | Error | Change | New Strength")
print("-" * 55)

for step in range(1, num_throws + 1):
    
    current_distance = throw_strength * 1.5
    
    error = target_distance - current_distance
    
    delta_w = learning_rate * error * input_strength
    

    throw_strength += delta_w
    
    print(f"{step:^4} | {current_distance:^9.2f} | {error:^6.2f} | {delta_w:^6.2f} | {throw_strength:^12.2f}")

    if abs(target_distance - current_distance) < 0.01:
        break
