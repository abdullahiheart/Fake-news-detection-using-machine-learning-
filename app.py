from flask import Flask, request, render_template
import pickle

# TfidfVectorizer
vector = pickle.load(open("vectorizer.pkl", 'rb'))

# saved model LogisticRegression
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        if predict == 1:
            predict = "warkan wa war sax ah"
        else:
            predict = "warkan wa war been abuur ah"

        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))
    else:
        return render_template("prediction.html")

if __name__ == '__main__':
    app.debug = True
    app.run()


# # from flask import Flask, escape, request, render_template
# from flask import Flask, request, render_template
# from markupsafe import escape

# import logging
# import pickle

# # Set up logging
# logging.basicConfig(level=logging.INFO)

# app = Flask(__name__)

# try:
#     # TfidfVectorizer
#     vector = pickle.load(open("vectorizer.pkl", 'rb'))

#     # saved model LogisticRegression
#     model = pickle.load(open("finalized_model.pkl", 'rb'))
# except Exception as e:
#     app.logger.error("Error loading model or vectorizer: %s", e)
#     raise e

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/prediction', methods=['GET', 'POST'])
# def prediction():
#     # Your existing logic here to set prediction_text
#     return render_template("prediction.html", prediction_text=prediction_text)

#     if request.method == "POST":
#         news = request.form.get('news', '')
#         if news:
#             try:
#                 predict = model.predict(vector.transform([news]))[0]
#                 if predict == 1:
#                     prediction_text = "News headline is -> warkan wa war sax ah"
#                 else:
#                     prediction_text = "News headline is -> warkan wa war been abuur ah"
#             except Exception as e:
#                 app.logger.error("Error in prediction: %s", e)
#                 prediction_text = "Error in processing the prediction."
#         else:
#             prediction_text = "No news headline provided."

#         return render_template("prediction.html", prediction_text=prediction_text)
#     else:
#         return render_template("prediction.html")

# if __name__ == '__main__':
#     app.run(debug=True)  # Set to False for production use
