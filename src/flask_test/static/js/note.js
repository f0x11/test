$(function () {
    function initTopicInfo() {
        var topicInfoUrl = 'api/topic/info';
        var topicInfoTemplate = _.template($("#topic-info-template").html());

        var data = {
            postData: JSON.stringify({
                idx: 1,
                params: {
                    topicid: 2000005
                }
            })
        };

        $.ajax({
            url: topicInfoUrl,
            data: data,
            success: function (res) {
                if (res.ret == 0) {
                    $(".tn-container").append(topicInfoTemplate(res.res));
                } else {
                    console.log(res)
                }
            },
            error: function (res) {
                console.log(res)
            }
        });
    }

    function initNoteList() {
        var noteTemplate = _.template($("#note-template"));
        var noteListUrl = "/api/note/list";

        $.ajax({
            url: noteListUrl,
            data: data,
            success: function (res) {
                if (res.ret == 0) {
                    $.each(res.res, function (index, noteInfo) {
                        $(".note-l-c").append(noteTemplate(noteInfo))
                    });
                } else {
                    console.log(res);
                }
            },
            error: function (res) {
                console.log(res);
            }
        });
    }

    initTopicInfo();
    initNoteList()
});