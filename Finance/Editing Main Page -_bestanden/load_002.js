var isCompatible=function(){if(navigator.appVersion.indexOf('MSIE')!==-1&&parseFloat(navigator.appVersion.split('MSIE')[1])<6){return false;}return true;};var startUp=function(){mw.config=new mw.Map(true);mw.loader.addSource({"local":{"loadScript":"/load.php","apiScript":"/api.php"}});mw.loader.register([["site","1402765136",[],"site"],["noscript","1402765136",[],"noscript"],["startup","1404671191",[],"startup"],["user","1402765136",[],"user"],["user.groups","1402765136",[],"user"],["user.options","1404671191",[],"private"],["user.cssprefs","1404671191",["mediawiki.user"],"private"],["user.tokens","1402765136",[],"private"],["filepage","1402765136",[]],["skins.chick","1402765136",[]],["skins.cologneblue","1402765136",[]],["skins.modern","1402765136",[]],["skins.monobook","1402765136",[]],["skins.nostalgia","1402765136",[]],["skins.simple","1402765136",[]],["skins.standard","1402765136",[]],["skins.vector","1402765136",[]],["jquery","1402765136",[]],["jquery.appear","1402765136",[]],[
"jquery.arrowSteps","1402765136",[]],["jquery.async","1402765136",[]],["jquery.autoEllipsis","1402765136",["jquery.highlightText"]],["jquery.byteLength","1402765136",[]],["jquery.byteLimit","1402765136",["jquery.byteLength"]],["jquery.checkboxShiftClick","1402765136",[]],["jquery.client","1402765136",[]],["jquery.collapsibleTabs","1402765136",[]],["jquery.color","1402765136",["jquery.colorUtil"]],["jquery.colorUtil","1402765136",[]],["jquery.cookie","1402765136",[]],["jquery.delayedBind","1402765136",[]],["jquery.expandableField","1402765136",["jquery.delayedBind"]],["jquery.farbtastic","1402765136",["jquery.colorUtil"]],["jquery.footHovzer","1402765136",[]],["jquery.form","1402765136",[]],["jquery.getAttrs","1402765136",[]],["jquery.highlightText","1402765136",[]],["jquery.hoverIntent","1402765136",[]],["jquery.json","1402765136",[]],["jquery.localize","1402765136",[]],["jquery.makeCollapsible","1402853202",[]],["jquery.messageBox","1402765136",[]],["jquery.mockjax","1402765136",[]],[
"jquery.mw-jump","1402765136",[]],["jquery.mwExtension","1402765136",[]],["jquery.placeholder","1402765136",[]],["jquery.qunit","1402765136",[]],["jquery.qunit.completenessTest","1402765136",["jquery.qunit"]],["jquery.spinner","1402765136",[]],["jquery.suggestions","1402765136",["jquery.autoEllipsis"]],["jquery.tabIndex","1402765136",[]],["jquery.tablesorter","1402765136",["jquery.mwExtension"]],["jquery.textSelection","1402765136",[]],["jquery.validate","1402765136",[]],["jquery.xmldom","1402765136",[]],["jquery.tipsy","1402765136",[]],["jquery.ui.core","1402765136",["jquery"],"jquery.ui"],["jquery.ui.widget","1402765136",[],"jquery.ui"],["jquery.ui.mouse","1402765136",["jquery.ui.widget"],"jquery.ui"],["jquery.ui.position","1402765136",[],"jquery.ui"],["jquery.ui.draggable","1402765136",["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget"],"jquery.ui"],["jquery.ui.droppable","1402765136",["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget","jquery.ui.draggable"],"jquery.ui"],[
"jquery.ui.resizable","1402765136",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.selectable","1402765136",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.sortable","1402765136",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.accordion","1402765136",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.autocomplete","1402765136",["jquery.ui.core","jquery.ui.widget","jquery.ui.position"],"jquery.ui"],["jquery.ui.button","1402765136",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.datepicker","1402765136",["jquery.ui.core"],"jquery.ui"],["jquery.ui.dialog","1402765136",["jquery.ui.core","jquery.ui.widget","jquery.ui.button","jquery.ui.draggable","jquery.ui.mouse","jquery.ui.position","jquery.ui.resizable"],"jquery.ui"],["jquery.ui.progressbar","1402765136",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.slider","1402765136",["jquery.ui.core",
"jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.tabs","1402765136",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.effects.core","1402765136",["jquery"],"jquery.ui"],["jquery.effects.blind","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.bounce","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.clip","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.drop","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.explode","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.fade","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.fold","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.highlight","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.pulsate","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.scale","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.shake","1402765136",["jquery.effects.core"],
"jquery.ui"],["jquery.effects.slide","1402765136",["jquery.effects.core"],"jquery.ui"],["jquery.effects.transfer","1402765136",["jquery.effects.core"],"jquery.ui"],["mediawiki","1402765136",[]],["mediawiki.api","1402765136",["mediawiki.util"]],["mediawiki.api.category","1402765136",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.edit","1402765136",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.parse","1402765136",["mediawiki.api"]],["mediawiki.api.titleblacklist","1402765136",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.watch","1402765136",["mediawiki.api","mediawiki.user"]],["mediawiki.debug","1402765136",["jquery.footHovzer"]],["mediawiki.debug.init","1402765136",["mediawiki.debug"]],["mediawiki.feedback","1402765136",["mediawiki.api.edit","mediawiki.Title","mediawiki.jqueryMsg","jquery.ui.dialog"]],["mediawiki.htmlform","1402765136",[]],["mediawiki.Title","1402765136",["mediawiki.util"]],["mediawiki.Uri","1402765136",[]],["mediawiki.user","1402765136",[
"jquery.cookie"]],["mediawiki.util","1402853201",["jquery.client","jquery.cookie","jquery.messageBox","jquery.mwExtension"]],["mediawiki.action.edit","1402765136",["jquery.textSelection","jquery.byteLimit"]],["mediawiki.action.history","1402765136",["jquery.ui.button"],"mediawiki.action.history"],["mediawiki.action.history.diff","1402765136",[],"mediawiki.action.history"],["mediawiki.action.view.dblClickEdit","1402765136",["mediawiki.util"]],["mediawiki.action.view.metadata","1402765136",[]],["mediawiki.action.view.rightClickEdit","1402765136",[]],["mediawiki.action.watch.ajax","1402853267",["mediawiki.api.watch","mediawiki.util"]],["mediawiki.language","1402765136",[]],["mediawiki.jqueryMsg","1402765136",["mediawiki.language","mediawiki.util"]],["mediawiki.libs.jpegmeta","1402765136",[]],["mediawiki.page.ready","1402765136",["jquery.checkboxShiftClick","jquery.makeCollapsible","jquery.placeholder","jquery.mw-jump","mediawiki.util"]],["mediawiki.page.startup","1402765136",[
"jquery.client","mediawiki.util"]],["mediawiki.special","1402765136",[]],["mediawiki.special.block","1402765136",["mediawiki.util"]],["mediawiki.special.changeemail","1402765136",["mediawiki.util"]],["mediawiki.special.changeslist","1402765136",["jquery.makeCollapsible"]],["mediawiki.special.movePage","1402765136",["jquery.byteLimit"]],["mediawiki.special.preferences","1402765136",[]],["mediawiki.special.recentchanges","1402765136",["mediawiki.special"]],["mediawiki.special.search","1402765136",[]],["mediawiki.special.undelete","1402765136",[]],["mediawiki.special.upload","1402765136",["mediawiki.libs.jpegmeta","mediawiki.util"]],["mediawiki.special.javaScriptTest","1402765136",["jquery.qunit"]],["mediawiki.tests.qunit.testrunner","1402765136",["jquery.qunit","jquery.qunit.completenessTest","mediawiki.page.startup","mediawiki.page.ready"]],["mediawiki.legacy.ajax","1402765136",["mediawiki.util","mediawiki.legacy.wikibits"]],["mediawiki.legacy.commonPrint","1402765136",[]],[
"mediawiki.legacy.config","1402765136",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.IEFixes","1402765136",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.mwsuggest","1402765136",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.preview","1402765136",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.protect","1402765136",["mediawiki.legacy.wikibits","jquery.byteLimit"]],["mediawiki.legacy.shared","1402765136",[]],["mediawiki.legacy.oldshared","1402765136",[]],["mediawiki.legacy.upload","1402765136",["mediawiki.legacy.wikibits","mediawiki.util"]],["mediawiki.legacy.wikibits","1402765136",["mediawiki.util"]],["mediawiki.legacy.wikiprintable","1402765136",[]]]);mw.config.set({"wgLoadScript":"/load.php","debug":false,"skin":"monobook","stylepath":"/skins","wgUrlProtocols":"http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|ircs\\:\\/\\/|gopher\\:\\/\\/|telnet\\:\\/\\/|nntp\\:\\/\\/|worldwind\\:\\/\\/|mailto\\:|news\\:|svn\\:\\/\\/|git\\:\\/\\/|mms\\:\\/\\/|\\/\\/","wgArticlePath"
:"/index.php/$1","wgScriptPath":"","wgScriptExtension":".php","wgScript":"/index.php","wgVariantArticlePath":false,"wgActionPaths":{},"wgServer":"http://ec2-54-213-106-230.us-west-2.compute.amazonaws.com","wgUserLanguage":"en","wgContentLanguage":"en","wgVersion":"1.19.16+dfsg-0+deb7u1","wgEnableAPI":true,"wgEnableWriteAPI":true,"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgMainPageTitle":"Main Page","wgFormattedNamespaces":{"-2":"Media","-1":"Special","0":"","1":"Talk","2":"User","3":"User talk","4":"","5":" talk","6":"File","7":"File talk","8":"MediaWiki","9":"MediaWiki talk","10":"Template","11":"Template talk","12":"Help","13":"Help talk","14":"Category","15":"Category talk"},"wgNamespaceIds":{"media":-2,"special":-1,"":0,"talk":1,"user":2,"user_talk":3,"_talk":5,"file":6,
"file_talk":7,"mediawiki":8,"mediawiki_talk":9,"template":10,"template_talk":11,"help":12,"help_talk":13,"category":14,"category_talk":15,"image":6,"image_talk":7,"project":4,"project_talk":5},"wgSiteName":"","wgFileExtensions":["png","gif","jpg","jpeg"],"wgDBname":"mediawiki","wgFileCanRotate":true,"wgAvailableSkins":{"nostalgia":"Nostalgia","modern":"Modern","cologneblue":"CologneBlue","monobook":"MonoBook","vector":"Vector","chick":"Chick","standard":"Standard","simple":"Simple","myskin":"MySkin"},"wgExtensionAssetsPath":"/extensions","wgCookiePrefix":"mediawiki","wgResourceLoaderMaxQueryLength":-1,"wgCaseSensitiveNamespaces":[]});};if(isCompatible()){document.write("\x3cscript src=\"/load.php?debug=false\x26amp;lang=en\x26amp;modules=jquery%2Cmediawiki\x26amp;only=scripts\x26amp;skin=monobook\x26amp;version=20140529T180158Z\"\x3e\x3c/script\x3e");}delete isCompatible;;

/* cache key: mediawiki:resourceloader:filter:minify-js:7:dea3a8b5f137911dceab1fb4d9ac96e6 */
