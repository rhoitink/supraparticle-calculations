import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()


st.write("# Supraparticle calculators")
col1, col2 = st.columns(2)

with col1:
    st.write("## Input")
    d_particle = st.number_input("Particle diameter (nm)", 1, 5000, 300)
    d_droplet = st.number_input("Diameter of the droplet (µm)", np.ceil(d_particle/1000.).astype(int), 1000, 100)
with col2:
    st.write("## Volume fractions")
    phi_i = st.number_input("Initial volume fraction", 0.001, .99, 0.03, format="%.3f")
    phi_f = st.number_input("Final volume fraction", phi_i, 1.0, 0.688, format="%.3f")

st.write("---")
st.write("## Output")
d_droplet_um = d_droplet  * ureg.µm
d_particle_nm = d_particle * ureg.nm

V_particle = np.pi / 6 * d_particle_nm**3
V_droplet = np.pi / 6 * d_droplet_um**3

N_particle = phi_i * V_droplet / V_particle
V_droplet_final = N_particle * V_particle/phi_f
d_droplet_final = (6 * V_droplet_final / np.pi)**(1/3)

st.write(f"### Number of particles: {N_particle.to(ureg.dimensionless).magnitude:.0f}")
st.write(f"### Final droplet diameter: {d_droplet_final.to(ureg.µm).magnitude:.3f} µm")
