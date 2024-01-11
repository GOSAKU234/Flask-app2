# OpenAI-Flask-App
provides a solution to build and deploy a gpt chatbot with OpenAI API using Flask and docker.
The whole tutorial can be found at [Deploy a “ChatGPT” with OpenAI API on Microsoft Azure using Flask + Docker Step by Step](https://medium.com/@mengmengliu24/deploy-a-chatgpt-with-openai-api-on-microsoft-azure-using-flask-docker-step-by-step-d7470b930672)

To run the Flask app locally;
```
pip install -r requirements.txt
```

Replace the OpenAI key in the app.py:
```
api_key = 'OPENAI_API_KEY'
```

Run in the command line:
```
python app.py
```

To test it locally:
```
curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"are you a dog person or a cat person?\"}"  http://localhost:5000/
```

