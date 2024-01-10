# 🐬 WoF Pwnagotchi plugin

![GitHub Release](https://img.shields.io/github/v/release/cyberartemio/wof-pwnagotchi-plugin?style=flat-square)
 ![GitHub issues](https://img.shields.io/github/issues/cyberartemio/wof-pwnagotchi-plugin?style=flat-square)
 ![GitHub License](https://img.shields.io/github/license/cyberartemio/wof-pwnagotchi-plugin?style=flat-square)

Simple plugin to show data from Wall Of Flippers on Pwnagotchi's screen. Display total number of Flippers met and the name of the last Flipper that is online. When a new Flipper is met, shows a custom status message with the Flipper's name.

**If Wall of Flippers is not running, it will still display the total number of Flippers met.**

<div align="center">
<img style="max-width: 500px" src=".github/assets/wof-plugin.png" alt="demo" />
</div>


## 🚀 Installation
> [!WARNING]
> Before installing this plugin on your Pwnagotchi, you need to have Wall of Flippers installed. To Install it, follow the installation steps on Wall of Flippers Github [repository](https://github.com/K3YOMI/Wall-of-Flippers#-installing-and-requirements-).

1. Login inside your pwnagotchi using SSH:
```shell
ssh pi@10.0.0.2
``` 
2. Go to `custom_plugins` directory where all custom plugins of your Pwnagotchi are stored:
```shell
cd /path/to/custom_plugins/directory
```
3. Download the plugin file:
```shell
wget https://raw.githubusercontent.com/cyberartemio/wof-pwnagotchi-plugin/main/wof.py
```
4. Edit your configuration file (`/etc/pwnagotchi/config.toml`) and add the following:
```toml
# Enable the plugin
main.plugins.wof.enabled = true
# Display coordinates for text position
main.plugins.wof.position.x = 5
main.plugins.wof.position.y = 84
# File system path where Flipper.json file is located
main.plugins.wof.wof_file = "/root/Wall-of-Flippers/Flipper.json"
```
5. Restart daemon service:
```shell
sudo systemctl restart pwnagotchi
```

Done! Now the plugin is installed and is working.

> [!NOTE]
> If you don't specify any values for `wof.position.x`, `wof.position.y` and `wof.wof_file`, the plugin will use the following default values:
> - `wof.position.x`: `5`
> - `wof.position.y`: `85`
> - `wof.wof_file`: `/root/Wall-of-Flippers/Flipper.json`

## ❤️ Contribution

If you need help or you want to suggest new ideas, you can open an issue [here](https://github.com/cyberartemio/wof-pwnagotchi-plugin/issues/new).

If you want to contribute, you can fork the project and then open a pull request.

## 🥇 Credits

- Wall of Flippers by K3YOMI ([Github](https://github.com/K3YOMI/Wall-of-Flippers))