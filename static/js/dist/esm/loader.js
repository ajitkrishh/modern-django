import { b as bootstrapLazy } from './index-67a17094.js';
export { s as setNonce } from './index-67a17094.js';
import { g as globalScripts } from './app-globals-0f993ce5.js';

const defineCustomElements = async (win, options) => {
  if (typeof window === 'undefined') return undefined;
  await globalScripts();
  return bootstrapLazy([["my-component",[[1,"my-component",{"first":[1],"middle":[1],"last":[1]}]]],["nav-bar",[[1,"nav-bar"]]],["nav-li",[[0,"nav-li",{"url":[1],"text":[1],"target":[1],"icon":[1]}]]],["page-footer",[[0,"page-footer"]]]], options);
};

export { defineCustomElements };

//# sourceMappingURL=loader.js.map