# Bootstrap

[Bootstrap](https://getbootstrap.com/) is a front-end framework that helps you build mobile responsive websites more quickly and easily. First developed by Twitter, Bootstrap is by now used for anything from developing web applications to WordPress themes. It is also completely free, versatile, and intuitive.

With Bootstrap, you can conjure complex web pages from standard HTML and customize them to your needs. Bootstrap also comes with a number of jQuery plugins that can provide additional functionality such as carousels, buttons, tooltips, and more.

Last, but not least, it gives you a lot of shortcuts for creating web pages that will save you time and energy. All you need is a basic understanding of HTML and CSS to creates that are responsive, mobile-first, and compatible with all modern browsers.



#### Setup

Bootstrap consists mainly of style sheets and script. As such, they can be loaded in your HTML like any other style sheet.



**Using a CDN**

CDN stands for *Content Delivery Network*. 

A CDN server hold resources such as images, videos, audio clips, but also CSS and JavaScript files.

With a CDN, you don't need to download the css/javascript framework that you want to add to your code, just use the remote resources.

For example, to get bootstrap into your page, use the `<link rel="stylesheet">` common syntax, but in the `href`, insert the address of the CDN.

> Actually, the CDN line include a bit more than this, you can copy it from [bootstrap download page](https://getbootstrap.com/docs/4.2/getting-started/download/)

Here is the whole line:

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
```



#### How bootstrap work

Basically, bootstrap is giving you a lot of pre-made CSS classes, for almost all the HTML elements.

For example, the `alert` bootstrap class will style your element in an alert style.

You can add additional styles (see bootstrap documentation for more infos) by adding another class.

For example `alert alert-primary` will style your element in a primary alert style.



#### Bootstrap grid

One of the most powerful features of bootstrap is his grid system.

The grid system is built with flexbox and allows you to organize your HTML file with rows and columns.

How it works:

-  First, your grid is defined under a container (meaning an element with the `container` class)

- Then, you need to define each row in an element with `row` as class, each row contains 12 columns

-  Inside each row you can define some columns in this way `class="col-<responsiveness>-<size>"`. The size is the number of columns this element will take, and the responsiveness parameter define on which screen size this column should be displayed. Here are the existing responsiveness modes:

  - Nothing: (Extra small devices - < 576px)

  - `sm`: (small devices - >576px)
  - `md`: (medium devices - > 768px)
  - `lg`: (large devices - > 992px)
  - `xl`: (xlarge devices - > 1200px)

  For example, `col-md-5` is an element that will take 5 columns of the row, but will be displayed only if the screen width is greater than 768px.

  

A bootstrap grid system overview:

![bootstrap grid example](images/bootstrap_grid_example.jpg)



#### Bootstrap by examples

**Bootstrap alerts**

Bootstrap provides a lot of css classes to display alerts (or any message to the user). 

First add the `alert` class to the element, and then decorate it with some others classes, like:

-  `alert-success`
- `alert-info`
- `alert-warning`
- `alert-danger`

Try them in an [online html editor](https://www.w3schools.com/code/tryit.asp?filename=G8OQDV1I5V0J).



You can also add *links* in your alert, to style them, just add the `alert-link` class to their attributes.



Closing the alert can be done by adding a link or a button with the `class="close"` and the `data-dismiss="alert"` attributes. You also need to put `alert-dismissible` in the alert classes.

You can add animations to those actions. For example, an alert with the `fade` and the `in` class will fade in and out.  



**Bootstrap icons**

Bootstrap provides a big set of icons, called glyphicons, to add a glyphicon, create a `<span>` element with the `glyphicon` class, and then add the class of the icon you want, like `glyphicon-search` or `gliphycon-user`.

For example:

```html
<p>Envelope icon: <span class="glyphicon glyphicon-envelope"></span></p>
<p>Search icon: <span class="glyphicon glyphicon-search"></span></p>
<p>Print icon: <span class="glyphicon glyphicon-print"></span></p>
```

Check the whole list [here](https://www.w3schools.com/bootstrap/bootstrap_ref_comp_glyphs.asp).



**Bootstrap forms**

Bootstrap provides three types of form layouts:

- Vertical, the default one
- Horizontal, `form-horizontal` class
- Inline, `form-inline` class



To build a vertical form with bootstrap:

1) Put each label/input couple in a `<div class="form-group">` container

2) Add the`form-control` class to all textual input.



To build an horizontal form, you need to use bootstrap grid system:

1) Add `control-label` class to the labels.

2) Add the size of the label in the class with a `col` class.

3) Put the input into a div and add a `col` class to this div to size it.





**Bootstrap buttons**

Bootstrap also provides some button styles, just add the `btn` class to your button (it works on `<a>`, `button`> and `<input>` tag.

A list of the bootstrap buttons:

-  `btn-link`
- `btn-primary`
- `btn-success`
- `btn-info`
- `btn-warning`
- `btn-danger`



You can add the classes `btn-lg`, `btn-md`, `btn-sm`, `btn-xs` to size your button, and the `disabled` to make it unclickable.

You can also make a group of button by putting all the buttons in a div with the `btn-group`/`btn-group-vertical` class.



**Bootstrap dropdowns**

A dropdown menu is a toggleable menu that display a predefined list of values.

To create a dropdown with bootstrap, first create a div with `class="dropdown"`.

Then a toggle button with a class of `dropdown-toggle` and the `data-toggle="dropdown"`.

Finally, add the predefined list in a `<ul>` element, add the `dropdown-menu` class to it to bind it.

Now you can add all your toggleable elements to the list in `<li>` elements.

You can add a `<li class="divider"></li>` to create a thin horizontal border in your dropdown menu.

```html
<div class="dropdown">
	<button class="btn dropdown-toggle" data-toggle="dropdown">
       Open me 
    </button>
    <ul class="dropdown-menu">
        <li>Hello</li>        
        <li>World</li>
        <li class="divider"></li>
        <li>Thanks for opening me</li>
    </ul>
</div>
```



You can use the boostrap caret class `<span class="caret"></span>` to add a caret in your dropdown menu.



**Bootstrap collapses**

A collapsible element is an element that can be hidden and showed with a button.

To do so, just add the `class="collapse"` attribute to an element, and `data-toggle="collapse" data-target="<target_id>"` to the button that controls the collapse.

For example:

```html
<button data-toggle="collapse" data-target="#collapseme">Collapsible</button>

<div id="collapseme" class="collapse">
Lorem ipsum dolor text....
</div>
```



**Bootstrap navbar**

To create a navbar, add the `navbar` class to your `<nav>` or `<div>` navbar element. You can add one of the following additional classes:

- `navbar-default`
- `navbar-inverse`, to invert the colors of the navbar
- `navbar-fixed-top`/`navbar-fixed-bottom`, to fix it to the top/bottom



Navbar direct children (generally `<ul>` elements) should have `nav` and `navbar-nav` classes.

For example:

```html
<nav class="navbar navbar-default">
	<ul class="nav navbar-nav">
        <li>Page 1</li>
        <li>Page 2</li>
        <li>Page 3</li>
    </ul>
</nav>
```

> You can also put this navbar into a container or a fluid-container



Bootstrap provides some additional elements:

-  `navbar-form`
- `navbar-btn`
- `navbar-text`



You can add some subdivisions to your navbar, for example:

-  `navbar-header` will display some elements as a header, for example, the name of your site.
- `navbar-right` will right-align elements



Finally, if your navbar is too big, you can add the `collapse navbar-collapse` classes to a div of the navbar and control it with a `button class="navbar-toggle" data-toggle="collapse" data-target="#<div_to_collapse_id>"`.



**Bootstrap carousels**

Carousels are another awesome feature of bootstrap.

[Try it here](https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_carousel&stacked=h)

To build a carousel:

- First, add an outer div, with an id of your choice, the `carousel` and the `slide` classes, and the `data--ride="carousel"` attribute. Add all the carousel content in this div.
- The slides are in a specific div with class `carousel-inner`, each slide should be in another div with class `item`, it can be text or images. You need to add `active` class to one of the slide, to set the carousel on this slide by default. You can also add captions in a div with class `carousel-caption`. 
- The indicators: indicators are some little dots at the bottom which indicates how many slides there are and which one the user is currently viewing. Specify them in an ordered list with class `carousel-indicators`. Each indicator should have a `data-target` attribute (the id of the carousel div) and a `data-slide-to` attribute that specifies which slide to go to when clicking on the dot.
- The left and right controls are buttons that allows the user to slide back and forth, just add them in `<a>` elements, set `left`/`right` and `carousel-control` as classes, `data-slide="prev"`/`data-slide="next"` as attribute, and the id of the carousel div as value for the `href` attribute.



Carousel example:

```html
<div class="container">
  <h2>Carousel Example</h2>
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">

      <div class="item active">
        <img src="la.jpg" alt="Los Angeles" style="width:100%;">
        <div class="carousel-caption">
          <h3>Los Angeles</h3>
          <p>LA is always so much fun!</p>
        </div>
      </div>

      <div class="item">
        <img src="chicago.jpg" alt="Chicago" style="width:100%;">
        <div class="carousel-caption">
          <h3>Chicago</h3>
          <p>Thank you, Chicago!</p>
        </div>
      </div>
    
      <div class="item">
        <img src="ny.jpg" alt="New York" style="width:100%;">
        <div class="carousel-caption">
          <h3>New York</h3>
          <p>We love the Big Apple!</p>
        </div>
      </div>
  
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>
```



**Bootstrap modal box**

Modal box is a little popup window that is displayed on the top of the current page, it's perfect for some explanation on something.

To build it:

-  Create a modal box. This is the div that contain the modal window, create a div with the `modal` class, and an `id` of your choice. You can add an animation class like `fade`. Inside this div, create another div with class `modal-dialog` (this is to set the proper width and margin of the modal). you can add a size to this `modal-dialog`, by adding the `modal-sm` or `modal-lg` class.
- Insert the modal content: Inside the previous div (the `modal-dialog` one), you need to create the content of the modal window. Add a div with the `modal-content` class, inside this div, you can create a `modal-header`, a `modal-body` and a `modal-footer` div.

-  Create a trigger. A button/link that display this modal box, to do so, add the `data-toggle="modal"` and the `data-target="<modal_div_id>"` in the button attributes. 

For example:

```html
<!-- Trigger the modal with a button -->
<button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Open Modal</button>

<!-- Modal -->
<div id="myModal" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Modal Header</h4>
      </div>
      <div class="modal-body">
        <p>Some text in the modal.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>
```



**More on bootstrap**

Check the whole bootstrap tutorial on [w3schools](https://www.w3schools.com/bootstrap/).

