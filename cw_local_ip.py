import socket

class cowsay():

    def __init__(self):
        # Get the IPv4 address of the device using the getaddrinfo() method
        self.Your_ipv4 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[0][4][0]
        # Create the prompt string with the IPv4 address
        self.PROMPT_IPV4 = f'Your ipv4 address is {self.Your_ipv4}'
        # Define the border characters and the settings for the speech balloon
        self.border = {'TopCornerLeft': "┌", 'separator': '-', 'TopCorneRight':"┐",
                       'sideleft': '|', 'sideright': '|',
                       'DownCornerLeft': "└", 'DownCorneRight':"┘",}
        self.settings_cowsay = {'height': 8, 'width': 0, 'wide': 2}
        # Define the cow ASCII art
        self.cow = ["\n",
                    "^__^\n",
                    "(oo)______\n",
                    "(__)      )\\\n",
                    "   ||---w|| *"]
        # Set the width of the speech balloon based on the length of the prompt string
        if len(self.PROMPT_IPV4) >= self.settings_cowsay['width']:
            self.settings_cowsay['width'] = len(self.PROMPT_IPV4) + 2

    def speech_balloon(self):
        # Print the top border of the speech balloon
        print(self.border['TopCornerLeft'], self.border['separator'] * self.settings_cowsay['width'], self.border['TopCorneRight'], sep='')
        # Print the prompt string in the speech balloon
        print(self.border['sideleft'], self.PROMPT_IPV4.center(self.settings_cowsay['width']), self.border['sideright'], sep='')
        # Print the middle part of the speech balloon
        for v in range(self.settings_cowsay['height'] - 2):
            print(self.border['sideleft'], ' ' * self.settings_cowsay['width'], self.border['sideright'], sep='')
        # Print the bottom border of the speech balloon
        print(self.border['DownCornerLeft'], self.border['separator'] * self.settings_cowsay['width'], self.border['DownCorneRight'], sep='')
        # Print the cow ASCII art
        print("\\\n".rjust(41, " "), "\\".rjust(40, " "), end="")
        for i in self.cow:
            print(i, end="".rjust(self.settings_cowsay['width'] + 4, ' '))
        return True

# Create an instance of the cowsay class and call the speech_balloon method
cowsayInstance = cowsay()
cowsayInstance.speech_balloon()
