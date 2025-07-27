from collections import deque

history = deque(maxlen=5)
forward_stack = deque()

def add_page(url):
    history.append(url)
    forward_stack.clear() # Clear forward history on new navigation
    print_state()

def go_back():
    if len(history) > 1:
        page = history.pop()
        forward_stack.append(page)
        print(f"Back from: {page}")
    else:
        print("No page to go back")
    print_state()

def go_forward():
    if forward_stack:
        page = forward_stack.pop()
        history.append(page)
        print(f"Forward to: {page}")
    else:
        print("No forward page available")
    print_state()

def print_state():
    print("History:", list(history))
    print("Forward Stack:", list(forward_stack))


add_page("google.com")
add_page("wikipedia.org")
add_page("github.com")
add_page("stackoverflow.com")
add_page("python.org")

go_back()
go_back()

go_forward()

add_page("realpython.com")
add_page("reddit.com")  
    

