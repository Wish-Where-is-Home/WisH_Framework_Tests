import React, { useState } from 'react';
import './App.css';
import "leaflet/dist/leaflet.css";
import { MapContainer, TileLayer, GeoJSON, useMapEvents } from 'react-leaflet';

import portugalGeoJSON from './GeoJsons/portugal.json';
import spainGeoJson from './GeoJsons/spain.json';
import franceGeoJson from './GeoJsons/france.json';
import moroccoGeoJson from './GeoJsons/morocco.json';
import algeriaGeoJson from './GeoJsons/algeria.json';
import DistrictsPortugalJson from './GeoJsons/DistrictsPortugal.json';

function App() {
  const portugalBounds = [
    [36.9, -9.5], // Southwest coordinates of Portugal
    [42.2, -6.5]  // Northeast coordinates of Portugal
  ];

  const [coordinates, setCoordinates] = useState({ lat: 0, lng: 0 });
  const [districtName, setDistrictName] = useState("");

  const handleMouseMove = (e) => {
    setCoordinates(e.latlng);
  };

  const handleDistrictHover = (e) => {
    const districtName = e.target.feature.properties.name;
    setDistrictName(districtName);
  };
  
  const handleDistrictHoverOut = () => {
    setDistrictName("");
  };

  return (
    <div className="App">
      <MapContainer
        center={[39.69450171944444,-8.130572855555556]} 
        zoom={7} 
        minZoom={7} 
        maxBounds={portugalBounds} 
        maxBoundsViscosity={1}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        />
        <MousePositionUpdater setCoordinates={setCoordinates} />

        <GeoJSON
          data={portugalGeoJSON}
          style={() => ({
            color: "black", 
            fillColor: "transparent",
            weight: 3, 
            fillOpacity: 0.2, 
          })}
        />

        <GeoJSON
          data={DistrictsPortugalJson}
          style={() => ({
            color: "black", 
            fillColor: "transparent",
            weight: 1, 
            fillOpacity: 0.5, 
          })}
          onEachFeature={(feature, layer) => {
            layer.on({
              mouseover: handleDistrictHover,
              mouseout: handleDistrictHoverOut
            });
          }}
        />

        {[
          { data: spainGeoJson, color: "gray" },
          { data: franceGeoJson, color: "gray" },
          { data: moroccoGeoJson, color: "gray" },
          { data: algeriaGeoJson, color: "gray" }
        ].map((country, index) => (
          <GeoJSON
            key={index}
            data={country.data}
            style={() => ({
              color: country.color,
              fillColor: country.color,
              weight: 1,
              fillOpacity: 0.8,
            })}
          />
        ))}
      </MapContainer>

      <div>
        <p>Latitude: {coordinates.lat.toFixed(5)}, Longitude: {coordinates.lng.toFixed(5)}</p>
        <p>District: {districtName}</p>

      </div>
    </div>
  );
}

function MousePositionUpdater({ setCoordinates }) {
  useMapEvents({
    mousemove: (e) => {
      setCoordinates(e.latlng);
    },
  });

  return null;
}

export default App;
