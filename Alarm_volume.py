#Paramters
target_volume = 80.0
current_volume = 60.0
learning_rate = 0.3
input_knob = 1.0
num_adjustments = 30
tolerance = 0.1

print("Step | Alarm Volume | Error | Adjustment")
print("-" * 50)

for step in range(1, num_adjustments + 1):
    
    error = target_volume - current_volume
    adjustment = learning_rate * error * input_knob
    current_volume += adjustment
    
    print(f"{step:^4} | {current_volume:^12.2f} | {error:^6.2f} | {adjustment:^9.2f}")
    
    if abs(error) < tolerance:
        break
