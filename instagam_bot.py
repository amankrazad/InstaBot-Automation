#                                  <---instagram Automation Bot--->

from instabot import Bot

bot = Bot()
bot.login(username = input("enter your username:"),password = input("enter your password:"))

print("\nwhat you want to Do?")
print("follow, unfollow, message, upload_photo, upload_video")


command = input("\nenter your command:")

if command == "follow":
    bot.follow(input("enter username that you want to follow:"))

elif command == "unfollow":
    bot.unfollow(input("enter username that you want to unfollow:"))

elif command == "message":
    bot.send_message(input("enter massage that you want to send:"),input("enter username you want to send:"))

elif command == "upload_photo":
    bot.upload_photo(input("paste the path of the photo:"),caption = input("entr your caption:"))

elif command == "upload_video":
    bot.upload_video(input("paste the path of the photo:"),caption = input("entr your caption:"))
else:
    print("unexpected command")