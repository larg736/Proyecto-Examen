from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:8000', allow_none=True)

nome = ''
while(nome != 'exit'):
	print('Networking Products')
	nome = input('\n- Product to search -> ')

	Available = s.products(nome.lower())

	if Available == '1':
		print('\nWe currently do not have this product.!')
	elif Available == '0':
		print('\nExiting the Application...\n')
	else:
		print('\nAvailability in ' + nome.upper())
		print('\n|' + Available + '|\n')