django.jQuery( document ).ready(function () {
    django.jQuery('.markItUpEditorConfig').each(function (i, config_element) {
        var config = JSON.parse(config_element.textContent);
        django.jQuery(config["selector"]).each(function (k, el) {
            var el = django.jQuery(el);
            if(!el.hasClass("markItUpEditor")) {
                el.markItUp(mySettings, config["extra_settings"]);
            }
        });
    });
});
