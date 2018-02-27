import nltk
archivo = open('archivoprueba.txt', 'r')
archivo2 = open('transcripccion.txt','w')
linea = archivo.readline()
while linea != '':
	z=0
	coma=0
	linea=archivo.readline()
	w = nltk.word_tokenize(linea)
	for i in w:
		if i=='pattern':
			if w[3]=='*' or w[3]=='_':
				archivo2.write('{"tag": "'+w[4] +'",' '\n')
			else:
				archivo2.write('{"tag": "'+w[3] +'",' '\n')
		elif i=='li':
				
				archivo2.write(' "patterns": [')
				
			
	
				while w[1]=='li':
					z=z+1
					if z<3:
						archivo2.write('"')
						for i in w: 
							if i!='li' and i!='/li' and i!='<' and i!='>':
								archivo2.write(i+' ')
						linea=archivo.readline()						
						w = nltk.word_tokenize(linea)
						archivo2.write('" ')
						if z<2:
							archivo2.write(',')
					
					else:
					    #archivo2.write(']'+'\n')
						archivo2.write('],'+'\n')
						archivo2.write(' "responses": [')
						while w[1]=='li':
							if coma==1:
								archivo2.write(',"')
							else:
								archivo2.write('"')
								coma=1
							for i in w: 
								if i!='li' and i!='/li' and i!='<' and i!='>':
									archivo2.write(i+' ')
							linea=archivo.readline()				
							w = nltk.word_tokenize(linea)
							archivo2.write('" ')					
				
				archivo2.write(']'+'\n')
				archivo2.write('},'+'\n')

archivo.close
archivo2.close
