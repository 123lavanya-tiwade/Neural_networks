target_volume=250.0
hand_tilt=10.0
learning_rate=0.01
input_tilt=1.0
num_pours=30
tolerance=0.1

print("Step | Volume | Error | Change | New Tilt")
print("-"*55)

for step in range(1, num_pours+1):
    current_volume = hand_tilt*2
    error=target_volume-current_volume
    delta_w=learning_rate*error*input_tilt
    hand_tilt+=delta_w
    print(f"{step:^4} | {current_volume:^8.2f} | {error:^7.2f} | {delta_w:^7.2f} | {hand_tilt:^9.2f}")

    if abs(error) < tolerance:
        break
    
