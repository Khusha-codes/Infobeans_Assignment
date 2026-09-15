import webbrowser

#webbrowser.open("https://github.com/Khusha-codes")

msg = input("Enter your Question: ")
call = "https://www.youtube.com/search?q=" + msg

webbrowser.open(call)