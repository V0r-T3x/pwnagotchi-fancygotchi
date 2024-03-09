# Pwnagotchi with embeded Fancygotchi

# If you only want to install Fancygotchi, use [Fancytools](https://github.com/V0r-T3x/Fancytools).

[Pwnagotchi wiki](https://github.com/V0r-T3x/pwnagotchi-fancygotchi/wiki)
<p align="center">
    <a href="https://github.com/evilsocket/pwnagotchi/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/evilsocket/pwnagotchi.svg?style=flat-square"></a>
    <a href="https://github.com/evilsocket/pwnagotchi/blob/master/LICENSE.md"><img alt="Software License" src="https://img.shields.io/badge/license-GPL3-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/evilsocket/pwnagotchi/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/evilsocket/pwnagotchi"/></a>
    <a href="https://travis-ci.org/evilsocket/pwnagotchi"><img alt="Travis" src="https://img.shields.io/travis/evilsocket/pwnagotchi/master.svg?style=flat-square"></a>
    <a href="https://invite.pwnagotchi.ai/"><img alt="Slack" src="https://invite.pwnagotchi.ai/badge.svg"></a>
    <a href="https://community.pwnagotchi.ai/"><img alt="Forum" src="https://img.shields.io/discourse/posts?server=https%3A%2F%2Fcommunity.pwnagotchi.ai%2F&style=flat-square"></a>
    <a href="https://twitter.com/intent/follow?screen_name=pwnagotchi"><img src="https://img.shields.io/twitter/follow/pwnagotchi?style=social&logo=twitter" alt="follow on Twitter"></a>
</p>

[Pwnagotchi](https://pwnagotchi.ai/) is an [A2C](https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752)-based "AI" leveraging [bettercap](https://www.bettercap.org/) that learns from its surrounding WiFi environment to maximize the crackable WPA key material it captures (either passively, or by performing authentication and association attacks). This material is collected as PCAP files containing any form of handshake supported by [hashcat](https://hashcat.net/hashcat/), including [PMKIDs](https://www.evilsocket.net/2019/02/13/Pwning-WiFi-networks-with-bettercap-and-the-PMKID-client-less-attack/), 
full and half WPA handshakes.

Instead of merely playing [Super Mario or Atari games](https://becominghuman.ai/getting-mario-back-into-the-gym-setting-up-super-mario-bros-in-openais-gym-8e39a96c1e41?gi=c4b66c3d5ced) like most reinforcement learning-based "AI" *(yawn)*, Pwnagotchi tunes [its parameters](https://github.com/evilsocket/pwnagotchi/blob/master/pwnagotchi/defaults.toml) over time to **get better at pwning WiFi things to** in the environments you expose it to. 

More specifically, Pwnagotchi is using an [LSTM with MLP feature extractor](https://stable-baselines.readthedocs.io/en/master/modules/policies.html#stable_baselines.common.policies.MlpLstmPolicy) as its policy network for the [A2C agent](https://stable-baselines.readthedocs.io/en/master/modules/a2c.html). If you're unfamiliar with A2C, here is [a very good introductory explanation](https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752) (in comic form!) of the basic principles behind how Pwnagotchi learns. (You can read more about how Pwnagotchi learns in the [Usage](https://www.pwnagotchi.ai/usage/#training-the-ai) doc.)

**Keep in mind:** Unlike the usual RL simulations, Pwnagotchi learns over time. Time for a Pwnagotchi is measured in epochs; a single epoch can last from a few seconds to minutes, depending on how many access points and client stations are visible. Do not expect your Pwnagotchi to perform amazingly well at the very beginning, as it will be [exploring](https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752) several combinations of [key parameters](https://www.pwnagotchi.ai/usage/#training-the-ai) to determine ideal adjustments for pwning the particular environment you are exposing it to during its beginning epochs ... but ** listen to your Pwnagotchi when it tells you it's boring!** Bring it into novel WiFi environments with you and have it observe new networks and capture new handshakes—and you'll see. :)

Multiple units within close physical proximity can "talk" to each other, advertising their presence to each other by broadcasting custom information elements using a parasite protocol I've built on top of the existing dot11 standard. Over time, two or more units trained together will learn to cooperate upon detecting each other's presence by dividing the available channels among them for optimal pwnage.

## Documentation

https://www.pwnagotchi.org

Pimoroni Display Hat Mini 320x240 with color background image in horizontal  
![preview](https://raw.githubusercontent.com/V0r-T3x/fancygotchi/main/img/pwnagotchi.png)  

Pimoroni Display Hat Mini 320x240 with color animated background in horizontal  
![preview](https://raw.githubusercontent.com/V0r-T3x/fancygotchi/main/img/horizontal.png)  

Pimoroni Display Hat Mini 320x240 with black background in vertical  
![preview](https://raw.githubusercontent.com/V0r-T3x/fancygotchi/main/img/vertical.jpg)  

Waveshare v2 150x122 1bit color with full color web UI  
![preview](https://github.com/V0r-T3x/fancygotchi/blob/main/img/wsv2_pwnachu.jpg)  

This mod can be a bit slow with some features enabled on a raspberry pi zero.
(I'll add a note about the best light config to your with a rpi0w soon)  

### To install a theme:  
----
- Download the [Fancygotchi Theme](https://github.com/V0r-T3x/fancygotchi_themes) you want. Create the theme folder inside the custom plugins folder and place your theme folder inside it. (default themes folder path: `/usr/local/share/pwnagotchi/custom-plugins/themes/`)

### To create a theme (* Update to come*):  
----  
You can create your own theme easily with fancygothci. You just have to copy the right resolution folders from the theme folder inside the fancygotchi theme folder.  

The folder three is always the same for each theme. Like the cyber theme folder.   

You have the img folder for all images used inside the theme. A css file to modify the webui. And a folder with the resolution of the display. The cyber use the 320x240.  

![image](https://github.com/V0r-T3x/pwnagotchi-fancygotchi/assets/70115207/e33e0937-f00c-4aac-81f2-642795885d88)  

Here a list of display resoltion types:  

![resolution type](https://github.com/V0r-T3x/pwnagotchi-fancygotchi/assets/70115207/a1197aa9-7a63-4e54-9a0e-68c849dc25f1)  

Inside the resolution folder, you will have two file config-h.toml and config-v.toml.  

They stand for the Horizontal and Vertical configuration files. Inside it you have all the possible options. Each position, color, if it can icon or not.. etc etc etc  

1- Copy the default folder.  
2- Rename it with the name of your choice, ex. yourtheme:  
`.../custom_plugins/themes/yourtheme`  
3- Inside this folder, you need a folder named with your display type (look into the config.toml file at `ui.display.type`). If the folder don't exist, just copy another one and rename it with the display type:   
`.../custom_plugins/themes/yourtheme/resolution/config-h.tom`  
4- Change your /etc/pwngotchi/config.toml file with your custom name:   
```
fancygotchi.theme = 'yourtheme'
fancygotchi.rotation = 0 #<--- 0 or 180 for horizontal and 90 or 270 vertical
```  
5- You can now modify this config-h.toml file to create your own interface.  
6- After saving the config file, no need to restart the pwnagotchi, just goto the fancygotchi web plugin page, and refresh it, this will activate the OTG feature, and the UI should be refresh.  

### Configuration files:
----
The configuration file header is composed with all the gobal options for the theme.  

Global options:  
----  

This start with `[theme.options]`.  

`stealth_mode = false`:  
It's not implemented yet, but will give a way to hide the pwnagotchi UI with a foreground image and potentially custom naive components.  

`fg_image`:
Foreground image name.  

`bg_color`:  
Background color.  

`bg_image`:  
Background image name.  

`bg_anim_image`:  
Animated background gif name.  

`font_sizes`:  
Font sizes in this order  
[Bold, BoldSmall, Medium, Huge, BoldBig, Small]  

`font = 'DejaVuSansMono'`
Font name.  

`status_font`:  
Status font name (not work properly for now).  

`label_spacing`:  
General label space.  

`size_offset`:   
Status font offset.  

`fps`:  
Refresh rate of the UI.  

`cursor`:  
Name cursor.  

`friend_bars`:  
Friend bar icons.  

`friend_no_bars`:  
Friend bar at 0.  

`color_web` &  `color_display`:  
The color mode for the web UI or the Display.  
They are independant, the web UI (and share to twitter, telegram, discord, etc) can be in full color, but the pwnagotchi can use a e-ink waveshare into 1bit color mode.  
'2' = 1bit color mode B&W  
'' = full color mode  

`anim_web` & `anim_display`:  
If an animated background is set it can be use as a fixed image too  
true = animated  
false = fixed on the first frame  

`main_text_color`:  
If the full color or animated full color is enabled  
the main color will have priority on all text color  
*this option help to avoid too much lag on a raspberry pi zero w*  

`color_text`:  
What will be the text color for a low color display, possible options:  
'black'  
'white'  
'auto' = pale color will be 'white' and dark color will be 'black'  

Main theme options:  
----  

This part is for all the options native options of the pwnagotchi.  
This start with `[theme.main_elements]`.  

Each __Text__ components options can have those options:  

`position`:  
Position [x,y].  

`font`:  
Font type.  

`color`:  
The component color.  

`colors`:  
The component color table for an color animation [colorname1, colorname2, ...].  

`icon`:  
If enabled (true), the component value is treated as an image name to add to the image folder parth to use an image instead of a text.  

`f_awesome`:  
If enabled (true) and the icon feature is enabled, the component value is use to select the right font awesome character to use instead of a text.  

`f_awesome_size`:  
The font size for Font Awesome.  

Each __Label__ components options can have those options:  

`position`:  
Position [x,y].  

`label`:  
The label value.  

`label_font`:   
The label font.  

`text_font`:  
The text font.  

`label_spacing`:  
Custom label spacing for the component.  

`label_line_spacing`:  
Custom label vertical position compared to the label text.  

`color`:  
The component color.  

`colors`:  
The component color table for an color animation [colorname1, colorname2, ...].  

`icon`:  
If enabled (true), the component value is treated as an image name to add to the image folder parth to use an image instead of a text.  

`f_awesome`:  
If enabled (true) and the icon feature is enabled, the component value is use to select the right font awesome character to use instead of a text.  

`f_awesome_size`:  
The font size for Font Awesome.  

`zoom`:  
The multiplier to adjust the image size.  
Number < 0 = smaller image (0.5 = half size)  
Number > 0 = bigger image (2 = double size)  

Plugins options:  
----  
The third section is for all other custom plugins configuration. This start with `[theme.plugin_elements]`.  

### To custom other plugin appearance:  
----  
For exemple with the bluetooth components, you can check inside the plugin file for the "add_element" variable:  

https://github.com/evilsocket/pwnagotchi/blob/master/pwnagotchi/plugins/default/bt-tether.py#L586  

```
ui.add_element('bluetooth', LabeledValue(color=BLACK, label='BT', value='-', position=(ui.width() / 2 - 15, 0),
                           label_font=fonts.Bold, text_font=fonts.Medium))
```

If you check into the config-h.toml you can check how the bluetooth part is constituted.  

All other custom plugins are stocked under [theme.plugin_elements].  

```
[theme.plugin_elements]

[theme.plugin_elements.bluetooth]
position = [276, 170]
label = 'BT'
value = '-'
label_font = 'Bold'
text_font = 'Medium'
label_spacing = 9
label_line_spacing = 0
color = 'lime'
colors = ['yellow','orange','red','purple','blue']
icon = false
f_awesome = false
f_awesome_size = 40
```
### To change the pwnagotchi face with image:  
----  

If you want you can change the pwny face too. Enable the icon feature, and places all the images faces with the right names in /themes/mytheme/img/. You can change the image type to use (I only tested it with png). The pure white on images will become transparent. Each image need to have the same size.  

```
[theme.main_elements.face]
position = [14, 28]
font = "Huge"
color = "lime"
colors = ['yellow','orange','red','purple','blue']
icon = true # Enable here
image_type = "png"
```

images name in /themes/mytheme/img/:  

```
look_r.png
look_l.png
look_r_happy.png
look_l_happy.png
sleep.png
sleep2.png
awake.png
bored.png
intense.png
cool.png
happy.png
excited.png
grateful.png
motivated.png
demotivated.png
smart.png
lonely.png
sad.png
angry.png
friend.png
broken.png
debug.png
upload.png
upload1.png
upload2.png
```

### On-The-Go refresh:  
----  
If something in the configration changed, no need to restart the pwnagotchi. You can go into Fancygotchi plugin page to refresh it. All the UI will be actualized.  

### Sharing custom theme:  
----  
If you create a custom theme and you want to share it. Just need to share the folder theme to another device with Fancygotchi installed.  

You can fork this repo, copy your new theme and push a commit to the main. I'll add them to the main repo.  

## Links

&nbsp; | Official Links
---------|-------
Website | [pwnagotchi.ai](https://pwnagotchi.ai/)
Discord | [Unofficial pwnagotchi](https://discord.gg/PgaU3Vp)
Discord | [Bananagotchi](https://discord.gg/tJusHNkPVs)
Subreddit | [r/pwnagotchi](https://www.reddit.com/r/pwnagotchi/)
Subreddit | [r/bananagotchi](https://www.reddit.com/r/bananagotchigotchi/)
Twitter | [@V0rT3x](https://twitter.com/V0rt3_x)  
Twitter | [@pwnagotchi](https://twitter.com/pwnagotchi)

## License

`pwnagotchi` is made with ♥  by [@evilsocket](https://twitter.com/evilsocket) and the [amazing dev team](https://github.com/evilsocket/pwnagotchi/graphs/contributors). It is released under the GPL3 license.
`fancygotchi` is made with ♥  by [@V0rT3x](https://twitter.com/V0rt3_x). It is released under the GPL3 license.
