function UUID() {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}

function setUUID() {
    var ssidKey = 'shitouren_ssid';
    var ca = document.cookie.split(';');
    for(var i=0; i< ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1);
        if (c.indexOf(ssidKey) != -1) {
            return c.substring(ssidKey.length, c.length);
        }
    }
    var d= new Date();
    d.setHours(d.getHours() + (24 * 30)); //保存一个月
    document.cookie=ssidKey + "=" + UUID() + "; expires=" + d.toGMTString() + "; path=/; domain=shitouren.com;";
}

setUUID();

