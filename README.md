# Audio Mixer
Dowmload and mix the background track of one song and the vocals of another in less than a minute!

## Installing dependencies 
### Tkinter

* <details>
  <summary>Windows/Macos</summary>
  Open command prompt/terminal and type: pip install tk
</details>

* <details>
  <summary>Ubuntu</summary>
  sudo apt install python-tk
</details>

* <details>
  <summary>Fedora</summary>
  sudo dnf install python3-tkinter
</details>

* <details>
  <summary>Arch</summary>
  sudo pacman -S tk
</details>

### Other pip Packages 
* Run the following command in your terminal to install all the other pip packages
```
pip install pydub pytube youtube_search
```

## Installation and first run
Run the following commands in a terminal to install and run the script:
```
git clone https://github.com/Haardispro/Epoch-Hackathon-Project.git
cd Epoch-Hackathon-Project/
python audiomixer.py
```
## Usage instructions
1. In the first box, input the name of the song whose backgroud track you want to mix and add `background track` prefix in the end. i.e. "tunak tunak tun background track" as illustrated below
![image](https://user-images.githubusercontent.com/93829532/211005989-858be3e3-81ab-45dd-aa9a-783f29d03379.png)
2. In the second box, input the name of the song whose vocals you want to mix and add 'vocals' prefix in the end. i.e. "rap god vocals" as illustrated below
![image](https://user-images.githubusercontent.com/93829532/211006239-673d4ed2-ea83-42cc-858b-b0cf46ae1199.png)
3. Click on 'Download Backgroud track' and 'Download Vocal track'
4. Click on 'Start'
5. Click on 'Play overlayed song'
