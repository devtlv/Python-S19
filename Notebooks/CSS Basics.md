# CSS Basics

#### What is CSS

CSS stands for **C**ascading **S**tyle **S**heets.

While HTML define the structure of a web page. CSS describes how elements are displayed on the screen.

> HTML represent content, and CSS represent the appearance of the content



#### CSS Syntax

A CSS rule-set consists of a selector and some declarations.

The selector points to the HTML element you want to style. It can be a *html tag*, *class* or *id*.

Declarations are defined in a declaration block, surrounded by curly brackets `{}`,  each declaration includes a CSS property name and value in this format `name:value`, and ends with a semicolon `;`. 

You can also add comments, surrounded by `/*` and `*/`. 

For example:

```css
h1 {                           /* Selector */
color: blue;                   /* Declaration 1 */
font-size: 12px;               /* Declaration 2 */
}
```



#### CSS Stylesheets

CSS can be written in three different places.

First, it can be written in any HTML element:

`<h1 style="color:blue; font-size:12px;">Hello World</h1>`

Another way, a lot more readable, is to write css in a **stylesheet**, a **stylesheet** is a text file, with the `.css` extension. This text file will be read by the browser and the style will be applied on the web page.

You need to specify the path of your **stylesheet** in your html code if you want it to be executed:

```html
<html>
    <head>
        <link rel="stylesheet" href="/path/to/stylesheet.css"></link>
    </head>
    <body>
        <h1>Hello world</h1>
    </body>
</html>
```



CSS can also be written in the HTML page, but that is really deprecated.



#### CSS Simple Selectors

CSS selectors are used to "find" (or select) the HTML elements you want to style.



We can divide CSS selectors into five categories:

-   Simple selectors (select elements based on name, id, class)

