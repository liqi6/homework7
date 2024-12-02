import streamlit as st
import leafmap.foliumap as leafmap

m = leafmap.Map(center=[23.5,121], zoom=7, minimap_control=True)
data = "https://raw.githubusercontent.com/liqi6/homework7/refs/heads/main/C-B0074-001.json"
m.add_points_from_xy(
  data,
  x="StationLongitude",
  y="StationLatitude",
  icon_names=["StationName", "status", "CountyName","Location"],
  spin=True,
    )
m.to_streamlit(height=500)
