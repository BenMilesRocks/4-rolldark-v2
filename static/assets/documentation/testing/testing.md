# Scrum Maester -  Testing

![The Rolldark site shown on a variety of screen sizes]()

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

I used [W3C's HTML validator](https://validator.w3.org/) to check my code. This raised no issues, other than issues raised because of the Django syntax used (which can be safely ignored in a Django app).

**CSS Validation**

I used [W3C's Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to test my site's CSS, which showed no issues.

![WC3's Jigsaw Validator]()

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

![Lighthouse scores]()

- - -

## MANUAL TESTING

### Testing User Stories

**First Time Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |


**Returning Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |


**Frequent Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |

**Admin Users**

| **Goals** | **How are they achieved?** |
| --- | --- |

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


| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | ---- | --- | --- |
| **Home Page** | --- | --- | --- | --- |


- - -