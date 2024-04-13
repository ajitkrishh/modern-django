import { Component, Host, h, Prop } from '@stencil/core';

@Component({
  tag: 'nav-li',
})
export class NavLi {
  @Prop() url: string;
  @Prop() text: string;
  @Prop() target: string = "#main";
  @Prop() icon: string;

  render() {
    return (
      <Host>
        <li class="sidebar-item">
          <a class="sidebar-link" href={this.url} up-target={this.target}>
            <img src={this.icon} class="icons" />
              {this.text}
          </a>
        </li>
      </Host>
    );
  }
}
