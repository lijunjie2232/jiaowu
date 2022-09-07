// ==UserScript==
// @name        去他妈的不支持定位
// @namespace   Violentmonkey Scripts
// @match       https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp
// @grant       none
// @version     1.0
// @author      lijunjie2232
// @description 2022/9/1 下午10:04:14
// @require http://code.jquery.com/jquery-1.11.0.min.js
// ==/UserScript==
// @run-at      document-body

(function() {
	$("#havelocation")
		.html("您当前使用的终端设备不支持定位，请使用超级App或企业微信应用进行填报！");
	var customUserAgent = 'superapp; app/Android';
	Object.defineProperty(navigator, 'userAgent', {
		value: customUserAgent,
		writable: false
	});

	console.log(navigator.userAgent);
	console.log($("#havelocation")
		.html());
	if (document.querySelector(".co4") == null) {
		//go_sub();
		go_subfx();
		document.querySelector(".co3")
			.click();
		//save();
		savefx();
	} else {
		alert("submited");
	}
})();
