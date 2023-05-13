roles=["blank", "backend", "frontend", "dota2", "cs2", "css", "mobile"]

last_response = null

$(document).ready(function () {
    prof_element  = $("#profile")
    prof_width = parseFloat(prof_element.width())
    prof_height = parseFloat(prof_element.height())
    $("#nickname").css({
        padding: 0.03*prof_width,
    })
    
    phone_width = $("#phone").width()
    phone_height = $("#phone").height()

    $("#changePhoneButton").css({
        padding: 0.03*phone_width,
        height: phone_height-0.06*phone_width
    })
    $("#phoneNumber").css({
        padding: 0.03*phone_width,
        height: phone_height-0.06*phone_width
    })

    for (let i = 0; i < 30; i++) {
        new_day = "<div class='day' id='day_"+(i+1)+"'>"+(i+1)+"</div>"
        $("#calendar").append(new_day);
    }
    $($(".day")[22]).addClass("deadline");
    $("#toExpandedSearch").click(function () {
        window.location.href = "expandedSearchPage.html"
    });
    $("#toMyCab").click(function () {
        window.location.href = "index.html"
    });
    $(".day").click(function (e) { 
        id = parseInt($(this).attr("id").split("_")[1])
        //взять из бд
        $("#task_day").text(id);
        $("#task_name").text("имя таска на день: "+id)
        $("#task_description").text("нереальное описание таска на день: "+id)
        deadline = id+4
        if (id <= 23){
            deadline = 23
        }
        if (deadline > 30){
            deadline = 30
        }
        $("#task_deadline").text(deadline)
        $("#task_faster").text("")
        text_last = "Это последний день выполнения!"
        if ($(this).hasClass("deadline")){
            for (let k = 0; k < text_last.length; k++) {
                setTimeout(() => {
                    $("#task_faster").text($("#task_faster").text()+text_last[k])
                }, 15*k);
                
            }
        }
    });
    $("#fast_search_button").click(async function (){
        search_activated();
    });
    $("#cross_info").click(function () {
        $("#person_info").css({
            display: "none"
        });
    });
});


document.addEventListener("click", function (e) {
    if ($(e.target).hasClass("dropdown_field")){
        id = parseInt($(e.target).attr("id").split("_")[1])
        person = last_response.data[id]
        $("#prof_photo_info").css({
            "background-image": "url("+person.photo+")"
        });
        console.log(person)
        $("#naming_info").text(person.name)
        $("#email_info").text(person.email)
        $("#phoneNumber_info").text(person.number)
        $("#roles_info").text(person.roles)
        $("#departament_info").text(person.departament)
        $("#interests_info").text(person.interests)
        $("#person_info").css({
            display: "block"
        });
    }
});

document.addEventListener("mousemove", function (e) {
    if ($("#form_search").is(":hover") == false &&
    $("#dropdown_list").is("hover") == false){
        $("#dropdown_list").css({
            "max-height": 0
        })
    }
    else {
        $("#dropdown_list").css({
            "max-height": "40vh"
        })
    }
});

document.addEventListener("keydown", function (e) {
    if (e.key == "Enter"){
        console.log("e")
        if (document.getElementById("fast_search") == document.activeElement){
            search_activated();
        }
    }
});

async function search_activated() {
    user_input = $("#fast_search").val()
    requestIng = "http://127.0.0.1:5000/find_users?key=" + user_input
    let request = await fetch(requestIng)
    let response = await request.json();
    console.log(response)
    last_response = response
    $("#dropdown_list").empty()
    for (let i = 0; i < response.count; i++) {
        new_element = "<div class='dropdown_field' id='profile_"+i+"'>" + response.data[i].name + "</div>"
        $("#dropdown_list").append(new_element);
    }
}