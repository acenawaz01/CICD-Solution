from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# configure below credentials 
JENKINS_URL = "http://localhost:8080/job/generic_build/buildWithParameters"
JENKINS_USER_TOKEN = "1181329ec4cf7d254b73408e7ed8b22d4f"
JENKINS_USER = "shariq"

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

    post_data = { JENKINS_USER : JENKINS_USER_TOKEN }
    response = requests.post(JENKINS_URL, auth=(JENKINS_USER, JENKINS_USER_TOKEN),data = post_data)
    result = response
    return render_template('app.html',result=response)

if __name__ == ' __main__':
    app.run(debug=True,host='0.0.0.0')