-  [Combinator selectors](https://www.w3schools.com/css/css_combinators.asp) (select elements based on a specific relationship between them)

- [Pseudo-class selectors](https://www.w3schools.com/css/css_pseudo_classes.asp) (select elements based on a certain state)

-  [Pseudo-elements selectors](https://www.w3schools.com/css/css_pseudo_elements.asp) (select and style a part of an element)

- [Attribute selectors](https://www.w3schools.com/css/css_attribute_selectors.asp) (select elements based on an attribute or attribute value)



**Element Selector:**

Element selector selects HTML elements based on the element name (tag). 

For example, this style will be applied on every `<p>` tag:

```css
p{
	color: red;
}
```



**HTML id and class:**

HTML elements can have a `class` attribute, used to define equal styles for elements with the same class name. Elements can also have a unique `id` attribute.



**Id Selector**

The **id selector** uses the `id` attribute of HTML element, to use it, write a hash `#` character, followed by the id of the element.

For example, to style this paragraph `<p id="my_paragraph">Hello World</p>`, use:

```css
#my_paragraph{
    color: red;
}
```



**Class Selector**

While the **class selector** uses the `class` attribute of the elements, to use it, write a dot `.` followed by the class of the element.

For example, to style this image `<img class="my_img" src="google.images/afkajenq.png"/>`, use:

```css
.my_img{
    width: 200px;
    height: 200px;
}
```



**Universal Selector**

**Universal selector** is also available, in css (and in a lot of computer languages), `*` means "Everything"

This style will be applied on every html elements of the page:

```css
* {
    color: blue;
}
```



**Grouping Selector**

You can style more than one element at the time, just separate each selector with a comma `,`:

```css
h1, h2, p {
  color: red;
}
```



#### CSS Properties

**Colors**

In css, colors can be Hexadecimal Color Codes (`#ffffff`), rgb (`rgb(255,255,255)`), or color names (`black`).



**Backgrounds**

You can use CSS to add a background to your sections, it can be a `background-color` or a `background-image`.

`background-image` should receive a url to work.

```css
body{ 
    background-image: url("my_img.png")
}
```



**Borders**

The CSS `border` properties allow you to specify the `border-style`, `border-width`, and `border-color` of an element's border.

```css
p {
  border-style: solid;
  border-width: 5px;
  border-color: green;
}
```



**Margins**

The CSS `margin` properties are used to create space around elements, outside of any defined borders.

You can specify the width of `margin` for every side, but you can also specify the margin for each side of the element.

```css
p {
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 150px;
  margin-left: 80px;
}
```



**Padding**

The CSS `padding` properties are used to generate space around an element's content, inside of any defined borders.

It works the same way as `margin`.

See the [box model](https://www.w3schools.com/css/css_boxmodel.asp) to understand `padding` and `margin`



**Elements dimensions**

The `height` and `width` properties are used to set the height and width of an element.



**Text styling**

You can specify the `color` of the text, but also the alignment (with `text-align`), the `text-decoration`, the `text-transformation`, the `text-indent` and [much more](https://www.w3schools.com/css/css_text.asp)

```css
p {
    color: blue;
    text-align: justify;
    text-indent: 50px;
    text-decoration: underline;
    text-transformation: uppercase;
}
```



 **List styling**

You can modify the icon in front of each list elements, with `list-style-type` to use a built in icon, or with `list-style-image` to add an image of your own. 



**Elements display**

You can modify the way elements are displayed.

The `display` property is controlling the layout of an element.

Block level: `display: block;` will display the element as a block, meaning stretch it out to the left and right as far as possible, and the next element will be placed below it.

Inline: `display: inline;` elements don't start on a new line and only take up as much width as necessary.

Inline block: `display: inline-block` allows to set a width and height on the element, and respect the padding, but doesn't add a line break after the element.

None: `display: none` won't display the element.

> Careful: It will not hide it (meaning it won't keep a blank place for the element), to hide an element, use `visibility: hidden`

See [this](https://www.w3schools.com/css/tryit.asp?filename=trycss_inline-block_span1) for a better understanding



**Elements position**

The `position` property specifies the type of positioning method used for an element (static on the page, relative to his parent, etc..)

It can be:

- `static`: Always positioned according to the normal flow of the page
- `relative`: Position the element relative to its normal position, you can add `left`, `right`, `top` or `bottom` arguments to add a gap by the element.
- `fixed`: Always stays in the same place even if the page is scrolled, `left`, `right`, `top` and `bottom` are used to position the element
- `absolute`: Always stays in the same place relative to his parent.
- `sticky`: The element won't leave the page, it will be positioned relative until he reaches the edge of the window, then it "sticks" to it.



**Dealing with overflow**

The `overflow` property specifies whether to clip the content or to add scrollbars when the content of an element is too big to fit in the specified area.

It can be:

- `visible` - Default. The overflow is not clipped. The content renders outside the element's box
- `hidden` - The overflow is clipped, and the rest of the content will be invisible
- `scroll` - The overflow is clipped, and a scrollbar is added to see the rest of the content
- `auto` - Similar to `scroll`, but it adds scrollbars only when necessary



#### CSS Combinators Selectors

**Descendant Selector**

The descendant selector matches all elements that are descendants of a specified element (meaning they are nested in it).

The following example selects all <p> elements inside <div> elements: 

```css
div p {
  background-color: yellow;
}
```



**Child Selector**

The child selector selects all elements that are the direct descendant of a specified element.

The following example selects all <p> elements that are children of a <div> element:

```css
div > p {
  background-color: yellow;
}
```



**Sibling Selector**

The general sibling selector selects all elements that are siblings of a specified element.

Sibling means "that have the same parent".

The following example selects all <p> elements that are siblings of <div> elements: 

```css
div ~ p {
  background-color: yellow;
}
```



**Adjacent Sibling Selector**

The adjacent sibling selector selects all elements that are the adjacent siblings of a specified element.

"Adjacent" means "immediately following".

The following example selects all <p> elements that are placed immediately after <div> elements:

```css
div + p {
  background-color: yellow;
}
```



#### CSS Pseudo Class Selectors

A pseudo class is used to style an element when he is in a special state (for example, when the user mouses over it)

The syntax is : `element:pseudo-class {...}`

**hover**

`hover` means "mouse is over it", for example, to change the color of a div when the mouse go over it:

```css
div:hover {
  background-color: blue;
}
```



**children**

You can target elements only if they are the *n*th child of their parent. For example, to style `<p>` tags that are the first child of another element, use:

```
p:first-child{
  color: blue;
}
```

The same thing works with `last-child` or `nth-child(n)`



**not**

The `not` pseudo class allows you to exclude elements, for example, select all the div that are not of the `ignore` class

```css
div:not(.ignore){
    background-color: yellow;
}
```



For more, see [this](https://www.w3schools.com/css/css_pseudo_classes.asp).



#### Flexbox

The Flexible Box Layout Module, makes it easier to design flexible responsive layout structure without using float or positioning.

To activate it, style the parent container with `display: flex`.

To see the flex properties and their uses, check this [awesome illustrated documentation](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) from css-tricks.







* 

* 