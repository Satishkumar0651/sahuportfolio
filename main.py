from flask import Flask,render_template,request,jsonify
from ad_click_prediction.acp import predict_ads


app=Flask(__name__,static_folder="static",
          static_url_path="",template_folder="templates")

@app.route("/")
def index():
    """This function will render the index page"""
    return render_template("index.html")


@app.route("/ad_click_prediction")
def ad_click_prediction():
    """This function will render the Ad_Click_Prediction Page"""
    return render_template("ad_click_prediction.html")

@app.route('/predict_ads', methods=['POST'])
def predict():
    data = request.get_json()
    result = predict_ads(data)
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(info):
    """function will render the 404 page"""
    print(info)
    return render_template("index.html")




if __name__=="__main__":
    app.run(host="localhost",port="8080",debug=True)