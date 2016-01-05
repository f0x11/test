$(function() {
    $(".send-sms").on("click", function() {
        var phone = $("#phone").val();
        $.ajax({
            url: '/api/user/sendsms',
            data: {
                postData: JSON.stringify({
                    idx: 1,
                    params: {
                        type: 'register',
                        phone: phone
                    }
                })
            },
            dataType: "json",
            type: 'post',
            success: function(res) {
                if(res.ret == 0) {
                    alert("发送成功");
                } else {
                    alert(res.msg);
                }
            },
            error: function(res) {
                alert(res.msg);
            }
        });
    });

    $(".submit").on("click", function() {
        var phone = $("#phone").val();
        var passwd = $("#passwd").val();
        var verify = $("#verify").val();

        $.ajax({
            url: "/api/user/signup",
            type: "post",
            dataType: "json",
            data: {
                postData: JSON.stringify({
                    idx: 1,
                    params: {
                        phone: phone,
                        passwd: passwd,
                        verify: verify
                    }
                })
            },
            success: function(res) {
                if(res.ret == 0) {
                    window.location.href="/web/signin"
                } else {
                    alert(res.msg);
                }
            },
            error: function(res) {
                alert(res.msg);
            }
        });
    });
});