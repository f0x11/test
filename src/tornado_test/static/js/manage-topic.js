$(function () {
            var provMap = [
                [1, "北京"],
                [2, "山东"],
                [3, "河北"],
                [4, "江苏"]
            ];

            for(var i in provMap) {
                var tmp = provMap[i];
                var cont = '<option value="' + tmp[0] + '">' + tmp[1] + '</option>';
                $("#new-topic-location").append(cont);
            }

            $("body").on("click", ".show-img", function (e) {
                e.preventDefault();

                var indexImg = $(this).closest(".panel-body").find(".index-img");
                indexImg.attr("src", indexImg.data('src')).show();

                $(this).hide();
            });

            var begin = 0;
            var limit = 20;
            var fetching = false;
            var normalTopicTemplate = _.template($("#topic-manage-template").html());

            function renderNormalTopic() {
                if (fetching) {
                    return;
                }
                fetching = true;

                var normalTopicUrl = 'http://test.shitouren.com/api/topic/list';
                var normalTopicData = {
                    postData: JSON.stringify({
                        idx: 0,
                        params: {
                            begin: begin,
                            limit: limit,
                            provid: 1
                        }
                    })
                };

                $.ajax({
                    url: normalTopicUrl,
                    type: 'post',
                    dataType: 'json',
                    data: normalTopicData,
                    success: function (res) {
                        if (res.ret == 0) {
                            var topicElem = $(".show-container");
                            if (begin == 0) {
                                topicElem.empty();
                            }
                            $.each(res.res, function (idx, normalTopic) {
                                topicElem.append(normalTopicTemplate(normalTopic));
                            });
                            begin += limit;
                        }
                    },
                    error: function (res) {
                        console.log(res.msg)
                    },
                    complete: function () {
                        fetching = false;
                    }
                });
            }

            renderNormalTopic();

            // Change this to the location of your server-side upload handler:
            var uploadUrl = location.pathname;
            Dropzone.autoDiscover = false;
            // Now that the DOM is fully loaded, create the dropzone, and setup the
            // event listeners
            var drop_settings = {
                maxFiles:1,
                uploadMultiple: false,
                url: uploadUrl,
                acceptedFiles: "image/*",
                paramName: "file",
                dictDefaultMessage:"<i class=\"fa fa-cloud-upload fa-3x fa-green\"></i><br>点击 或 拖放图片到这里上传",
                dictFallbackMessage:"你的浏览器不支持拖放上传",
                autoProcessQueue: false
            };
            var dz = new Dropzone(".dropzone", drop_settings);
            dz.on("sending", function(file, xhr, formData) {
                formData.append("provid", $("#new-topic-location").val());
                formData.append("title", $("#new-topic-title").val().trim());
                formData.append("intro", $("#new-topic-content").val().trim());
            });
            dz.on('success', function(file, response) {
                window.location.href = window.location.protocol + '//' + window.location.host + '/i/' + response['id'] + '/';
            });

            $(".nt-submit").on("click", function(e) {
                e.preventDefault();

                var title = $("#new-topic-title").val().trim();
                if(!title) {
                    alert("标题不能为空");
                    return;
                }
                dz.processFiles();
            });
        });