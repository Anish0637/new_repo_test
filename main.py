from langchain import OpenAI, ConversationChain
def main():
    llm = OpenAI(temperature=0.9)
    conversation = ConversationChain(llm=llm, verbose=True)
    conversation.run("Hi there!")       
if __name__ == "__main__":    
    main()