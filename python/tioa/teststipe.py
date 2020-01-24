# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_q4fdg9hqru6omjpKGPieHxFz00UrmxTA5l'

session = stripe.checkout.Session.create(
  payment_method_types=['card'],
  subscription_data={
    'items': [{
      'plan': 'plan_123',
    }],
  },
  success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
  cancel_url='https://example.com/cancel',
)