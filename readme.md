# Email Spam Detector made with Scikit Learn

This is a sklearn model that detects wheater or not an inputed email is a spam or not. This model was made for my resume and deploys a website where you can copy & paste emails to see if its spam.

This webstie can found at: https://email-spam-detector-d811.onrender.com/

This project has the following steps:
1. Sklearn Pipeline with Naive Bayes Model and Vectorizer
2. Front End Webpage created using Streamlit
3. Dockerzation of app using Docker
4. CI/CD using Github that pushes new versions of docker image when CI passes
5. Website hosted on Render

## How to Use
This website is quite straight forward. 
1. Go to https://email-spam-detector-d811.onrender.com/
2. Copy and Paste an email from your inbox
3. Press Submit and it will tells you wheater or not its spam