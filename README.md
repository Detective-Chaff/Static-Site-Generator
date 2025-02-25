# Static-Site-Generator

This project generates html files based on any markdown files located in the project's "content" directory. It will inject the generated html into a base template and save it to a public directory that will mirror the content directory file structure.

It uses a basic markdown parser created from scratch with no 3rd party libraries.  Currently it only supports basic markdown syntax and does not allow for nested inline markdown elements such as:

> 1.  "***" -> ***bold and Italics***
> 2. **bold *with nested Italic* text**
> 3. *Italic **with nested Bold** text*

### Supported Mardown

This project supports the following markdown syntax:

> * Text containting non-nested inline elements such as
>
> * **bold text** with *Italic* and vice versa.
>
> * ![images] (path to image link here)
>
> * [whatever link you'd like] (link path here)
>
> * blockquotes such as what this list is in
>
> * lists, both ordered and unordered
> 
> * standard text
