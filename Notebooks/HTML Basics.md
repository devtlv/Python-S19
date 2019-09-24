## HTML ?

HTML --> hypertext markup language.
Markup language: computer language that use tags to define elements.

Browsers like Chrome or Firefox are softwares that can read HTML files.
Every web page is an HTML page.

## HTML files structure

An HTML element is defined by a start tag and an end tag, with the content inserted between:
`<element-type>My element value</element-type>`

> Notice how a tag is closed with the slash
> Some tags don't need to be closed, they're called orphan tags: `<element />`

A HTML file is a text file with the `.html` extension, the code needs to start with `<!DOCTYPE html>`.
All the html code is inside an html element (`<html>`).

The html code is separated in two big parts, the `<head>` and the `<body>`.
The body is the visible part of the html code, while the head is here to add some config to the file.

## HTML elements

A lot of elements are available in HTML, here are some popular ones:

#### head elements:

`<title>` is used to define the title of the tab



#### headings

> Headings are used for titles and big texts

# `<h1>h1 heading</h1>`

## `<h2>h2 heading</h2>`

### `<h3>h3 heading</h3>`

#### `<h4>h4 heading</h4>`

##### `<h5>h5 heading</h5>`

###### `<h6>h6 heading</h6>`



#### HTML text elements:

`<p>I'm a paragraph</p>`

**`<b>I'm a bold paragraph</b>`**

*`<i>I'm an italic paragraph</i>`*



#### HTML divisions - Used to create sections in the code:

`<div><p>I'm in a division</p></div>`

`<p>I got two <span>sections</span></p>`



#### HTML separators:

New line: `<br>` 

Horizontal line: `<hr>`



#### HTML lists - Used to render a list of elements:

`<ul>` and `<ol>` tags can be used to define a list.
List elements needs to be in `<li>` tag.



#### HTML comments - They are here to comment the code, they won't be executed:

`<!-- My comment -->`