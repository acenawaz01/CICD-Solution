from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        github_url = request.form['github_url']
        github_credentials = request.form['github_credentials']
        build_tool = request.form['build_tool']
        meta_data_file = request.form['meta_data_file']
        doSonarScan = request.form.getlist('sonar_scan')
        doEC2deploy = request.form.getlist('ec2_deploy')

    result = doSonarScan
    return render_template('app.html',result=result)

if __name__ == ' __main__':
    app.run(debug=True,host='0.0.0.0')
