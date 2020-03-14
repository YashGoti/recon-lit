## About recon-lit

reco-lit is an improvised version of our favourite subdomain enumeration tool #Sublist3r, which delivers various features such as indicating URL redirections, displaying server name (if present) and IP information, basic port scanning having services running on ports [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 1723, 3306, 3389, 5900, 8080, 8443] and also indicating the URL response status code in output.

## Screenshots

![recon-lit](http://thedarkfiles.tk/Content/Yash/recon-lit/ScreenShot.png "recon-lit in action")

## Installation

```
git clone https://github.com/YashGoti/recon-lit.git
cd recon-lit
python3 setup.py install
pip3 install -r requirements.txt
```

## Usage

```
python3 reconlit.py -d <DOMAIN NAME>
```

## Recommended Python Version:

recon-lit currently supports **Python 2** and **Python 3**.

* The recommended version for Python 2 is **2.7.x**
* The recommended version for Python 3 is **3.4.x**

## Dependencies:

recon-lit depends on the `requests`, `dnspython` and `argparse` python modules.

These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python27\python.exe -m pip install -r requirements.txt
```
- Installation on Linux
```
sudo pip install -r requirements.txt
```
## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-d            | --domain      | Domain name to enumerate subdomains of
-b            | --bruteforce  | Enable the subbrute bruteforce module
-v            | --verbose     | Enable the verbose mode and display results in realtime
-t            | --threads     | Number of threads to use for subbrute bruteforce
-e            | --engines     | Specify a comma-separated list of search engines
-o            | --output      | Save the results to text file
-h            | --help        | show the help message and exit

## License

recon-lit is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/YashGoti/recon-lit/blob/master/LICENSE) for more information.

## Credits

* [streetofhacker](https://twitter.com/streetofhacker) - The Alive Sub-domain check module.
* [aboul3la](https://github.com/aboul3la/Sublist3r) - The Base code for sub-domain enumeration.

## Version
**Current version is 1.0**
