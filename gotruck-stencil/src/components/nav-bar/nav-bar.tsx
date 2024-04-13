import { Component, Host, h } from '@stencil/core';

@Component({
  tag: 'nav-bar',
  shadow: true,
})
export class NavBar {

  render() {
    return (
      <Host>
        <slot></slot>
      </Host>
    );
  }

}
