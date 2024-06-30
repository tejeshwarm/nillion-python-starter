# Securely computing the average temperature readings from different sensors in various locations.
# This can help organizations analyze environmental data while preserving the privacy of individual sensor readings.

"""
Secure Average Temperature Calculation
no.of.locations: l = 3
no.of.sensors per location: s = 2
"""

from nada_dsl import *

def nada_main():

    # 1. Parties initialization
    location0 = Party(name="Location0")
    location1 = Party(name="Location1")
    location2 = Party(name="Location2")
    outparty = Party(name="OutParty")

    # 2. Inputs initialization
    ## Temperature readings from location 0 sensors
    l0_s0_temp = SecretFloat(Input(name="l0_s0_temp", party=location0))
    l0_s1_temp = SecretFloat(Input(name="l0_s1_temp", party=location0))
    
    ## Temperature readings from location 1 sensors
    l1_s0_temp = SecretFloat(Input(name="l1_s0_temp", party=location1))
    l1_s1_temp = SecretFloat(Input(name="l1_s1_temp", party=location1))

    ## Temperature readings from location 2 sensors
    l2_s0_temp = SecretFloat(Input(name="l2_s0_temp", party=location2))
    l2_s1_temp = SecretFloat(Input(name="l2_s1_temp", party=location2))

    # 3. Computation
    ## Calculate total temperature and count of sensors for each location
    total_temp_l0 = l0_s0_temp + l0_s1_temp
    total_sensors_l0 = 2
    
    total_temp_l1 = l1_s0_temp + l1_s1_temp
    total_sensors_l1 = 2
    
    total_temp_l2 = l2_s0_temp + l2_s1_temp
    total_sensors_l2 = 2

    ## Calculate average temperature for each location
    avg_temp_l0 = total_temp_l0 / total_sensors_l0
    avg_temp_l1 = total_temp_l1 / total_sensors_l1
    avg_temp_l2 = total_temp_l2 / total_sensors_l2

    ## Calculate overall total temperature and count of sensors
    overall_total_temp = total_temp_l0 + total_temp_l1 + total_temp_l2
    overall_total_sensors = total_sensors_l0 + total_sensors_l1 + total_sensors_l2

    ## Calculate the overall average temperature
    overall_avg_temp = overall_total_temp / overall_total_sensors

    # 4. Output
    avg_temp_l0_output = Output(value=avg_temp_l0, name="avg_temp_location0", party=outparty)
    avg_temp_l1_output = Output(value=avg_temp_l1, name="avg_temp_location1", party=outparty)
    avg_temp_l2_output = Output(value=avg_temp_l2, name="avg_temp_location2", party=outparty)
    overall_avg_temp_output = Output(value=overall_avg_temp, name="overall_avg_temp", party=outparty)

    return [avg_temp_l0_output, avg_temp_l1_output, avg_temp_l2_output, overall_avg_temp_output]