import { Host, h } from "@stencil/core";
export class NavLi {
    constructor() {
        this.url = undefined;
        this.text = undefined;
        this.target = "#main";
        this.icon = undefined;
    }
    render() {
        return (h(Host, { key: '4f3792cbae4e46e8ba09c8f72c2440b50e3633cd' }, h("li", { key: '66da0ed7ebd5643e56fa694ea8350c8d4c73e5a9', class: "sidebar-item" }, h("a", { key: 'a17257746c12cf27e425eebafccbb724a826976b', class: "sidebar-link", href: this.url, "up-target": this.target }, h("img", { key: 'baac34fce8e28bc8cb2f15baf037102f190f6306', src: this.icon, class: "icons" }), this.text))));
    }
    static get is() { return "nav-li"; }
    static get properties() {
        return {
            "url": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string",
                    "resolved": "string",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "url",
                "reflect": false
            },
            "text": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string",
                    "resolved": "string",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "text",
                "reflect": false
            },
            "target": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string",
                    "resolved": "string",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "target",
                "reflect": false,
                "defaultValue": "\"#main\""
            },
            "icon": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string",
                    "resolved": "string",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "icon",
                "reflect": false
            }
        };
    }
}
//# sourceMappingURL=nav-li.js.map
