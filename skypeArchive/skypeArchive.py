from skpy import Skype, SkypeGroupChat, SkypeSingleChat
import sys

dict_list = []
input_login = sys.argv[1]
input_password = sys.argv[2]
input_file_name = sys.argv[3] if len(sys.argv) > 3 else "skype_chat_archive.txt"


class SkypeArchive:
    def __init__(self, login, password, file):
        self.login = login
        self.password = password
        self.file = file

    def get_chats(self):
        skype_username = self.login
        skype_password = self.password
        sk = Skype(skype_username, skype_password)
        i = 0
        for chat in sk.chats.recent():
            group = sk.chats[chat]
            if not isinstance(group, SkypeSingleChat):
                dictionary = dict(id=i, topic=group.topic, chat_id=chat)
                i += 1
                dict_list.append(dictionary)
                print(dict_list[i - 1])
        instance.create_archive()

    def create_archive(self):
        skype_username = self.login
        skype_password = self.password
        sk = Skype(skype_username, skype_password)
        user_input = int(input("Choose the chat ID: "))
        conversation_id = dict_list[user_input]["chat_id"]
        conversation = sk.chats[conversation_id]
        j = 0

        def get_display_name(user_id):
            try:
                user_profile = sk.contacts[user_id]
                return user_profile.name
            except KeyError:
                return user_id

        with open(input_file_name, "w", encoding="utf-8") as file:
            while True:
                messages = conversation.getMsgs()
                if not messages:
                    break

                for msg in messages:
                    if type(msg.userId) is None:
                        print("Done")
                        break
                    display_name = get_display_name(msg.userId)
                    file.write(f"{display_name} {msg.time}\n")
                    file.write(f"{msg.content}\n")
                    file.write("-" * 50 + "\n")
                    print(f"Processing message {j}")
                    j += 1


instance = SkypeArchive(input_login, input_password, input_file_name)
instance.get_chats()

