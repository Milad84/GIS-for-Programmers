<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Simple Web Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js">
</script>
    <style>
        /* Set the map's dimensions */
        #map {
            width: 100%;
            height: 400px;
        }
    </style>
</head>
<body>

<div id="map"></div>

<script>
    
    var map = L.map('map').setView([51.505, -0.09], 13); 
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var marker = L.marker([51.505, -0.09]).addTo(map)
        .bindPopup('Hello, I am a marker!').openPopup();
</script>

</body>
</html>

