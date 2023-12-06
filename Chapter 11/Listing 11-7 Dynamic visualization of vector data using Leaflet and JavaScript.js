var map = L.map("map").setView([28.8882080, -97.939990], 15);

var osm =  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var OpenStreetMap_DE = L.tileLayer(
'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var OpenStreetMap_BZH = L.tileLayer('https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles courtesy of 
<a href="http://www.openstreetmap.bzh/" target="_blank">Breton OpenStreetMap Team</a>',
	
});

osm.addTo(map);

var baseLayer = {
  "osm": osm,
  "OpenStreetMap_DE": OpenStreetMap_DE,
  "OpenStreetMap_BZH": OpenStreetMap_BZH,
};

var geojson  = L.geoJSON(TexCounty, {
  onEachFeature: function(feature, layer) {
   var County = feature.properties.namelsad;
    layer.bindPopup(`<h3>County: ${County}</h3>`)
  },
  style: {
    color:"red",
    fillColor: "yellow",
    fillOpacity: 0.2,

  }
}).addTo(map);

map.fitBounds(geojson.getBounds())
 

var overlayers = {
  "geojson Layer": geojson,
};

L.control.layers(baseLayer, overlayers).addTo(map);
