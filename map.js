var ourLoc;
var view;
var map;

function init() {
  ourLoc = ol.proj.fromLonLat([-122.347992, 47.648029]);

view = new ol.View({
      center: ourLoc,
      zoom: 4
    })

  map = new ol.Map({
   target: 'map',
   layers: [
     new ol.layer.Tile({
       source: new ol.source.OSM()
     })
   ],
   view
 });
}

function panHome() {
  view.animate({
    center: ourLoc,
    duration: 1000
  });
}
window.onload = init;
