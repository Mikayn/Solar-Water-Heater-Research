import math, datetime

def main():

    theta = calculations()
    print("\n".join(map(str, theta)))

def calculations():  
    # Given values
    latitude = 27  # Latitude of Kathmandu
    phi = math.radians(latitude)  # Latitude in radians

    startDate = datetime.datetime(2024,11,1)
    endDate = datetime.datetime(2025,2,1)

    date = startDate

    hour_angle = 0

    theta = []

    while date <= endDate:
        
        ordinal_day = date.timetuple().tm_yday

        solar_declination = 23.44 * math.sin(math.radians((360/365) * (ordinal_day - 81)))  # Solar declination formula
        delta = math.radians(solar_declination)  # Solar declination in radians

        # Calculate Solar Zenith Angle using the formula
        # cos(theta) = sin(phi) * sin(delta) + cos(phi) * cos(delta) * cos(H)

        # Calculate cosine of solar zenith angle
        cos_theta = math.sin(phi) * math.sin(delta) + math.cos(phi) * math.cos(delta) * math.cos(math.radians(hour_angle))

        # Calculate solar zenith angle
        theta.append(round(math.degrees(math.acos(cos_theta)),3))

        date += datetime.timedelta(days=1)
    
    return theta

if __name__ == "__main__":
    main()