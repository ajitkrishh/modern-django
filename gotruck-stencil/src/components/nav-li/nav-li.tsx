import { Component, Host, h, Prop, State, Listen } from '@stencil/core';

@Component({
  tag: 'nav-li',
})
export class NavLi {
  @Prop() url: string;
  @Prop() text: string;
  @Prop() target: string = "#main";
  @Prop() icon: string;

  @State() isActiveState: boolean; // Manage isActive state internally

  // Initialize isActiveState with the prop value
  componentWillLoad() {
    this.setActiveLink()
  }

  @Listen('up:fragment:inserted', { target: 'body' })
  handleLinkClicked(event: any) {
    this.setActiveLink();
  }


  setActiveLink() {
    this.isActiveState = window.location.pathname == this.url;
  }

  render() {

    // Determine the class based on isActiveState
    const liClass = this.isActiveState ? 'sidebar-item active' : 'sidebar-item';

    return (
      <Host>
        <li class={liClass} >
          <a href={this.url} up-target={this.target} class="sidebar-link">
            <img src={this.icon} class="icon icon-sm me-xl-2 icon-heavy" />
            {this.text}
          </a>
        </li>
      </Host>
    );


  }
}