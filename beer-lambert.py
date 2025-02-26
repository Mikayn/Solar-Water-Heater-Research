import numpy as np

def main():
    # Conditions to evaluate
    conditions = [
        "Clear", "Lightly Cloudy", "Mostly Cloudy", "Overcast",
        "Mostly Cloudy (Rain)", "Fog",
        "Fog until 9 then Cloudy", "Fog until 9 then Clear",
        "Fog until 10 then Cloudy", "Fog until 10 then Clear",
        "Fog until 11 then Cloudy", "Fog until 11 then Clear",
        "Fog until 12 then Cloudy", "Fog until 12 then Clear",
        "Fog then Rain", "Overcast (Rain)"
    ]

    # Compute values for each condition
    results = {cond: estimate_transmittance_absorption(cond) for cond in conditions}
    
    # Print results
    for cond, (absorp, trans) in results.items():
        print(f"{cond}: Absorption = {absorp}, Transmittance = {trans}")

def beer_lambert_transmittance(tau):
    """Calculate transmittance using the Beer-Lambert Law."""
    return np.exp(-tau)

def estimate_transmittance_absorption(condition, tau_clear = 0.2, tau_cloud = 0.65, tau_fog = 0.7):
    """Estimate transmittance and absorption based on weather condition."""
    if condition == "Clear":
        tau = tau_clear
    elif condition == "Lightly Cloudy":
        tau = tau_clear + 0.3
    elif condition == "Mostly Cloudy":
        tau = tau_cloud + 0.3
    elif condition == "Overcast":
        tau = tau_cloud * 2
    elif condition == "Mostly Cloudy (Rain)":
        tau = tau_cloud * 2
    elif condition == "Overcast (Rain)":
        tau = tau_cloud * 2 + 0.5
    elif "Fog" in condition:  # Check for any fog condition
        # Adjust tau based on time mentioned in condition
        try:
            time_str = condition.split(" ")[2]  # Extract the time 

            if time_str.isdigit() and "Clear" in condition:
                time_hour = int(time_str)
                tau = tau_fog + (time_hour - 9) * 0.1 - tau_clear  #Subtracting because more transmission

            elif time_str.isdigit() and "Cloudy" in condition:
                time_hour = int(time_str)
                tau = tau_fog + (time_hour - 9) * 0.1 + tau_clear #Adding because less transmission

            elif "Rain" in condition:
                tau = tau_fog + 0.5 #Rain constant 0.5 

            else:
                tau = tau_fog

        except IndexError:
            tau = tau_fog + 0.4

    else:
        raise ValueError("Unknown condition")
    
    transmittance = beer_lambert_transmittance(tau)
    absorption = 1 - transmittance
    return round(absorption, 3), round(transmittance, 3)

if __name__ == "__main__":
    main()