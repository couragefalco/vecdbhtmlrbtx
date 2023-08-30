import subprocess

def scrape_rbtx_website():
    command = "httrack https://rbtx.com/ -O 'RBTX' '+*.rbtx.com/*' -r3 -v -N0"
    subprocess.call(command, shell=True)

scrape_rbtx_website()
