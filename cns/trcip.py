import math
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/enc',methods=['GET','POST'])
def enc():
	if request.method=='POST':
		ptext=request.form['ptext']
		pkey=request.form['pkey']
		def encryptMessage(ptext): 
		    cipher = "" 
		  
		    # track key indices 
		    k_indx = 0
		  
		    msg_len = float(len(ptext)) 
		    msg_lst = list(ptext) 
		    key_lst = sorted(list(pkey)) 
		  
		    # calculate column of the matrix 
		    col = len(pkey) 
		      
		    # calculate maximum row of the matrix 
		    row = int(math.ceil(msg_len / col)) 
		  
		    # add the padding character '_' in empty 
		    # the empty cell of the matix  
		    fill_null = int((row * col) - msg_len) 
		    msg_lst.extend('_' * fill_null) 
		  
		    # create Matrix and insert message and  
		    # padding characters row-wise  
		    matrix = [msg_lst[i: i + col]  
		              for i in range(0, len(msg_lst), col)] 
		  
		    # read matrix column-wise using key 
		    for _ in range(col): 
		        curr_idx = pkey.index(key_lst[k_indx]) 
		        cipher += ''.join([row[curr_idx]  
		                          for row in matrix]) 
		        k_indx += 1
		  
		    return cipher
		cipher=encryptMessage(ptext)
		
		return render_template('cip.html', cipher=cipher)

	return render_template('enc.html')
@app.route('/dec',methods=['GET','POST'])
def dec():
	if request.method=='POST':
		ctext=request.form['ctext']
		ckey=request.form['ckey']
		def decryptMessage(ctext): 
		    msg = "" 
		  
		    # track key indices 
		    k_indx = 0
		  
		    # track msg indices 
		    msg_indx = 0
		    msg_len = float(len(ctext)) 
		    msg_lst = list(ctext) 
		  
		    # calculate column of the matrix 
		    col = len(ckey) 
		      
		    # calculate maximum row of the matrix 
		    row = int(math.ceil(msg_len / col)) 
		  
		    # convert key into list and sort  
		    # alphabetically so we can access  
		    # each character by its alphabetical position. 
		    key_lst = sorted(list(ckey)) 
		  
		    # create an empty matrix to  
		    # store deciphered message 
		    dec_cipher = [] 
		    for _ in range(row): 
		        dec_cipher += [[None] * col] 
		  
		    # Arrange the matrix column wise according  
		    # to permutation order by adding into new matrix 
		    for _ in range(col): 
		        curr_idx = ckey.index(key_lst[k_indx]) 
		  
		        for j in range(row): 
		            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
		            msg_indx += 1
		        k_indx += 1
		  
		    # convert decrypted msg matrix into a string 
		    try: 
		        msg = ''.join(sum(dec_cipher, [])) 
		    except TypeError: 
		        raise TypeError("This program cannot", 
		                        "handle repeating words.") 
		  
		    null_count = msg.count('_') 
		  
		    if null_count > 0: 
		        return msg[: -null_count] 
		  
		    return msg 
		plain=decryptMessage(ctext)
		return render_template('pl.html', plain=plain)
	
	return render_template('dec.html')

if __name__=="__main__":
	app.run()
