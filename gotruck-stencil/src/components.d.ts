/* eslint-disable */
/* tslint:disable */
/**
 * This is an autogenerated file created by the Stencil compiler.
 * It contains typing information for all components that exist in this project.
 */
import { HTMLStencilElement, JSXBase } from "@stencil/core/internal";
export namespace Components {
    interface MyComponent {
        /**
          * The first name
         */
        "first": string;
        /**
          * The last name
         */
        "last": string;
        /**
          * The middle name
         */
        "middle": string;
    }
    interface NavBar {
    }
    interface NavLi {
        "icon": string;
        "target": string;
        "text": string;
        "url": string;
    }
    interface PageFooter {
    }
}
declare global {
    interface HTMLMyComponentElement extends Components.MyComponent, HTMLStencilElement {
    }
    var HTMLMyComponentElement: {
        prototype: HTMLMyComponentElement;
        new (): HTMLMyComponentElement;
    };
    interface HTMLNavBarElement extends Components.NavBar, HTMLStencilElement {
    }
    var HTMLNavBarElement: {
        prototype: HTMLNavBarElement;
        new (): HTMLNavBarElement;
    };
    interface HTMLNavLiElement extends Components.NavLi, HTMLStencilElement {
    }
    var HTMLNavLiElement: {
        prototype: HTMLNavLiElement;
        new (): HTMLNavLiElement;
    };
    interface HTMLPageFooterElement extends Components.PageFooter, HTMLStencilElement {
    }
    var HTMLPageFooterElement: {
        prototype: HTMLPageFooterElement;
        new (): HTMLPageFooterElement;
    };
    interface HTMLElementTagNameMap {
        "my-component": HTMLMyComponentElement;
        "nav-bar": HTMLNavBarElement;
        "nav-li": HTMLNavLiElement;
        "page-footer": HTMLPageFooterElement;
    }
}
declare namespace LocalJSX {
    interface MyComponent {
        /**
          * The first name
         */
        "first"?: string;
        /**
          * The last name
         */
        "last"?: string;
        /**
          * The middle name
         */
        "middle"?: string;
    }
    interface NavBar {
    }
    interface NavLi {
        "icon"?: string;
        "target"?: string;
        "text"?: string;
        "url"?: string;
    }
    interface PageFooter {
    }
    interface IntrinsicElements {
        "my-component": MyComponent;
        "nav-bar": NavBar;
        "nav-li": NavLi;
        "page-footer": PageFooter;
    }
}
export { LocalJSX as JSX };
declare module "@stencil/core" {
    export namespace JSX {
        interface IntrinsicElements {
            "my-component": LocalJSX.MyComponent & JSXBase.HTMLAttributes<HTMLMyComponentElement>;
            "nav-bar": LocalJSX.NavBar & JSXBase.HTMLAttributes<HTMLNavBarElement>;
            "nav-li": LocalJSX.NavLi & JSXBase.HTMLAttributes<HTMLNavLiElement>;
            "page-footer": LocalJSX.PageFooter & JSXBase.HTMLAttributes<HTMLPageFooterElement>;
        }
    }
}
