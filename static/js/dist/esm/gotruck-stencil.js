import { p as promiseResolve, b as bootstrapLazy } from './index-67a17094.js';
export { s as setNonce } from './index-67a17094.js';
import { g as globalScripts } from './app-globals-0f993ce5.js';

/*
 Stencil Client Patch Browser v4.15.0 | MIT Licensed | https://stenciljs.com
 */
const patchBrowser = () => {
    const importMeta = import.meta.url;
    const opts = {};
    if (importMeta !== '') {
        opts.resourcesUrl = new URL('.', importMeta).href;
    }
    return promiseResolve(opts);
};

patchBrowser().then(async (options) => {
  await globalScripts();
  return bootstrapLazy([["my-component",[[1,"my-component",{"first":[1],"middle":[1],"last":[1]}]]],["nav-bar",[[1,"nav-bar"]]],["nav-li",[[0,"nav-li",{"url":[1],"text":[1],"target":[1],"icon":[1]}]]],["page-footer",[[0,"page-footer"]]]], options);
});

//# sourceMappingURL=gotruck-stencil.js.map