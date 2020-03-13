import pip
uninstall = {}
flag=0

def install(package):
    try:
        pipcode = pip.main(['install', package])
        if pipcode != 0:
            flag=1
            uninstall[package] = "Unable to install " + package
    except:
        uninstall[package] = "Unable to install " + package


temp = {
    "Dependencies": ["beautifulsoup4==4.4.1", "boto==2.48.0", "bz2file==0.98", "certifi==2017.7.27.1", "chardet==3.0.4",
                     "html5lib==0.999", "idna==2.5", "nltk==3.2.4", "pexpect==4.0.1",
                     "pip==9.0.1", "ptyprocess==0.5", "pyxdg==0.25", "requests==2.18.3",
                     "setuptools==20.7.0", "six==1.10.0", "smart-open==1.5.3", "textblob==0.12.0",
                     "twitter==1.17.1", "urllib3==1.22"]}
for package in temp['Dependencies']:
    install(package)

if flag:
    for name, value in uninstall.items():
         print(name, value)
else:
         print("Sucessfully installed all packages")
         print("You are good to go..")
         
