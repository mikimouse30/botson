from flask import Flask,request

app = Flask(__name__)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    
    query_result = req.get('queryResult')
    intent = query_result.get('intent').get('displayName')
    print(intent)
    
    if intent == 'inquiry-address':
        fulfillmentText = "We are located at Unit 3B, Basic Petroleum Building, 104 C Don Carlos Palanca, Legazpi Village, Makati, Metro Manila"
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }

    if query_result.get('action') == 'get.foodrestaurant':
        fulfillmentText = "Hi there adasdasdasd"
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }

if __name__ == '__main__':
	app.run()