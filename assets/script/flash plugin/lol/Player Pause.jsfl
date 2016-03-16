﻿var showDesc = true
var desc = " --[战斗]攻击者暂停"

function setScript(script)
{
	if(showDesc) script += desc;
	script += "\n"
	
	var timeline = fl.getDocumentDOM().getTimeline();
	var layers = timeline.layers;
	var frames = timeline.getSelectedFrames();
	var layer = layers[frames[0]];
	var frame = layer.frames[frames[1]];
	frame.actionScript = frame.actionScript + script;
}

var doc = fl.getDocumentDOM();
var uxi = doc.xmlPanel(fl.configURI + "Commands/lol/MoveOut.xml");
if(uxi.dismiss == "accept")
{
	var script = "win.fightingFlash.playerPause(" + uxi.time + ")";	
	setScript(script)
}
