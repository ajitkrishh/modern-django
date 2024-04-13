import { r as registerInstance, h, H as Host } from './index-67a17094.js';

const NavLi = class {
    constructor(hostRef) {
        registerInstance(this, hostRef);
        this.url = undefined;
        this.text = undefined;
        this.target = "#main";
        this.icon = undefined;
    }
    render() {
        return (h(Host, { key: '4f3792cbae4e46e8ba09c8f72c2440b50e3633cd' }, h("li", { key: '66da0ed7ebd5643e56fa694ea8350c8d4c73e5a9', class: "sidebar-item" }, h("a", { key: 'a17257746c12cf27e425eebafccbb724a826976b', class: "sidebar-link", href: this.url, "up-target": this.target }, h("img", { key: 'baac34fce8e28bc8cb2f15baf037102f190f6306', src: this.icon, class: "icons" }), this.text))));
    }
};

export { NavLi as nav_li };

//# sourceMappingURL=nav-li.entry.js.map