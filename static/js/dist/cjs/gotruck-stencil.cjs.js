'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-fbb876a2.js');
const appGlobals = require('./app-globals-3a1e7e63.js');

/*
 Stencil Client Patch Browser v4.15.0 | MIT Licensed | https://stenciljs.com
 */
const patchBrowser = () => {
    const importMeta = (typeof document === 'undefined' ? new (require('u' + 'rl').URL)('file:' + __filename).href : (document.currentScript && document.currentScript.src || new URL('gotruck-stencil.cjs.js', document.baseURI).href));
    const opts = {};
    if (importMeta !== '') {
        opts.resourcesUrl = new URL('.', importMeta).href;
    }
    return index.promiseResolve(opts);
};

patchBrowser().then(async (options) => {
  await appGlobals.globalScripts();
  return index.bootstrapLazy([["my-component.cjs",[[1,"my-component",{"first":[1],"middle":[1],"last":[1]}]]],["nav-bar.cjs",[[1,"nav-bar"]]],["nav-li.cjs",[[0,"nav-li",{"url":[1],"text":[1],"target":[1],"icon":[1]}]]],["page-footer.cjs",[[0,"page-footer"]]]], options);
});

exports.setNonce = index.setNonce;

//# sourceMappingURL=gotruck-stencil.cjs.js.map