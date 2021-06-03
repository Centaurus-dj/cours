import { exportAppData, helloWorld } from "./generator.js";

helloWorld();
exportAppData(document.body.getElementsByTagName("footer"));