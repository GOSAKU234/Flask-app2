import openai

class ChatBot():
    def __init__(self, api_key, system_prompt):
        # OPENAI authentication
        self.OPENAI_API_KEY = api_key

        # model parameter
        self.system_prompt = system_prompt

        # initialize the message to send each time
        self.message = [{"role":"system","content":self.system_prompt}]
        
        # chat_history = [(user_msg, assist_msg), (user_msg, assist_msg), ...]
        self.chat_history = []
        
    def initialize(self):
        openai.api_key = self.OPENAI_API_KEY

    def request(self, new_query):
        # if the length of chat history >5, we only keep the the last 5 chat records 
        # in case we broke the company, the system prompt should always be in the msg
        if len(self.chat_history) > 5:
            self.chat_history = self.chat_history[-5:]

        for human, assistant in self.chat_history:
            self.message.append({"role":"user", "content":human})
            self.message.append({"role":"assistant", "content":assistant})
        
        if new_query != '':
            self.message.append({"role":"user", "content":new_query})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=self.message)

        # clean up the message list:
        self.message = [{"role":"system","content":self.system_prompt}]

        # update the chat_history
        self.chat_history.append([new_query, response["choices"][0]["message"]["content"]])

        return response.choices[0].message.content

# bot = ChatBot(api_key, "you are a helpful assistant.")
# bot.initialize()
# print(bot.request("Hi do you know who's the president of america?"))
