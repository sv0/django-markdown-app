(function($) {
    var config = JSON.parse($("#markItUpEditorConfig").text());
    $(document).ready(function() {
        $(config["selector"]).each(function (k, el) {
            var el = $(el);
            if(!el.hasClass("markItUpEditor")) el.markItUp(
                mySettings, config["extra_settings"]);
        });
    });
})(jQuery);
