


$("#send").on("click", function(e) {
    e.preventDefault();
    let msg = $("#msg").val()
    var data_to_send =
        {
            "message": msg
        }

    $.ajax({
        url: "http://35.211.212.220:5005/webhooks/rest/webhook",
        type: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(data_to_send),
        beforeSend: function(x) {
            if (x && x.overrideMimeType) {
              x.overrideMimeType("application/j-son;charset=UTF-8");
            }
          },
        success: function(result) {
            console.log(result[0].text)
            $("#response").html(result[0].text)
        }
    })
})