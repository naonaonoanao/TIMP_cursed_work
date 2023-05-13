roles=["blank", "backend", "frontend", "dota2", "cs2", "css", "mobile"]

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
        lastOne = $(".day")[$(".day").length-1]
    }
    $($(".day")[22]).addClass("deadline");
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
        user_input = $("#fast_search").val()
        request = "http://127.0.0.1:5000/find_users?key=" + user_input
        let response = await fetch(request)
        let data = await response.json();
        console.log(data)
        $("#dropdown_list").empty()
        for (let i = 0; i < data.count; i++) {
            new_element = "<div class='dropdown_field'>" + data.data.name + "</div>"
        }
    });

});