import { exportAppData, exportAppUtils, helloWorld } from "./generator.js";
import { Widget } from "./props-behaviour.js";

helloWorld();
exportAppData(document.body.getElementsByTagName('footer')[0]);
exportAppUtils(document.body.getElementsByTagName('footer')[0])

var wTest = new Widget()
wTest.init('Hello, I\'m working')