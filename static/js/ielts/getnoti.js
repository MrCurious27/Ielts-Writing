$(document).ready(function() {
    const interval = setInterval(function() {
    getNotified();
    }, 5000);
})

function getNotified(){
    $.ajax({
        url: "/get-noti/",
        method: "GET",
        success: function(data) {
            // console.log("I got the following data");
            // console.log(data);

            if (data.task_one_a){
                $('#taskonea').addClass('badge badge-secondary');
                $('#taskonea').html("New");
            } else {
                $('#taskonea').removeClass('badge badge-secondary');
                $('#taskonea').html("");
            }

            if (data.task_one_g){
                $('#taskoneg').addClass('badge badge-secondary');
                $('#taskoneg').html("New");
            } else {
                $('#taskoneg').removeClass('badge badge-secondary');
                $('#taskoneg').html("");
            }

            if (data.task_two){
                $('#tasktwo').addClass('badge badge-secondary');
                $('#tasktwo').html("New");
            } else {
                $('#tasktwo').removeClass('badge badge-secondary');
                $('#tasktwo').html("");
            }

            if (data.task_one_a || data.task_one_g || data.task_two){
                $('#taskmain').addClass('badge badge-secondary');
                $('#taskmain').html("New");
            } else {
                $('#taskmain').removeClass('badge badge-secondary');
                $('#taskmain').html("");
            }

        },
        error: function(data) {
            console.log("error");
            // console.log(data);
        }
    })
}
