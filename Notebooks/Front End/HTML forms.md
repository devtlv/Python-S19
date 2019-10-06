# HTML Forms

HTML Forms are required to collect different kinds of user inputs, such as contact details like name, email address, phone numbers, or details like credit card information, etc.

You can see HTML forms on (almost) every web site, like the "sign in" section.

Here is a simple form example:

```html
<form>
    <label>Username: <input type="text"></label>
    <label>Password: <input type="password"></label>
    <input type="submit" value="Submit">
</form>
```



#### Defining a form

To define a form, use the `<form>` element.



#### The input element

This is the most commonly used element within HTML forms.

The `<input>` tag allows you to specify various types of user input fields, depending on the `type` attribute. An input element can be of type:

- text field
- password field
-  checkbox
- radio button
- submit button
- reset button
- file select box

And a lot more !

To change the type of a field, pass the `type="<field_type>"` as attribute in the `<input>` element.

You can specify the `size` of the field by passing it in the attributes.



#### The label element

This element is created to define the *label* of a `<input>` element 