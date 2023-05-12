$(document).ready(function () {
    prof_element  = $("#profile")
    prof_width = parseFloat(prof_element.width())
    prof_height = parseFloat(prof_element.height())
    $("#avatar").css({
        height: $("#avatar").width()
    })
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
});