<h3 align="center">SAT Verifica (México) - Facturas y Recibos de Nómina</h3>
  <p align="center">
    Verify mexican invoices and payroll receipts with government SAT entity.
    <br />
    <a href="https://github.com/mexmarv/mx-sat-verifica"><strong>Explore the docs »</strong></a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/mexmarv/mx-sat-verifica.git
   ```
2. Install Python libraries (you can use pip only if you´ve sourced to pip3).
   ```sh
   pip3 install fastapi
   pip3 install suds-py3
   pip3 uvicorn
   ```
3. You can run uvicorn with reload option so you can modify code as you test things out.
   ```sh
   uvicorn main:app --reload
   ```
4. You will run default on your local machine on port :8000
   ```js
   INFO:     Will watch for changes in these directories: ['/Users/marvin/Documents/Code/mx-sat-verifica']
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [35729] using watchgod
   INFO:     Started server process [35731]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Now head to a favorite browser and open http://localhost:8000/sat. You will get the required paameters in order to return the validation with the SAT.
```JSON
{"detail":[{"loc":["query","rfce"],"msg":"field required","type":"value_error.missing"},{"loc":["query","rfcr"],"msg":"field required","type":"value_error.missing"},{"loc":["query","monto"],"msg":"field required","type":"value_error.missing"},{"loc":["query","folio"],"msg":"field required","type":"value_error.missing"}]}
```
The required parameters are:
- rfce (RFC Emisor or the originating party´s RFC (Registro Federal de Contribuyentes), the one that signed the Invoice or W2)
- rfcr (RFC Receptor or the RFC of the party that was granted the Invoice or W2)
- monto (amount to verify in the document)
- folio (this is the folio unique number of the document)

All these parameters can be consulted on any valid printed invoice or payroll receipt.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
