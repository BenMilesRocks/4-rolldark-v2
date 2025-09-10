# Rolldark Game Master Agency

![The Rolldark site shown on a variety of screen sizes](static/assets/documentation/screenshots/responsive-image.jpg)

Rolldark Game Master Agency are a UK based company who provide paid Game Masters for Table Top Roleplaying Games both online and in person, as well as provide supplimentary products like Dice and Dungeons and Dragons modules for customers to run themselves.

The business currently uses a variety of third party solutions to run its website, which they have shown an interest in consolodating into one solution. They have mentioned several challenges they currently face. By creating a website with a robust database, we can consolodate many of those solutions into one place with a great deal of scope for future expansion.

[The deployed version of the site is available here](https://rolldark-b52dc36be8e7.herokuapp.com/)

## Contents

* [User Experience](#user-experience)
    - [User Stories](#user-stories)
* [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframe](#wireframe)
    - [Database](#database)
* [Features](#features)
* [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment and Local Development](#deployment-and-local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
* [Testing](#testing)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
* [Credits](#credits)
    - [Code Used](#code-used)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## User Experience

### User Stories

---
|**End User Stories**| |
|---|---|
| **All Users** | I want the site to be responsive to my device |
| | I want the site to be easy to navigate |
| | I want to be able to check out quickly and easily if I make a purchase |
| | I want to be able to sort products according to my needs |
| **First Time User** | I want to quickly understand the services Rolldark Game Master Agency offer |
| | I want the user registration process to be quick and easy |
| **Returning User** | I want to be able to quickly navigate to the relevant part of the site for my needs |
| | I want the option to stay logged in for faster checkout |

---
| **Admin User Stories** | |
|---|---|
| **Purchases** | I want the site to automatically respond to customers, confirming purchases |
| | I want customers to be able to see previous purchases, allowing them to easily purchase the same items again |
| | I want customers to be able to contact us directly through the site, without the need to refer them to a 3rd party API |
| **Site Management** | I want to be able to add products to the site easily |
| | I want to be able to edit and delete products through the main site, not the admin panel |
| | I want to be able to select if a product is "Live" or not, allowing me to temporarily remove or edit products without deleting them from the database |
| | I want to edit the advertising on my homepage, informing customers of new products without the need for a webmaster |
| | I want to be able to create, edit and delete Game Master profiles, to keep the team info up to date easily |



## Design

### Color Scheme

Because of the nature of the site, I went with a bold, colourful palette for the project. I wanted customers to be intrigued and excited about the products on offer, and this seemed like the best way to achieve this.

![Rolldark Colour Palette](/static/assets/documentation/colour-palette.png)

### Typography

Because of the wide range of customers likely to visit the site, as well as the amount of images already vying for the customer's attention; I wanted to keep the fonts simple and easy to read to ensure they were not distracting to the user.

I decided to keep the Bootstrap default font family which uses Helvetica and Arial. Both are sans-serif fonts, making them clear and easy to read.

### Imagery

Because of the high-fantasy nature of the games on sale, it makes sense for the imagery on the site to use lots of bold, colourful images that elicit a sense of excitement in the customer. In addition to the product images, the main images on display are on the Home page and the About page.

*Home Page*

![Rolldark Background Image](/media/castle_background.webp)

![Call to Action Background](/media/doorway_background.webp)

*About Page*

![Rolldark Game Masters in action](/media/gala2.webp)

![Rolldark Game Masters in action](/media/gala3.webp)

![Rolldark Game Masters in action](/media/gala4.webp)

### Wireframe

### Database


## Features


## Accessibility


## Technologies Used

### Languages Used

### Frameworks, Libraries & Programs Used


## Deployment and Local Development

### Deployment

### Local Deployment


## Testing

Please refer to [testing.md](static/assets/documentation/testing/testing.md) for all testing carried out.

### Solved Bugs

| **No.** | **Bug** | **How I Solved The Issue** |
|:-------:|:-------:|:--------------------------:|
| 1 | Navbar does not correctly highlight currently open page | Used a conditional statement to check if the URL matches the open page, and applying the Bootstrap 'active' class if it does |
| 2 | TextField data from database does not display text formatting, making product descriptions difficult to read | Used the Django 'linebreaks' filter which preserves paragraphs, making the data easier to read |
| 3 | Game Master cards on the About page do not conform to the same height, making the layout messy | Added responsive height properties in CSS to ensure all the images conform to the same style |
| 3 | Add Product requires the user to understand JSON formatting, which would make it difficult for users to add Games to the database | I implemented code to dynamically create Date field inputs, and then a JavaScript function to input this data into the Game Dates field on behalf of the user |
| 4 | After checkout, Delivery Costs are sometimes incorrectly applied to products | Modified the update_total function to set delivery charge to 0 for each line item, ensuring delivery cost is calculated correctly |
| 5 | Product Detail page does not correctly calculate price for Dice products | Split the JavaScript function to display the total price into two functions - one for dice, one for games - to allow seperate handling for different products |

### Known Bugs

Most of the known bugs I have seen relate to the Add Product page. Although this would need addressing in a future version of the site, it seemed less important than the customer-facing issues on the site. The issue with Order Emails not sending occurred only during testing a couple days prior to the project being submitted.

| **No.** | **Bug** |
|:-------:|:-------:|
| 1 | Edit Product does not dynamically create date fields in the same way Add Product does |
| 2 | If adding a Game in Add Product and the form is invalid, it will remove the dynamically created Game Dates |
| 3 | Dynamically created Date fields do not match the styling of the rest of the page |
| 4 | Order Confirmation Emails are not sending on the deployed version of the site |


## Credits

### Code Used

I used code from [This Learn Django Article](https://learndjango.com/tutorials/django-email-contact-form-tutorial) to create the Contact form.

The Call to Action carousel on the Home page took its structure from an article on [Free Frontend.dev](https://freefrontend.dev/code/bootstrap/call-to-action/call-to-action-carousel/), before I added the dynamic elements from the database.

[This Stack Overflow Post](https://stackoverflow.com/questions/14853779/dynamically-creating-a-specific-number-of-input-form-elements) provided the code for dynamically creating Input Elements for the Add Product page.

For the Toasts, I took code from [CSS Tricks.com](https://css-tricks.com/snippets/css/css-triangle/) to add the triangle at the top of the Toast.

[This Stack Overflow Post](https://stackoverflow.com/questions/75371409/how-to-render-an-arbitrary-set-of-key-value-pairs-from-a-jsonfield-in-a-jinja2) provided code I used to display data from the JSONfield in my database, allowing the user to select from an array of Game Dates on the Product Detail page.

Finally, [This Stack Overflow Post](https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap) explained how to dynamically change the Active class for items on the navbar.


### Media

All images were taken from [The Current Rolldark Website](https://rolldark.co.uk/) and their [Instagram Page](https://www.instagram.com/RolldarkGMA).

### Acknowledgements
