import { drawProductsMap } from "./productsMap.js";
import {drawDepartamentMap} from './departmentMap.js'
import {drawSubordinationMap} from './subordinationMap.js'
// Создаем карту Leaflet
export var map = L.map('map').setView([51.505, -0.09], 4);

map.setMinZoom(4);
map.setMaxZoom(13);

// Создаем пустой слой
var emptyLayer = L.tileLayer('', {
    attribution: 'Empty Map'
}).addTo(map);

drawSubordinationMap()



$(document.getElementsByClassName("leaflet-control-attribution leaflet-control")).remove();