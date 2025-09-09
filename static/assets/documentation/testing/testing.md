# Rolldark -  Testing

![The Rolldark site shown on a variety of screen sizes](static/assets/documentation/screenshots/responsive-image.jpg)

Visit the deployed site: [Scrum Maester](https://rolldark-b52dc36be8e7.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Python Linter](#python-linter)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. During development I made use of Google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome developer tools & Microsoft Edge inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

**HTML Validation**

I used [W3C's HTML validator](https://validator.w3.org/) to check my code. This raised a couple issues, most of which were raised erroneously due to the way the data is pulled from django.

![WC3's HTML Validator](static/assets/documentation/testing/validation/w3c-full.png)

![WC3's HTML Validator](static/assets/documentation/testing/validation/w3c-1.png)

This attribute was added to the Main Logo for the benefit of screen readers, as labelling the 'div' parent element could potentially cause more confusion and layout issues.

![WC3's HTML Validator](static/assets/documentation/testing/validation/w3c-2.png)

For some reason, W3C's validator seems to see an empty 'H2' element in the page footer. This is not in my code, and it is unclear where it is seeing this element from. As it is not causing any issues with the site I decided not to alter anything about my code.

![WC3's HTML Validator](static/assets/documentation/testing/validation/w3c-3.png)

This javascript was written inline to ensure the Toasts worked properly on all pages. Removing this 'type' attribute caused the script to fail, so I decided to leave this attribute in my code.

![WC3's HTML Validator](static/assets/documentation/testing/validation/w3c-4.png)

These errors seem to be raised due to how the code is loaded in Django - the base element leaves the 'page-container' div element open to include the HTML from the relevant page and then closes it after this content has been loaded. It would seem that the validator does not read the code in this order, and as such is raising the error incorrectly. Inspecting the HTML with Google Chrome's developer tools shows these tags have been closed properly, so no action is necessary.

**CSS Validation**

I used [W3C's Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to test my site's CSS, which showed no issues.

![WC3's Jigsaw Validator](static/assets/documentation/testing/validation/jigsaw-validation.png)

- - -

### Python Linter

I used [The Pylint extension for VS Code](https://www.pylint.org/) to ensure my code was up to PEP-8 standards. Most of the issues raised by this were "E1101 - Instance has no Member", which were raised erroneaously 
because the objects were created dynamically (and as such can be safely ignored).

**App name**

File Name

![image of file scanned]()

Explaination of issues ignored


- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. The site scored highly across the board:

![Lighthouse scores](/static/assets/documentation/testing/lighthouse/index-lh-full.jpg)

The main issue flagged was the use of 3rd party cookies, which are part of the Stripe API and not something I am capable of altering.

![Lighthouse scores - Best Practices](static/assets/documentation/testing/lighthouse/index-lh-bp.png)

- - -

## MANUAL TESTING

### Testing User Stories

**All Users**
| **Goals** | **How are they achieved?** |
| --- | --- |
| I want the site to be responsive to my device | The site has been tested on a range of devices to ensure it is responsive to multiple screen sizes |
| I want the site to be easy to navigate | The navigation bar is clearly labled, to make it as simple as possible to navigate |
| I want to be able to check out quickly and easily if I make a purchase | Toasts pop up after each item is added to the cart, inviting user to go to the Checkout quickly. Purchases can be made whilst logged out, for ease of use |
| I want to be able to sort products according to my needs | The site is split into two simple categories - Games and Dice. This makes it easy for customers to find the type of product they are looking for, whilst still giving control over what products are displayed |

**First Time Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |
| I want to quickly understand the services Rolldark Game Master Agency offer | The home page has multiple, clear call to action elements to inform users about products that are available |
| I want the user registration process to be quick and easy | User registration is as simple as possible, with verification being automated for conveneince |

**Returning Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |
| I want to be able to quickly navigate to the relevant part of the site for my needs | The nav bar is split into simple, easy to understand elements to make it easy to navigate to the part of the site you want |
| I want the option to stay logged in for faster checkout | The site remembers previous users, and keeps them logged in unless they actively log out. There is also the option to save delivery info for faster checkout |


**Admin Users**

*Purchases*

| **Goals** | **How are they achieved?** |
| --- | --- |
| I want the site to automatically respond to customers, confirming purchases | The site has automated messages enabled, confirming user registration and purchases automatically |
| I want customers to be able to see previous purchases, allowing them to easily purchase the same items again | The User Profile shows their order history, allowing them to see what items they have purchased before |
| I want customers to be able to contact us directly through the site, without the need to refer them to a 3rd party API | The site has a Contact form that emails the admin team directly, without the need for 3rd party APIs or navigation away from the site |

*Site Management*

| **Goals** | **How are they achieved?** |
| --- | --- |
| I want to be able to add products to the site easily | The site has an Add Product page, allowing ease of product creation |
| I want to be able to edit and delete products through the main site, not the admin panel | The site has full CRUD functionality for products |
| I want to be able to select if a product is "Live" or not, allowing me to temporarily remove or edit products without deleting them from the database | Products have a "product_live" value, which allows Admin users to remove a product from active view if needed |
| I want to edit the advertising on my homepage, informing customers of new products without the need for a webmaster | The Edit Call to Action page allows Admin users to dynamically create advertising, with full CRUD functionality |
| I want to be able to create, edit and delete Game Master profiles, to keep the team info up to date easily | The site allows full CRUD functionality for all Game Master details, allowing the site to dynamically populate the Game Master details shown on the About Us page |

- - -

### Full Testing

Full testing was performed on the following devices:

Desktop:
<ul><li>HP Envy All-in-one 32-a10</li></ul>

Mobile Devices:

<ul>
<li>Samsung Galaxy S20 FE</li>
<li>Samsung A20</li>
</ul>


Each device tested the site using the following browsers:

* Google Chrome
* Microsoft Edge
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. They reported no issues when using the site.

All testing below was performed on both my local development environment and the deployed version of the site, to ensure thoroughness of testing.

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| **Navbar** | --- | --- | --- | --- |
| Main Logo | Should redirect to Home page | Clicked Logo in Home, Games, Dice, About, Contact, Profile, Add Product & Cart pages | Redirects to Home page | **PASS** |
| Nav Items Hover | Item should show underline when hovered over | Hovered over nav items | Nav items display underline correctly | **PASS** |
| Nav Items Dropdown | More Info, Your Account and Site Management should open a dropdown menu when clicked | Clicked More Info, Your Account and Site Management tabs | Dropdown opened as expected | **PASS** |
| Nav Item Links | Nav Items should redirect to their appropriate pages | Clicked each Nav Item | Redirected to the correct page | **PASS** |
| Account Info | When logged in, Your Account should display account options. When logged out this should be replaced by links to Register / Log In | Signed in as user, clicked Your Account. Logged out, clicked links for Register / Log In | Links displayed as expected | **PASS** |
| Site Admin | When user is logged in as Super User, site admin should display. When logged out or logged in as normal user, site admin should be hidden | Logged in as Superuser, logged out, logged in as normal user | Site admin displayed for Superuser, did not display for logged out or regular user | **PASS** |
| Cart Total | When items are added to the cart, the total should update to the correct price | Added items to cart | Cart total updated correctly | **PASS** |
| --- | --- | --- | --- | --- |
| **Toasts** | --- | --- | --- | --- |
| Display Toasts | When messages are passed from backend, toast should display | Added product to cart, viewed previous order, filled in Add Product Form incorrectly | Toast for success, alert and warning displayed correctly | **PASS** |
| Cart Summary | Toast Success should show summary of items in cart | Added items to cart | Cart summary displayed correctly | **PASS** |
| --- | --- | --- | --- | --- |
| **Footer** | --- | --- | --- | --- |
| Links | Links for Discord, Facebook, YouTube and Instagram should open in new tabs | Clicked each link | Links opened correctly in a new tab | **PASS** |
| Positioning | Links should display below main content, should not overlap with page content | Visited all pages | Links displayed correctly underneath main content at the bottom of the page | **PASS** |
| --- | --- | --- | --- | --- |
| **Home Page** | --- | --- | --- | --- |
| Call to Action link | "Get a Quote Today!" button should redirect to Contact Us page | Clicked button | Redirected to Contact Us page | **PASS** |
| Call to Action Carousel | Should display items from the database and links to each item | Clicked scroll buttons, clicked links on carousel | Carousel scrolls with appropriate buttons, links redirect to relevant products | **PASS** |
| --- | --- | --- | --- | --- |
| **Games Page** | --- | --- | --- | --- |
| Game Card | Games should be displayed dynamically, showing *only* products marked in the database as 'Game' | Opened Games page | Games displayed correctly, non-Game products not displayed | **PASS** |
| Edit & Delete buttons Display | Edit & Delete product buttons should only show for Superuser | Logged in as Superuser, logged out, logged in as normal user | Edit & Delete buttons showed for Superuser, did not display for other users | **PASS** |
| Edit button | Should navigate to Edit Product page, with relevant product info | Clicked Edit button while logged in as Superuser | Loads Edit Product page with correct product info | **PASS** |
| Delete button | Should bring up modal confirming product deletion | Clicked Delete button | Modal displayed correctly | **PASS** |
| Delete Modal | Cancel button should close modal, delete button should delete the relevant product | Clicked cancel, clicked delete | Cancel closes modal, Delete button deletes the correct product from database | **PASS** |
| Product link | Should redirect to product_detail page with relevant product information | Clicked Product link | Redirected to product_detail, with correct product info loaded | **PASS** |
| --- | --- | --- | --- | --- |
| **Dice Page** | --- | --- | --- | --- |
| Product Card | Games should be displayed dynamically, showing *only* products NOT marked in the database as 'Game' | Opened Dice page | Dice displayed correctly, Game products not displayed | **PASS** |
| Edit & Delete buttons Display | Edit & Delete product buttons should only show for Superuser | Logged in as Superuser, logged out, logged in as normal user | Edit & Delete buttons showed for Superuser, did not display for other users | **PASS** |
| Edit button | Should navigate to Edit Product page, with relevant product info | Clicked Edit button while logged in as Superuser | Loads Edit Product page with correct product info | **PASS** |
| Delete button | Should bring up modal confirming product deletion | Clicked Delete button | Modal displayed correctly | **PASS** |
| Delete Modal | Cancel button should close modal, delete button should delete the relevant product | Clicked cancel, clicked delete | Cancel closes modal, Delete button deletes the correct product from database | **PASS** |
| Product link | Should redirect to product_detail page with relevant product information | Clicked Product link | Redirected to product_detail, with correct product info loaded | **PASS** |
| --- | --- | --- | --- | --- |
| **Product Detail Page** | --- | --- | --- | --- |
| Product info | Should display the information for *only* the selected product | Loaded multiple different Product Detail pages | Product info displayed correctluy| **PASS** |
| Product image | Should display on right side for larger screens, on top for smaller displays | Resized screen | Displayed on right side for larger screen, on top for smaller screen | **PASS** |
| Ticket Option select box (display) | Should only display for Games | Opened Game product, opened Dice product | Select box showed for Games, not for Dice product | **PASS** |
| Ticket Option | Should add specified ticket option to cart | Selected Ticket Option, added to cart | Product showing in cart correctly | **PASS** |
| Campaign Ticket | Should display price for campaign ticket (Number of dates * Price per game) | Selected Campaign ticket, selected multiple quantities | Total price updated correctly, added to cart with correct option | **PASS** |
| Quantity | Should add mulitple products to cart, should update Total Price | Selected multiple different quantities | Added product quantities to cart correctly, total price displayed correctly at bottom of page | **PASS** |
| Subtotal & delivery charge display | Should only display on items which have a delivery charge | Opened products with delivery charge, opened products without delivery charge | Only displays on items which have a delivery charge | **PASS** |
| Subtotal | Should update dependant on quantity | Selected multiple different quantities | Displayed subtotal correctly | **PASS** |
| Deluvery | Should update dependant on quantity | Selected multiple different quantities | Displayed delivery correctly | **PASS** |
| Total | Should update dependant on quantity | Selected multiple different quantities | Displayed Total correctly | **PASS** |
| Add to cart | Should add product quantity & selected options to cart | Clicked add to cart on multiple products, with different options & quanities selected | Added to cart correctly | **PASS** |
| --- | --- | --- | --- | --- |
| **About Page** | --- | --- | --- | --- |
| Image carousel | Should display images, automatically scroll and scroll with user input | Loaded page, clicked scroll buttons | Images loaded, scrolled automatically. Scroll buttons manually scrolled through images | **PASS** |
| Call to Action links | Contact Us should redirect to contact page, Browse Games should redirect to Games page | Clicked links | Contact Us redirects to contact page, Browse Games redirects to Games page | **PASS** |
| Game Master Cards | Game Master cards should be generated dynamically from database, populating page | Navigated to About Us page | Game Master cards displayed correctly | **PASS** |
| More Info links | More Info should open a modal with info about the selected Game Master | Clicked More Info links | Opened modal with info about Game Master, populated from database | **PASS** |
| Edit & Delete buttons Display | Edit & Delete product buttons should only show for Superuser | Logged in as Superuser, logged out, logged in as normal user | Edit & Delete buttons showed for Superuser, did not display for other users | **PASS** |
| Edit button | Should navigate to Edit Game Master page, with relevant Game Master info | Clicked Edit button while logged in as Superuser | Loads Edit Game Master page with correct Game Master info | **PASS** |
| Delete button | Should bring up modal confirming Game Master deletion | Clicked Delete button | Modal displayed correctly | **PASS** |
| Delete Modal | Cancel button should close modal, delete button should delete the relevant game master | Clicked cancel, clicked delete | Cancel closes modal, Delete button deletes the correct game master from database | **PASS** |
| --- | --- | --- | --- | --- |
| **Contact Page** | --- | --- | --- | --- |
| Form Validation | Form should not submit with blank fields, whitespace validation or an invalid email address | Tried submitting form with blank fields, fields filled with whitespace & invalid email address | Form would not submit, displayed error on relevant field | **PASS** |
| Submit Button | Should redirect to contact/success page | Submitted valid form | Redirected to success page | **PASS** |
| Messages | Message should be sent to email address stored in global variables | Submitted valid form | Email received successfully | **PASS** |
| --- | --- | --- | --- | --- |
| **Message Sent Page** | --- | --- | --- | --- |
| Browse Games button | Should redirect to the Games page | Clicked button | Redirects to Games page | **PASS** |
| --- | --- | --- | --- | --- |
| **Profile Page** | --- | --- | --- | --- |
| Order History | Links should open previous order details | Clicked links for previous orders | Order summary displayed correctly, along with Toast to inform this is an old order | **PASS** |
| Default Delivery Information | Should display any saved delivery info | Opened Profile page | Default Delivery info displayed correctly | **PASS** |
| Update Information | Form should update delivery info on database | Changed delivery info, clicked UPDATE INFORMATION button | New delivery info saved to database | **PASS** |
| --- | --- | --- | --- | --- |
| **Log Out Page** | --- | --- | --- | --- |
| Log Out button | Should log user out | Clicked Log Out button | User logged out successfully | **PASS** |
| --- | --- | --- | --- | --- |
| **View All Products Page** | --- | --- | --- | --- |
| Product Card | Products should be displayed dynamically, showing all products | Opened Games page | Products displayed correctly, all product categories included | **PASS** |
| Edit & Delete buttons Display | Edit & Delete product buttons should only show for Superuser | Logged in as Superuser, logged out, logged in as normal user | Edit & Delete buttons showed for Superuser, did not display for other users | **PASS** |
| Edit button | Should navigate to Edit Product page, with relevant product info | Clicked Edit button while logged in as Superuser | Loads Edit Product page with correct product info | **PASS** |
| Delete button | Should bring up modal confirming product deletion | Clicked Delete button | Modal displayed correctly | **PASS** |
| Delete Modal | Cancel button should close modal, delete button should delete the relevant product | Clicked cancel, clicked delete | Cancel closes modal, Delete button deletes the correct product from database | **PASS** |
| Product link | Should redirect to product_detail page with relevant product information | Clicked Product link | Redirected to product_detail, with correct product info loaded | **PASS** |
| --- | --- | --- | --- | --- |
| **Add New Product Page** | --- | --- | --- | --- |
| Form Validation | Should display errors if form not filled in correctly, should not submit form | Filled in form with errors | All errors displayed correctly, form not submitted | **PASS** |
| Cancel button | Should redirect to View All Products | Clicked Cancel button | Redirects to View All Products | **PASS** |
| Add Product | Should add product to database | Filled in form, clicked Add Product | Product added to database | **PASS** |
| --- | --- | --- | --- | --- |
| **Add Call to Action Page** | --- | --- | --- | --- |
| Form Validation | Should display errors if form not filled in correctly, should not submit form | Filled in form with errors | All errors displayed correctly, form not submitted | **PASS** |
| Cancel button | Should redirect to Home page | Clicked Cancel button | Redirects to Home page | **PASS** |
| Add Call to Action | Should add Call to Action to database | Filled in form, clicked Add Call to Action | Call to Action added to database | **PASS** |
| Dark Text toggle | Should display Call to Action with dark text instead of light text | Clicked Dark Text toggle, saved Call to Action | Call to Action displayed with Dark Text | **PASS** |
| --- | --- | --- | --- | --- |
| **Edit Call to Action Page** | --- | --- | --- | --- |
| Call to Action details | Existing data should be populated in fields | Clicked Edit Call to Action | Info loaded correctly | **PASS** |
| Form Validation | Should display errors if form not filled in correctly, should not submit form | Filled in form with errors | All errors displayed correctly, form not submitted | **PASS** |
| Cancel button | Should redirect to Home page | Clicked Cancel button | Redirects to Home page | **PASS** |
| Edit Call to Action | Should edit existing Call to Action | Filled in form, clicked Edit Call to Action | Call to Action details changed | **PASS** |
| Dark Text toggle | Should display Call to Action with dark text instead of light text | Clicked Dark Text toggle, saved Call to Action | Call to Action displayed with Dark Text | **PASS** |
| --- | --- | --- | --- | --- |
| **View all Actions Page** | --- | --- | --- | --- |
| Call to Action cards | Should display all call to action items on database | Opened View all Actions page | Call To Action cards displaying correctly | **PASS** |
| Edit button | Should load Edit Call to Action page, with the relevant data lodaded | Clicked Edit button on multiple Call to Actions | Redirected to Edit Call to Action page, with correct info loaded | **PASS** |
| Delete button | Should bring up modal confirming Call to Action deletion | Clicked Delete button | Modal displayed correctly | **PASS** |
| Delete Modal | Cancel button should close modal, delete button should delete the relevant Call to Action | Clicked cancel, clicked delete | Cancel closes modal, Delete button deletes the correct Call to Action from database | **PASS** |
| Call to Action link | Should redirect to Edit Call to Action page with relevant Call to Action information | Clicked Call to Action link | Redirected to Edit Call to Action, with correct Call to Action info loaded | **PASS** |
| --- | --- | --- | --- | --- |
| **Add Game Master Page** | --- | --- | --- | --- |
| Form Validation | Should display errors if form not filled in correctly, should not submit form | Filled in form with errors | All errors displayed correctly, form not submitted | **PASS** |
| Cancel button | Should redirect to About Us page | Clicked Cancel button | Redirects to About Us page | **PASS** |
| Add Game Master | Should add Game Master to database | Filled in form, clicked Add Game Master | Game Master added to database | **PASS** |
| --- | --- | --- | --- | --- |
| **Cart Page** | --- | --- | --- | --- |
| Cart Summary | Should display summary of items in cart, if empty should display links to purchase Games & Dice | Opened page with empty cart, added items to cart | Displays summary of items in cart, if empty displays links to purchase Games & Dice | **PASS** |
| Update button | Should update quantity of item to selected amount | Selected new quantity, clicked update | Updated quantity of item in cart | **PASS** |
| Delete button | Should open modal confirming delete | Clicked Delete button | Modal opened successfully | **PASS** |
| Totals | Should update with the subtotal, cart total, delivery cost and Grand Total depending on items in cart | Added items to cart, both with and without delivery costs | Updates with the subtotal, cart total, delivery cost and Grand Total depending on items in cart | **PASS** |
| Checkout Button | Should redirect to Checkout page | Clicked Checkout button | Redirected to Checkout page | **PASS** |
| --- | --- | --- | --- | --- |
| **Checkout Page** | --- | --- | --- | --- |
| Cart Summary | Should display summary of items in cart | Opened Checkout page | Displays summary of items in cart | **PASS** |
| Form Validation | Should display errors if form not filled in correctly, should not submit form | Filled in form with errors | All errors displayed correctly, form not submitted | **PASS** |
| Save delivery info | On form submit should save details to user's profile | Checked save delivery info, completed order | Info saved to profile correctly | **PASS** |
| Adjust Cart | Should redirect back to Cart page | Clicked Adjust Cart | Redirected to Cart page | **PASS** |
| Complete Order | Should process order, redirect to Order Summary | Clicked Complete Order | Order proccessed & saved on database, redirected to Order Summary page | **PASS** |
| Confirmation Email | On order completion should send confirmation email to user | Clicked Complete Order | Email received on local host, but does not send in production server | **FAIL** |
| --- | --- | --- | --- | --- |
| **Checkout Success Page** | --- | --- | --- | --- |
| Order Summary | Should display order summary | Proccessed order | Order Summary displayed correctly | **PASS** |
| --- | --- | --- | --- | --- |

- - -