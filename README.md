# Got Room

This web app is a place where University students can add their universities and post off campus rooms they would like to 
rent out to other students. 

<br>

This uses Google plus log on to allow signed in users to post rooms to any of the universities or even post a new university that is 
not available on the website already.
<br>


## Main Python Libraries Used in this Project
- Flask
- oauth2clien
- Jinja2
- SQLAlchemy
#Please see the requirements.txt file for the full list


## How to Run

1. First, you need to install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads) on your machine. Here are the tools you will need to install and the instructions:

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

<br>

2. Then, you'll need to clone this repository to your local machine, this will have all the requirements needed to run the application as the
requirements are installed within the virtual machine.

3. Go to the vagrant directory in the cloned repository, then open a terminal window and type `$ vagrant up` to launch your virtual machine. This will take some time in your first run, because it needs to install some dependencies.

4. Once it is up and running, type `$ vagrant ssh` to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. 

5. On your virtual machine, go to <b>/vagrant/Got-Room</b> directory, then type `$ python app.py`. This will launch the application.

6. You can check out the page from your browser at <b>[http://localhost:5000](http://localhost:5000)</b>.

7. If the terminal says that it can't find some modules, then open <b>requirements.txt</b> file in the current directory. You will see an instruction on how to install dependencies.


## To Run the Application with Your own Google Credential ID and Secret :
1. Visit <b>[http://console.developers.google.com]</b>(http://console.developers.google.com)
2. log in with your google username and password
3. Once logged in, Click the <b>Create Project</b> button 
4. Give a name for your project and do not change the project ID provided by Google
5. Click Create and you will be navgiated to the project dashboard
6. Click <b>APIs & auth</b> on the left hand menu and then select <b>Credentials</b>
7. In the <b>OAuth</b> section , click <b>Create new Client ID</b>
8. Make sure <b>Web Application</b> is selected and then click <b>Configure consent screen</b>
9. Prove your email address and a name for the product
10. Save and click <b>Create Client ID</b>
11. Click <b>Edit Settings</b> and add <b>http://localhost:5000</b> to <b>Authorized Javascript Origins</b>, click update
12. Click the <b>Download JSON</b> button and save the downloaded file as <b>client_secrets.json</b>

##Update Your Client ID and Client Secrets
1.Replace the <b>client_secrets.json</b> file within the <b>Got-Room</b> folder with the one you downloaded on step 12 above
2.Open the login.html file within <b>Got-Room/templates</b>
3. replace the  <b>data-clientid</b> on  line 28 with your Client ID from the project you created, save all and run the application.


##API Endpoints Access :
1. http://localhost:5000/university/JSON/
2. http://localhost:5000/university/1/rooms/JSON  (for rooms within any university)
3. http://localhost:5000/university/1/rooms/1/JSON/  (for any room within a university)





[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/)