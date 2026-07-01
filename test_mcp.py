from app.agent import drive_test_agent

def test():
    print("Sending prompt to agent...")
    try:
        response = drive_test_agent("List the files in my drive root.")
        if hasattr(response, 'message'):
            print(response.message.content)
        else:
            print(response)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f'Error: {e}')

if __name__ == "__main__":
    test()
