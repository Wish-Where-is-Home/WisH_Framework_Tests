import './ndpage.css';
import { useLocation } from "react-router-dom";
import "leaflet/dist/leaflet.css";
import { MapContainer, TileLayer, GeoJSON, useMapEvents } from 'react-leaflet';
import React from "react";
import portugalGeoJSON from '../../GeoJsons/portugal.json';


const Ndpage = ({darkMode}) => {
    const location = useLocation();
    const selectedDistrict = location.state.selectedDistrict;
    console.log('Ndpage selected ', selectedDistrict);


    const portugalBounds = [
        [36.9, -9.5], // Southwest coordinates of Portugal
        [42.2, -6.5]  // Northeast coordinates of Portugal
      ];

    return (
        <div className={`home-section ${darkMode ? 'dark-mode' : 'light-mode'}`}>
            <div className='ndpage-container'> 
                <div className='questionaire'>

                </div>
                <div className='mapp'>
                    <MapContainer
                            style={{ height: "100%", width: "100%",zIndex:"22" }}
                            center={[40.6412,  -8.65362]}
                            zoom={9}
                            minZoom={9}
                            maxBounds={portugalBounds}
                        >
                            <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        />
                            <GeoJSON
                                data={portugalGeoJSON}
                                style={() => ({
                                    fillColor: "transparent",
                                    fillOpacity: 0.5,
                                    color: "black",
                                    weight: 1,
                                })}
                            />
                            
                        </MapContainer>
                </div>
            </div>
        </div>
    );
};

export default Ndpage;
