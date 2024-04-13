'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-fbb876a2.js');
const appGlobals = require('./app-globals-3a1e7e63.js');

const defineCustomElements = async (win, options) => {
  if (typeof window === 'undefined') return undefined;
  await appGlobals.globalScripts();
  return index.bootstrapLazy([["my-component.cjs",[[1,"my-component",{"first":[1],"middle":[1],"last":[1]}]]],["nav-bar.cjs",[[1,"nav-bar"]]],["nav-li.cjs",[[0,"nav-li",{"url":[1],"text":[1],"target":[1],"icon":[1]}]]],["page-footer.cjs",[[0,"page-footer"]]]], options);
};

exports.setNonce = index.setNonce;
exports.defineCustomElements = defineCustomElements;

//# sourceMappingURL=loader.cjs.js.map