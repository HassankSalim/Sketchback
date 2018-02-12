wget --header 'Host: dl.dropboxusercontent.com' --user-agent 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --header 'Accept-Language: en-US,en;q=0.5' --referer 'https://www.dropbox.com/' --header 'Cookie: uc_session=mdHEbCfpzRjYNSpoWsCKHZ1QdP7qLeGgUcNTHgZ5iPThaWHvrkzmW20CMY53aZaC' --header 'Upgrade-Insecure-Requests: 1' 'https://dl.dropboxusercontent.com/content_link/bsnzDeGeTsT72Q9jPdY1b7NG6QCJqJjZvgQSPrNNPw8SLAIaaP9j47jb9ulH52AB/file?_download_id=302164999818814648326433301618876415808728696265849791076695680396&_notify_domain=www.dropbox.com&dl=1' --output-document 'img_align_celeba.zip'

pip install fastai

apt update && apt install -y libsm6 libxext6

pip install parmap

pip install keras

pip install -U -q PyDrive

mkdir celeba_sketch

unzip img_align_celeba.zip

cd ~/Sketchback/PencilSketch/

python sketch.py
