mapboxgl.accessToken = 'pk.eyJ1IjoibWF0dGhld211cmllbDc4IiwiYSI6ImNsdjAxOWd2bDBkcW8ya3IzdjAxcmc5ZHkifQ.tcIDC6ucq8VaI5hrik3TFA';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-24, 42]
});

map.addControl(
    new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: false
        },
        // When active the map will receive updates to the device's location as it changes.
        trackUserLocation: true,
    })
);

