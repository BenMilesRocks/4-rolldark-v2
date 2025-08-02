/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/


// Set session variables
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Call stripe variables
var stripe = Stripe(stripePublicKey);


// Set appearance and options
const appearance = {
    theme: 'flat'
};

const options = {
    layout: {
        type: 'accordion',
        defaultCollapsed: false,
        radios: false,
        spacedAccordionItems: true
    }
};

// Mount card element to div
const elements = stripe.elements({ clientSecret, appearance });
var card = elements.create('card', options);
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // prevent default action
    ev.preventDefault();

    // Disable card element and submit while code is running, preventing multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // Pass card details to Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // Pull billing details from form
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                    // No postcode, as Stripe will override this with postcode in Card element
                }
            }
        },
        // Pull shipping info from form
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {

        // If error, display message
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Re-enable card element & submit to allow user to try again
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            
        } else {
            // If success, submit form
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
