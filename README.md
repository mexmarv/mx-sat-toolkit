[![dependency - Python](https://img.shields.io/badge/dependency-Python-blue)](https://pypi.org/project/Python)
![GitHub language count](https://img.shields.io/github/languages/count/mexmarv/mx-sat-toolkit)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/mexmarv/mx-sat-toolkit)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![issues - mx-sat-toolkit](https://img.shields.io/github/issues/mexmarv/mx-sat-toolkit)](https://github.com/mexmarv/mx-sat-toolkit/issues)

<h1 align="center">Free Toolkit SAT (México)</h1>
  <p align="left">
    Support for 3 services: Validating CFDIs (use cases for income inference and validation, RFC Homoclave generation with digit verification and CURP Generation.<br/><br/>
    It is also a great tutorial to learn the amazing FastAPI framework, and run it with uvicorn as multithreaded, and wrap an old SOAP Webservice call. As a bonus, you can build a docker image and deploy it. It truly is extremely fast and practically works anywhere. Enjoy!  
    <br />
    <a href="https://github.com/mexmarv/mx-sat-toolkit"><strong>Explore the docs »</strong></a>
  </p>
</div>
<!-- TABLE OF CONTENTS -->
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#load-testing">Load Testing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#enjoy">Enjoy!</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This is a REST API front for undocumented, public SOAP/WebService from the Mexican Government SAT (Secretaría de Administración Tributaria), in order to verify invoices and or W2 (Payroll Receipts) online.
<p align="right">(<a href="#top">back to top</a>)</p>

### Built With
* [Python](https://python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Suds-Py3](https://github.com/cackharot/suds-py3/)
* [pyfiscal](https://github.com/thomgonzalez/pyfiscal)
* [Uvicorn](https://www.uvicorn.org/)
* [Docker](https://docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you can setup your project locally, and how to build it and run it locally in Docker. You may push docker image to AWS, Azure or GCP using containers. To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure you have both brew and python installed. I will be explaining how to run this on a Mac OSx, (I use a Apple M1 MacBook Pro and will show some tricks to build docker and push to azure), but you can do this on any Windows or linux setup.

If you have brew installed, skip this step.
* Brew (The missing package manager for Mac OSx)
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

If you have pyhton3 installed, with anaconda or anything you like, skip this step.
* python3
  ```sh
  brew install python3
  ```
This will install python3 and pip to install python libraries.

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/mexmarv/mx-sat-toolkit.git
   ```
2. Install Python libraries (you can use pip only if you´ve sourced to pip3).
   ```sh
   pip3 install fastapi
   pip3 install suds-py3
   pip3 install pyfiscal
   pip3 uvicorn
   ```
3. You can run uvicorn with reload option so you can modify code as you test things out.
   ```sh
   uvicorn main:app --reload
   ```
4. You will run default on your local machine on port :80
   ```js
   INFO:     Will watch for changes in these directories: ['/Users/marvin/Documents/Code/mx-sat-toolkit']
   INFO:     Uvicorn running on http://127.0.0.1:80 (Press CTRL+C to quit)
   INFO:     Started reloader process [35729] using watchgod
   INFO:     Started server process [35731]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```
5. If you prefer to run it on Docker, make sure you have it installed prior to this. 
   ```sh
   docker build -t mx-sat-toolkit . 
   ```
   Then just make sure (the script that will run initially will run uvicorn on port 80 multithreaded.
   
   <b>For M1 Apple Chip Mac OS users:</b>
   Little trick, I tried for ours building and deploying to Azure (make sure you are logged in and can publish a container), you need to build the docker image with AMD/Intel in mind in order to run.
   ```sh
   docker buildx build --platform=linux/amd64 --load -t mx-sat-toolkit . 
   ```
   ... and now you are good to go and push that amd64 image to the cloud.
   
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Now head to a favorite browser and open http://localhost:80/sat-cfdi as an example. You will get the required paameters in order to return the validation with the SAT.
```JSON
{"detail":[{"loc":["query","rfce"],"msg":"field required","type":"value_error.missing"},{"loc":["query","rfcr"],"msg":"field required","type":"value_error.missing"},{"loc":["query","monto"],"msg":"field required","type":"value_error.missing"},{"loc":["query","folio"],"msg":"field required","type":"value_error.missing"}]}
```
The required parameters are:
- <b>rfce</b> (RFC Emisor or the originating party´s RFC (Registro Federal de Contribuyentes), the one that signed the Invoice or W2)
- <b>rfcr</b> (RFC Receptor or the RFC of the party that was granted the Invoice or W2)
- <b>monto</b> (amount to verify in the document)
- <b>folio</b> (this is the folio unique number of the document)

All these parameters can be consulted on any valid printed invoice or payroll receipt.

Also you can enter this in the whole GET statement:
* Curl:
```sh
curl -X 'GET' \
  'http://localhost:80/sat?rfce=XXX1234567&rfcr=YYY12345678&monto=1000&folio=AXBVVDGGDGD' \
  -H 'accept: application/json'
```

* http:
```sh
http://localhost:80/sat?rfce=XXX1234567&rfcr=YYY12345678&monto=1000&folio=AXBVVDGGDGD
```
All these parameters can be consulted on any valid printed invoice or payroll receipt.

The response (TB Documented), but its pretty intuitive throws something like this:
```JSON
{
  "CodigoEstatus": "N - 601: La expresión impresa proporcionada no es válida.",
  "EsCancelable": null,
  "Estado": "No Encontrado",
  "EstatusCancelacion": null,
  "ValidacionEFOS": null
}
```
If you get a <b>Y</b> then its valid and you make sure Estado is not cancelled, and you have just verified if an Invoice or Payroll Receipt is valid. This allows you to determine validity, your companies submitted invoices, and even determine income deteremination for loans in a fintech/neobank space.

_To view the Swagger, OpenAPI spec to use on Postman or any other cool tool, just browse to http://localhost:80/docs or http://localhost:80/redoc. You can even invoke the API from the /docs endpoint._ 

<p align="right">(<a href="#top">back to top</a>)</p>

## Load Testing
<b>(Simple Metrics) FastAPI/Uvicorn/Python/Container and SAT Homoclave Calculation</b>

Uploaded the docker image to Google Cloud Container and published it under the free tear demo account so I could try to Load Test it and see response times. Please see Below Images, but in summary:

1. 100-125 concurrent sessions over time, with a total of 6,000+ cummulative sessions.
2. It took 7.5 min to do full test scenario.
3. Response time was less than 10ms per API Response and calculation.
4. There were no errors and console in GCP is included which shows throttling at 18.12 sessions/sec, at an average 10% CPU utilization at full load, so theoretically with this container we could do 180 sessions/sec at heavy load.
5. FastAPI + Uvicorn simply rock at these speeds !

<img src="https://github.com/mexmarv/mx-sat-toolkit/blob/main/images/ExecutionPlan.png?raw=true">
<p align="right">Execution Plan in Time</p>

<img src="https://github.com/mexmarv/mx-sat-toolkit/blob/main/images/GCPLoad.png?raw=true">
<p align="right">GCP Load @ 18.12 s/sec</p>

<img src="https://github.com/mexmarv/mx-sat-toolkit/blob/main/images/AVGResponseTime.png?raw=true">
<p align="right">Average Response Time</p>

<img src="https://github.com/mexmarv/mx-sat-toolkit/blob/main/images/NumSessions.png?raw=true">
<p align="right">Number of Sessions</p>

<img src="https://github.com/mexmarv/mx-sat-toolkit/blob/main/images/CumSessions.png?raw=true">
<p align="right">Cummulative Sessions</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Creative Commons Zero 1.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Marvin Nahmias - mexmarv@gmail.com & marvin.nahmias@broxel.com
Project Link: [https://github.com/mexmarv/mx-sat-toolkit](https://github.com/mexmarv/mx-sat-toolkit)

<p align="right">(<a href="#top">back to top</a>)</p>

## Enjoy 

Lets build on Financial Inclusion for all!
#vamoscontodo. 
Marvs.

