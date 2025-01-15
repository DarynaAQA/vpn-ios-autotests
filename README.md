# VPN iOS Test

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About project 

![logo](https://www.facebook.com/photo/?fbid=122139127040174832&set=p.122139127040174832)

This project was created to ensure the highest the product quality and speed up the testing process.
This README file will help you prepare everything you need to run the tests on your computer.
Please see the information below to get started 👇

> <p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
This section lists all the core frameworks/libraries used to bootstrap this project. 

- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"/>
- <img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=node.js&logoColor=white"/>
- <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white"/>
- <img src="https://img.shields.io/badge/Appium-EE376D?style=for-the-badge&logo=appium&logoColor=white"/>
- <img src="https://img.shields.io/badge/XCUITest-83B81A?style=for-the-badge"/>
- <img src="https://img.shields.io/badge/XCode-147EFB?style=for-the-badge&logo=xcode&logoColor=white"/>

> <p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
To prepare the test environment, perform the following steps👇:
### Prerequisites

1. Install last version Python on your computer - 🧐 [documentation](https://www.python.org/downloads/)

2. Install Node.js and npm
- Go to the site https://nodejs.org/en/ and click on the button `Download Node.js (LTS)`.
- Perform installation of the downloaded package.
- Check if the installation was successful, open your terminal and check version:
```sh
  node -v
  ```
```sh
  npm -v
  ```

3. Install Appium server - 🧐 [documentation](https://appium.io/docs/en/2.11/quickstart/install/)
- install Appium server
```sh
  npm install -g appium
  ```
- check current version 
```sh
  appium -v
  ```
4. Install XCUITest driver - 🧐 [documentation](https://appium.github.io/appium-xcuitest-driver/7.24/installation/)

- install XCUITest 
```sh
  appium driver install xcuitest
  ```
- сheck for driver XCUITest driver in Appium drivers list
```sh
  appium driver list
  ```
5. Install Appium Doctor - is a utility that helps diagnose problems with the configuration of the Appium environment. It checks whether all necessary dependencies are installed and whether systems are correctly configured to work with Appium. 
- install Appium Doctor 
```sh
  npm install @appium/doctor -g
  ```
- execute next command for diagnose
```sh
  appium-doctor --ios
  ```

6. Setting up WebDriverAgent - 🧐 [documentation](https://appium.github.io/appium-xcuitest-driver/4.24/wda-custom-server/).
Follow this step by step to prepare your simulator for use with Appium:
- Open WebDriverAgent.xcodeproj in Xcode:
```sh
  cd ~
  cd .appium/
  cd node_modules/
  cd appium-xcuitest-driver/
  cd node_modules/
  cd appium-webdriveragent/
  open .
  open WebDriverAgent.xcodeproj in Xcode 
  ```
- Select your real phone/Simulator you'd like to run automated tests on as build target
- Select IntegrationApp and click on the Build button - https://prnt.sc/Vr9JasqU3fo6. Check on successful installation of IntegrationApp.
- Select WebDriverAgentRunner and click the Test button - https://prnt.sc/D7sXJJ3mE-US
- Build the iOS app one time before running tests

### Installation
- clone the repository from the main branch 
```sh
  git clone {repo link}
  ```
- go to the project root folder 
```sh
  cd /vpn-ios-autotests
  ```
- create virtual environment by command
```sh
  python3 -m venv venv
  ```
- activate virtual environment
```sh
  source venv/bin/activate
  ```
- install requirements
```sh
  pip install -r requirements.txt
  ```
- open conftest.py and indicate current value for variable APP_PATH. To determine the actual path, you need to open the desired Xcode project, go to Show the project navigator, find the app in the Products folder and click on it. On the right side you will see full path the app - https://prnt.sc/kw6_sELIOhM4

- open your terminal and execute next command for run Appium server 
```sh
  appium --allow-cors --port 4723
  ```
- to run tests execute command on the root directory
```sh
  pytest
  ```

> <p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
If you still have some questions, please ask them in my Slack profile - [Darina Bannik]() 🙌