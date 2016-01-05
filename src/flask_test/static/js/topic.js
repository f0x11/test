$(function() {
    var begin = 0;
    var limit = 20;
    var fetching = false;
    var normalTopicTemplate = _.template($("#normal-topic-template").html());

    function renderNormalTopic() {
        if (fetching) {
            return;
        }
        fetching = true;

        var normalTopicUrl = '/api/topic/list';
        var normalTopicData = {
            postData: JSON.stringify({
                idx: 0,
                params: {
                    begin: begin,
                    limit: limit,
                    provid: 0
                }
            })
        };

        $.ajax({
            url: normalTopicUrl,
            type: 'post',
            dataType: 'json',
            data: normalTopicData,
            success: function(res) {
                if(res.ret == 0) {
                    var topicElem = $(".normal-topics");
                    if(begin == 0) {
                        topicElem.empty();
                    }
                    $.each(res.res, function(idx, normalTopic) {
                        console.log(normalTopic)
                        topicElem.append(normalTopicTemplate(normalTopic));
                    });
                    begin += limit;
                }
            },
            error: function(res) {
                console.log(res.msg)
            },
            complete: function() {
                fetching = false;
            }
        });
    }

    renderNormalTopic();
});