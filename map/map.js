import { drawProductsMap } from "./productsMap.js";
import {drawDepartamentMap} from './departmentMap.js'
import {drawSubordinationMap} from './subordinationMap.js'
// Создаем карту Leaflet
export var map = L.map('map').setView([51.505, -0.09], 4);

changer_expand = false

map.setMinZoom(4);
map.setMaxZoom(13);

// Создаем пустой слой
var emptyLayer = L.tileLayer('', {
    attribution: 'Empty Map'
}).addTo(map);

drawSubordinationMap()

$(document).ready(function () {
    $(".inText").click(function () {
        console.log("iii")
        if (changer_expand) {
            changer_expand = false;
        }
        else{
            changer_expand = true;
            $("#map_changer").css("height", "20vh")
        }
    });
});

$(document.getElementsByClassName("leaflet-control-attribution leaflet-control")).remove();

window.addEventListener("click", function (e) {
    console.log(e);
    if ($(e.target).hasClass("custom-cluster-icon")){
        console.log('Нажатие на иконку:', e.target);
    } else if ($(e.target).hasClass("teamCircle")) {
        console.log('Нажатие на иконку:', e.target);

    } else if ($(e.target).hasClass("cityCircle")) {
        console.log('Нажатие на иконку:', e.target);
    }
    el = e.target;
    if ($(el).attr("id") == "toMyCab"){
        console.log("ggg");
        window.location.href = "../index.html";
    }
});
