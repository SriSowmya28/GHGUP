import streamlit as st
import pandas as pd

# Define emission factors (in eqmton per unit)
emission_factors = {
    'coal': 2.86,  # for coal in mton
    'biomass': 0.06,  # for biomass in mton
    'natural_gas': 0.0053,  # for natural gas in mmBTU
    'diesel_oil': 0.0027,  # for diesel oil in liters
    'ch4_coal': 0.0003,  # for CH4 emissions per mton of coal burned
    'ch4_biomass': 0.0002,  # for CH4 emissions per mton of biomass burned
    'ch4_natural_gas': 0.0001,  # for CH4 emissions per mmBTU of natural gas burned
    'ch4_diesel_oil': 0.00015,  # for CH4 emissions per liter of diesel oil burned
    'n2o_coal': 0.00005,  # for N2O emissions per mton of coal burned
    'n2o_biomass': 0.00004,  # for N2O emissions per mton of biomass burned
    'n2o_natural_gas': 0.00002,  # for N2O emissions per mmBTU of natural gas burned
    'n2o_diesel_oil': 0.00003  # for N2O emissions per liter of diesel oil burned
}

# Streamlit UI elements
st.title("GHG Emissions Calculator")
st.write("This app calculates greenhouse gas emissions from various fuel sources.")

# Input fields for user data
coal_mton = st.number_input("Enter coal in mton:", min_value=0.0)
biomass_mton = st.number_input("Enter biomass in mton:", min_value=0.0)
natural_gas_mmbtu = st.number_input("Enter natural gas in mmBTU:", min_value=0.0)
diesel_oil_liters = st.number_input("Enter diesel oil in liters:", min_value=0.0)

# Calculate GHG emissions
if st.button("Calculate"):
    ghg_coal = coal_mton * emission_factors['coal']
    ghg_biomass = biomass_mton * emission_factors['biomass']
    ghg_natural_gas = natural_gas_mmbtu * emission_factors['natural_gas']
    ghg_diesel_oil = diesel_oil_liters * emission_factors['diesel_oil']

    # Calculate CH4 emissions based on fuel burn
    ghg_ch4_coal = coal_mton * emission_factors['ch4_coal']
    ghg_ch4_biomass = biomass_mton * emission_factors['ch4_biomass']
    ghg_ch4_natural_gas = natural_gas_mmbtu * emission_factors['ch4_natural_gas']
    ghg_ch4_diesel_oil = diesel_oil_liters * emission_factors['ch4_diesel_oil']

    # Calculate N2O emissions based on fuel burn
    ghg_n2o_coal = coal_mton * emission_factors['n2o_coal']
    ghg_n2o_biomass = biomass_mton * emission_factors['n2o_biomass']
    ghg_n2o_natural_gas = natural_gas_mmbtu * emission_factors['n2o_natural_gas']
    ghg_n2o_diesel_oil = diesel_oil_liters * emission_factors['n2o_diesel_oil']

    # Total GHG emissions
    total_ghg = (ghg_coal + ghg_biomass + ghg_natural_gas + ghg_diesel_oil + 
                  ghg_ch4_coal + ghg_ch4_biomass + ghg_ch4_natural_gas + ghg_ch4_diesel_oil +
                  ghg_n2o_coal + ghg_n2o_biomass + ghg_n2o_natural_gas + ghg_n2o_diesel_oil)

    # Prepare results for tabulation
    results = {
        "Source": [
            "Coal", "Biomass", "Natural Gas", "Diesel Oil",
            "CH4 (Coal)", "CH4 (Biomass)", "CH4 (Natural Gas)", "CH4 (Diesel Oil)",
            "N2O (Coal)", "N2O (Biomass)", "N2O (Natural Gas)", "N2O (Diesel Oil)",
            "Total GHG Emissions"
        ],
        "GHG Emissions (eqmton)": [
            ghg_coal, ghg_biomass, ghg_natural_gas, ghg_diesel_oil,
            ghg_ch4_coal, ghg_ch4_biomass, ghg_ch4_natural_gas, ghg_ch4_diesel_oil,
            ghg_n2o_coal, ghg_n2o_biomass, ghg_n2o_natural_gas, ghg_n2o_diesel_oil,
            total_ghg
        ]
    }

    # Create DataFrame for results
    results_df = pd.DataFrame(results)

    # Display the results in tabulated form
    st.write("\nGHG Emissions Calculation Results")
    st.table(results_df)

    # Company name and developer information
    st.write("\nCompany: NIMIR")
    st.write("Developed by: mak3.11")

