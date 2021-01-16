import numpy as np

# vehicle assumptions
avg_speed_uam = 120/60 # km/min
avg_pax_per_trip = 2.5

# UAM CONOPS:
time_board = 5 # min
time_deboard = 2 # min

# VTTS
VTTS_personal = 0.35 # we can change this to 0.35
VTTS_business = 0.80
working_minutes_per_yr = 2080 * 60




# CHANGES ARE NECESSARY ONLY IN GET_PKT (TOTAL PKM and mu and sigma for income)

# EU commuter data source: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC83304/tch-d2.1_final.pdf