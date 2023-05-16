from socket import * 
class cowsay():

	def __init__(self) -> None:
		
		self.Your_ipv4 = gethostbyname(gethostname())

		self.PROMPT_IPV4 = f'Your ipv4 address is {self.Your_ipv4}'

		self.border = {'TopCornerLeft': "┌", 'separator': '-', 'TopCorneRight':"┐",
							'sideleft': '|',                      'sideright': '|',
					  'DownCornerLeft': "└",                  'DownCorneRight':"┘",}
		self.settings_cowsay = {'height' : 8, 'width': 0, 'wide': 2}
		
		self.cow = ["\n",
		  			"^__^\n",
					"(oo)______\n",
					"(__)      )\\\n",
					"   ||---w|| *"]

		if len(self.PROMPT_IPV4) >= self.settings_cowsay['width']:
			self.settings_cowsay['width'] = len(self.PROMPT_IPV4) + 2 

	def speech_balloon(self):

		print(self.border['TopCornerLeft'],end='')
		for v in range(self.settings_cowsay['width']):
			print(self.border['separator'], end='')
		print(self.border['TopCorneRight'])

		print(self.border['sideleft'].ljust(2," "),end='')
		print(f"{self.PROMPT_IPV4}",end='')
		print(self.border['sideright'].rjust(self.settings_cowsay['wide']))

		for v in range(self.settings_cowsay['height'] -2):
			print(self.border['sideleft'].ljust(2," "),end='')
			print(' '*len(self.PROMPT_IPV4),end='')
			print(self.border['sideright'].rjust(self.settings_cowsay['wide']))


		print(self.border['DownCornerLeft'],end='')
		for v in range(self.settings_cowsay['width']):
			print(self.border['separator'], end='')    
		print(self.border['DownCorneRight'],end='')


		print("\\\n","\\".rjust(40," "),end="")
		for i in cowsayInstance.cow:
			print(i,end="".rjust(self.settings_cowsay['width'] + 4, ' '))

		return True

cowsayInstance = cowsay()
cowsayInstance.speech_balloon()

