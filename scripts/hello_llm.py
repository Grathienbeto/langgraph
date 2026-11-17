from app.llm import get_chat_model


def main():
    print("Hello, LLM")
    response = get_chat_model().invoke(input='Como se dice fabuloso en aleman')
    
    print(response.content)
    
    
    
if __name__ == '__main__':
    main()