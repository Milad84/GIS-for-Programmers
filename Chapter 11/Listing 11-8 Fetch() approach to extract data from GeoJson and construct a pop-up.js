fetch("data/TexCounty.geojson")
.then(function(response) {
return response.json();
})
.then(function(data) {
L.geoJSON(data, {
style: stat_style,
onEachFeature: function(feature, layer) {
layer.bindPopup(feature.properties.namelsad);
}
}).addTo(map);
});
