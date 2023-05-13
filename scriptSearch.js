interests = new Set()
names = new Set()
roles = new Set()

searching = new Set()

last_response = null

$(document).ready(function () {
    getNames();
    getRoles();
    getInterests();
    $("#make_search_btn").click(async function () {
        requestIng = "http://127.0.0.1:5000/find_users_by_name?key=" + generateSearchRequest("names");
        let request = await fetch(requestIng)
        let responseNames = await request.json();
        console.log(requestIng)
        console.log(responseNames)
        requestIng = "http://127.0.0.1:5000/find_users_by_roles?key=" + generateSearchRequest("roles");
        request = await fetch(requestIng)
        let responseRoles = await request.json();
        console.log(requestIng)
        console.log(responseRoles)
    });
});

function addToRoles(par) {
    return roles.has(par)
}

async function getNames() {
    requestIng = "http://127.0.0.1:5000/find_users?key="
    let request = await fetch(requestIng)
    let response = await request.json();
    for (let i = 0; i < response.count; i++) {
        newNamePar = response.data[i].name.split(" ");
        for (let n = 0; n < newNamePar.length; n++) {
            if (names.has(newNamePar[n]) == false){
                names.add(newNamePar[n]);
                newCheck = "<div class='check'>" + newNamePar[n] + "</div>"
                $("#names_check").append(newCheck);
            }
        }
    }
    console.log(names)
}

async function getRoles() {
    requestIng = "http://127.0.0.1:5000/find_users?key="
    let request = await fetch(requestIng)
    let response = await request.json();
    for (let i = 0; i < response.count; i++) {
        newCheckPar = response.data[i].roles.split(" ")
        for (let n = 0; n < newCheckPar.length; n++) {
            if (roles.has(newCheckPar[n].toLowerCase()) == false){
                roles.add(newCheckPar[n].toLowerCase());
                newCheck = "<div class='check'>" + newCheckPar[n].toLowerCase() + "</div>"
                $("#roles_check").append(newCheck);
            }
        }
    }
}

async function getInterests() {
    requestIng = "http://127.0.0.1:5000/find_users?key="
    let request = await fetch(requestIng)
    let response = await request.json();
    for (let i = 0; i < response.count; i++) {
        newCheckPar = response.data[i].interests.split(", ")
        for (let n = 0; n < newCheckPar.length; n++) {
            if (interests.has(newCheckPar[n].toLowerCase()) == false){
                interests.add(newCheckPar[n].toLowerCase());
                newCheck = "<div class='check'>" + newCheckPar[n].toLowerCase() + "</div>"
                $("#interests_check").append(newCheck);
            }
        }
    }
}

document.addEventListener("click", function (e) {
    if ($(e.target).hasClass("search_tag")){
        element = $(e.target).text() + "_" + $(e.target).attr("id")
        $(e.target).remove();
        searching.delete(element);
    }
    else if ($(e.target).hasClass("text_check")){
        parent = $(e.target)[0].parentNode
        if ($(parent).hasClass("opened") == false){
            $(parent).addClass("opened");
        }else{
            $(parent).removeClass("opened");
        }
    }
    else if ($(e.target).hasClass("check")){
        myId = $($(e.target)[0].parentNode).attr("id").split("_")[0]
        newtag = "<div class='search_tag' id='" + myId + "'>" + $(e.target).text() + "</div>"
        search_parameter = $(e.target).text()+"_"+myId
        if (searching.has(search_parameter) == false){
            $("#searching_field").append(newtag);
            searching.add(search_parameter)
        }
    }
});

function generateSearchRequest(type = "") {
    new_req = ""
    console.log(searching)
    for (let i = 0; i < searching.length; i++) {
        console.log(searching[i])
        if (searching[i].split("_")[1] == type){
            if (i < searching.length-1){
                new_req += (searching[i] + ",")
            }else{
                new_req += searching[i]
            }
        }
    }
    return new_req
}