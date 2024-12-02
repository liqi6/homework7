import streamlit as st
import leafmap.foliumap as leafmap

m = leafmap.Map(center=[23.5,121], zoom=7, minimap_control=True)
data = "https://raw.githubusercontent.com/liqi6/homework7/refs/heads/main/nos_p_08.csv"
m.add_points_from_xy(
  data,
  x="longitude",
  y="latitude",
  icon_names=["county", "recordtype", "stationname","noisetype","address"],
  spin=True,
    )
m.to_streamlit(height=500)
