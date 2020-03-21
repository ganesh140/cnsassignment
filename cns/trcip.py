from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/enc',methods=['GET','POST'])
def enc():
	if request.method=='POST':
		ptext=request.form['ptext']

		return render_template('cip.html', ptext=ptext)

	return render_template('enc.html')
@app.route('/dec',methods=['GET','POST'])
def dec():
	if request.method=='POST':
		ctext=request.form['ctext']

		return render_template('pl.html', ctext=ctext)
	
	return render_template('dec.html')

if __name__=="__main__":
	app.run()
