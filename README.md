The Goal is to make A super powered full stack framework.
Django is love, but needs more reactivity at frontend, to accompolish this i am using stencil and unpoly.js not at their full capacity
but for simple reactivity.
Using Custom html element comes with added benifit, we have less template to render and this saves bandwith, combining small response size with unpoly.js,
we get a server rendered, yet fully reactive web app.

simple rule for stencil: if we are going to loop over bunch of html ,then create a custom element can be created for it , :
  for example : a simple bootstrap user card has ~10 lines, to render 20 such cards, html response easily reaches 200 lines:
      so create a simple <user-card /> element and loop over it 20 times. it will be rendered on froontend by stencil + all the reactivity you get.

Unpoly is used to avoid blank screen duing page load and smooth transition.
