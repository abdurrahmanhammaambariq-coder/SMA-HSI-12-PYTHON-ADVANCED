def konversi_suhu (suhu,unit):
    if unit.upper() == "C":
       return (suhu * 9/5) + 32
    elif unit.upper() == "F":
       return (suhu - 32) * 5/9
    
hasil1 = konversi_suhu(30, "C")   # 30°C ke Fahrenheit
hasil2 = konversi_suhu(86, "F")   # 86°F ke Celsius

print(f"30°C sama dengan {hasil1}°F")
print(f"86°F sama dengan {hasil2}°C")

