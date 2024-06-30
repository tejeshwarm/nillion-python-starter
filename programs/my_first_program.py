# Securely calculating the average sales in multiple regions based on individual sales figures.
# This is useful for companies to determine regional and overall sales performance while keeping individual sales data confidential.

"""
Secure Average Sales Calculation
nr of regions: r = 3
nr of salespersons per region: s = 2
"""

from nada_dsl import *

def nada_main():

    # 1. Parties initialization
    region0 = Party(name="Region0")
    region1 = Party(name="Region1")
    region2 = Party(name="Region2")
    outparty = Party(name="OutParty")

    # 2. Inputs initialization
    ## Sales figures from region 0 salespersons
    r0_s0_sales = SecretUnsignedInteger(Input(name="r0_s0_sales", party=region0))
    r0_s1_sales = SecretUnsignedInteger(Input(name="r0_s1_sales", party=region0))
    
    ## Sales figures from region 1 salespersons
    r1_s0_sales = SecretUnsignedInteger(Input(name="r1_s0_sales", party=region1))
    r1_s1_sales = SecretUnsignedInteger(Input(name="r1_s1_sales", party=region1))

    ## Sales figures from region 2 salespersons
    r2_s0_sales = SecretUnsignedInteger(Input(name="r2_s0_sales", party=region2))
    r2_s1_sales = SecretUnsignedInteger(Input(name="r2_s1_sales", party=region2))

    # 3. Computation
    ## Calculate total sales for each region
    total_sales_r0 = r0_s0_sales + r0_s1_sales
    total_sales_r1 = r1_s0_sales + r1_s1_sales
    total_sales_r2 = r2_s0_sales + r2_s1_sales

    ## Calculate the number of salespersons in each region
    num_salespersons_per_region = Integer(2)  # Since each region has 2 salespersons

    ## Calculate average sales for each region
    avg_sales_r0 = total_sales_r0 / num_salespersons_per_region
    avg_sales_r1 = total_sales_r1 / num_salespersons_per_region
    avg_sales_r2 = total_sales_r2 / num_salespersons_per_region

    ## Calculate the overall total sales
    overall_total_sales = total_sales_r0 + total_sales_r1 + total_sales_r2

    ## Calculate the overall number of salespersons
    overall_num_salespersons = Integer(3) * num_salespersons_per_region  # 3 regions, each with 2 salespersons

    ## Calculate the overall average sales
    overall_avg_sales = overall_total_sales / overall_num_salespersons

    # 4. Output
    avg_sales_r0_output = Output(value=avg_sales_r0, name="avg_sales_region0", party=outparty)
    avg_sales_r1_output = Output(value=avg_sales_r1, name="avg_sales_region1", party=outparty)
    avg_sales_r2_output = Output(value=avg_sales_r2, name="avg_sales_region2", party=outparty)
    overall_avg_sales_output = Output(value=overall_avg_sales, name="overall_avg_sales", party=outparty)

    return [avg_sales_r0_output, avg_sales_r1_output, avg_sales_r2_output, overall_avg_sales_output]

# Hence the program ensures the security of the confidential data. Security is not a product, but a process and here it is achieved through secret data type.