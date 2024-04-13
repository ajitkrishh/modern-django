import { Component, Host, h } from '@stencil/core';

@Component({
  tag: 'page-footer',
})
export class PageFooter {

  render() {
    return (
      <Host>
        <footer class="position-absolute bottom-0 bg-darkBlue text-white text-center py-3 w-100 text-xs" id="footer">
          <div class="container-fluid">
            <div class="row gy-2">
              <div class="col-sm-6 text-sm-start">
                <p class="mb-0">Go Truck &copy; 2017-2022</p>
              </div>
            </div>
          </div>
        </footer>
      </Host>
    );
  }

}
