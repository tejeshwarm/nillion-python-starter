#Securely calculating the top-performing salesperson in multiple regions based on their sales figures. This is useful for companies to determine the best salespeople while keeping individual sales data confidential.

"""
Secure Top-Performing Salesperson Calculation
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
    ## Find top salesperson in each region
    top_sales_r0 = max(r0_s0_sales, r0_s1_sales)
    top_sales_r1 = max(r1_s0_sales, r1_s1_sales)
    top_sales_r2 = max(r2_s0_sales, r2_s1_sales)
    
    ## Find the overall top salesperson
    top_sales_overall = max(top_sales_r0, top_sales_r1, top_sales_r2)

    # 4. Output
    top_sales_r0_output = Output(top_sales_r0, "top_sales_region0", outparty)
    top_sales_r1_output = Output(top_sales_r1, "top_sales_region1", outparty)
    top_sales_r2_output = Output(top_sales_r2, "top_sales_region2", outparty)
    top_sales_overall_output = Output(top_sales_overall, "top_sales_overall", outparty)

    return [top_sales_r0_output, top_sales_r1_output, top_sales_r2_output, top_sales_overall_output]

# Hence the program ensures the security of the confidential data. Security is not a product, but a process and here it is achieved through secret data type.