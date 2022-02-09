enigmabox-openwrt-private
=========================

OpenWrt package feed for the Enigmabox software suite.

How to build that stuff:

    $ git clone https://github.com/openwrt/openwrt.git
    $ cd openwrt
    
    $ git checkout v19.07

    $ vi feeds.conf

Your feeds.conf should look like this:

    src-git packages https://git.openwrt.org/feed/packages.git;openwrt-19.07
    src-git luci https://git.openwrt.org/project/luci.git;openwrt-19.07
    src-git routing https://git.openwrt.org/feed/routing.git;openwrt-19.07
    src-git telephony https://git.openwrt.org/feed/telephony.git;openwrt-19.07
    
    src-git enigmabox https://github.com/CyberMind-FR/enigmabox-openwrt-private.git;openwrt-19.07
    

Next use that package system to incorporate the Enigmabox software suite:

    $ ./scripts/feeds update -a
    $ ./scripts/feeds install -a

Then configure for your system:

    $ make menuconfig

## Private rework refresh based on OpenWrt v19.07.7

    Use it at your own risk...
    Still in development phase...
    
    CONFIDENTIAL and PRIVATE!
    For your eyes only!    

## Building firmware for the EspressoBin Board

    20210605: fully working on cortexa53
    tested on MVEBU ARMADA 37xx ESPRESSOBIN BOARD from GST

    //FIXME-TODO: define the settings (as defaults devices)...


"Target System": **Marvell EBU Armada**

"Subtarget": **Marvell Armada 3700LP (ARM64)**

"Target Profile": **ESPRESSObin V7 eMMC (Marvell Armada 3700 Community Board**

"Target Images": configure as you please. Example:
* Root filesystem images:
  * ext4: yes
    * Root filesystem block size: 4k
    * Create a journaling filesystem: yes
  * GZip images: no
* Image Options:
  * Kernel partition size (in MB): 16
  * Root filesystem partition size (in MB): 3600

"Libraries":
  * libffmpeg-audio-dec

"Enigmabox":
* cfengine-promises: yes
  * Network profile: **EspressoBin**
* provision-grandstream: yes
* roundcube: yes
* teletext: yes
* webinterface: yes

The "webinterface" is the most important part, since it's selecting all required dependencies.

Quit and save your .config

Then:

    $ make

After about 30mins (depending on your machine), your image is ready:

    bin/targets/mvebu/cortexa53/openwrt-19.07.7-mvebu-cortexa53-globalscale_espressobin-v7-emmc-ext4-sdcard.img.gz

Flash it on the EspressoBin emmc (or sdcard) as usual!

## Building firmware for the Banana Pi

"Target System": **Allwinner A1x/A20/A3x**

"Target Profile": **Bananapi**

"Target Images": configure as you please. Example:
* Root filesystem images:
  * ext4: yes
    * Maximum number of inodes in root filesystem: 200000
    * Create a journaling filesystem: yes
  * GZip images: no
* Image Options:
  * Root filesystem partition size (in MB): 3600
  * Include kernel in root filesystem: yes
  * Include DTB in root filesystem: yes

Recently, OpenWrt decided to ~~fuck everything up~~ switch to musl by default.

Stick to uClibc manually:

"Advanced configuration options":
  * Toolchain Options
    * C Library implementation
      * Use uClibc

"Libraries":
  * libffmpeg-audio-dec

"Enigmabox":
* cfengine-promises: yes
  * Network profile: **Rasperry Pi**
* provision-grandstream: yes
* roundcube: yes
* teletext: yes
* webinterface: yes

The "webinterface" is the most important part, since it's selecting all required dependencies.

Quit and save your .config

Then:

    $ make

After about 30mins (depending on your machine), your image is ready:

    bin/sunxi/openwrt-sunxi-Bananapi-sdcard-vfat-ext4.img

## Building firmware for the PC-Engines APU

"Target System": **x86**

"Target Profile": **x86_64**

"Target Images": configure as you please. Example:
* Root filesystem images:
  * ext4: yes
    * Maximum number of inodes in root filesystem: 200000
    * Create a journaling filesystem: yes
  * GZip images: no
* Image Options:
  * Root filesystem partition size (in MB): 3600
  * Include kernel in root filesystem: yes

Recently, OpenWrt decided to ~~fuck everything up~~ switch to musl by default.

Stick to uClibc manually:

"Advanced configuration options":
  * Toolchain Options
    * C Library implementation
      * Use uClibc

"Libraries":
  * libffmpeg-audio-dec

"Enigmabox":
* cfengine-promises: yes
  * Network profile: **APU**
* provision-grandstream: yes
* roundcube: yes
* teletext: yes
* webinterface: yes

The "webinterface" is the most important part, since it's selecting all required dependencies.

Quit and save your .config

Then:

    $ make

After about 30mins (depending on your machine), your image is ready:

    bin/x86-uClibc/openwrt-x86-64-combined-ext4.img

## Building firmware for the PC-Engines Alix

"Target System": **x86**

"Target Profile": **Generic**

"Target Images": configure as you please. Example:
* Root filesystem images:
  * ext4: yes
    * Maximum number of inodes in root filesystem: 200000
    * Create a journaling filesystem: yes
  * GZip images: no
* Image Options:
  * Root filesystem partition size (in MB): 3600
  * Include kernel in root filesystem: yes

Recently, OpenWrt decided to ~~fuck everything up~~ switch to musl by default.

Stick to uClibc manually:

"Advanced configuration options":
  * Toolchain Options
    * C Library implementation
      * Use uClibc

"Libraries":
  * libffmpeg-audio-dec

"Enigmabox":
* cfengine-promises: yes
  * Network profile: **ALIX**
* provision-grandstream: yes
* roundcube: yes
* teletext: yes
* webinterface: yes

The "webinterface" is the most important part, since it's selecting all required dependencies.

Quit and save your .config

Then:

    $ make

After about 30mins (depending on your machine), your image is ready:

    bin/x86-uClibc/openwrt-x86-generic-combined-ext4.img

