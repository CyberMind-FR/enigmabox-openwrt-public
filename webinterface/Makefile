include $(TOPDIR)/rules.mk

PKG_NAME:=webinterface
PKG_VERSION:=2.15.0
PKG_RELEASE:=8

include $(INCLUDE_DIR)/package.mk

define Package/webinterface
  SECTION:=administration
  CATEGORY:=Enigmabox
  TITLE:=Enigmabox web interface
  URL:=http://enigmabox.net/en/
##  DEPENDS:=+cjdns
  DEPENDS+= +cjdns-master +cjdns-contrib
#  DEPENDS+= +cjdns-v6 +cjdns-v16
  DEPENDS+= +curl +syslog-ng +zip +unzip +shadow-usermod +kmod-ipt-nat6 +isc-dhcp-server-ipv4 +radvd +openssh-sftp-server +vnstat +rsync +fdisk +@DROPBEAR_ECC +@BUSYBOX_CUSTOM +@BUSYBOX_CONFIG_DIFF
  DEPENDS+= +python-gevent
# south obsolete since django 1.7
#  DEPENDS+= +python-django-south +python-django +python-gunicorn +python-six
  DEPENDS+= +python-django-south +python-django-1.4 +python-gunicorn +python-six
  DEPENDS+= +python +python-requests +python-simplejson +python-yaml +python-unidecode +python-beanstalkc +python-pillow
  DEPENDS+= +asterisk16 +asterisk16-sounds +asterisk16-codec-gsm +asterisk16-format-gsm +asterisk16-format-wav +asterisk16-res-srtp +asterisk16-res-musiconhold +asterisk16-app-confbridge +asterisk16-app-read +asterisk16-res-timing-pthread +asterisk16-voicemail +asterisk16-format-h264 +asterisk16-app-system +asterisk16-chan-sip +asterisk16-res-rtp-asterisk +asterisk16-codec-ulaw +svox +libffmpeg-audio-dec +sox
  DEPENDS+= +php7 +php7-cgi +php7-cli +php7-pecl-mcrypt +php7-mod-pdo-sqlite +php7-mod-pdo-mysql +php7-mod-mysqli +php7-mod-session +php7-mod-iconv +php7-mod-json +php7-mod-ctype +php7-mod-dom +php7-mod-gd +php7-mod-hash +php7-mod-mbstring +php7-mod-simplexml +php7-mod-xml +php7-mod-xmlreader +php7-mod-xmlwriter +php7-mod-zip +php7-mod-curl +php7-mod-sqlite3 +php7-mod-fileinfo +php7-mod-exif +php7-mod-ftp +@php7_FILTER +@php7_LIBXML +@BUILD_NLS
  DEPENDS+= +php7-mod-openssl +php7-mod-intl
  DEPENDS+= +mariadb-server +mariadb-common +mariadb-server-base +libmariadb +libdbd-mysql +libdbi
  DEPENDS+= +lighttpd +lighttpd-mod-auth +lighttpd-mod-access +lighttpd-mod-cgi +lighttpd-mod-fastcgi +lighttpd-mod-proxy +lighttpd-mod-rewrite +lighttpd-mod-setenv +lighttpd-mod-alias +lighttpd-mod-authn_file
  DEPENDS+= +privoxy
  DEPENDS+= +dovecot +exim4
  DEPENDS+= +cfengine +cfengine-promises
  DEPENDS+= +beanstalkd
  DEPENDS+= +socat
  DEPENDS+= +cryptsetup +losetup +kmod-loop +kmod-crypto-xts +kmod-crypto-cbc +kmod-crypto-misc +kmod-crypto-iv +e2fsprogs
  DEPENDS+= +zoneinfo-africa +zoneinfo-asia +zoneinfo-atlantic +zoneinfo-australia-nz +zoneinfo-europe +zoneinfo-india +zoneinfo-northamerica +zoneinfo-pacific +zoneinfo-poles +zoneinfo-simple +zoneinfo-southamerica
  DEPENDS+= +kmod-usb-net +kmod-usb-net-asix +kmod-usb-net-asix-ax88179 +kmod-usb-net-cdc-eem +kmod-usb-net-cdc-ether +kmod-usb-net-cdc-mbim +kmod-usb-net-cdc-ncm +kmod-usb-net-cdc-subset +kmod-usb-net-dm9601-ether +kmod-usb-net-hso +kmod-usb-net-huawei-cdc-ncm +kmod-usb-net-ipheth +kmod-usb-net-kalmia +kmod-usb-net-kaweth +kmod-usb-net-mcs7830 +kmod-usb-net-pegasus +kmod-usb-net-qmi-wwan +kmod-usb-net-rndis +kmod-usb-net-sierrawireless +kmod-usb-net-smsc95xx
  DEPENDS+= +wireless-tools +wpa-supplicant +kmod-ath +kmod-ath9k-htc +kmod-brcmfmac +kmod-carl9170 +kmod-libertas-usb +kmod-p54-usb +kmod-rt2500-usb +kmod-rt2800-usb +kmod-rt73-usb +kmod-rtl8187 +kmod-rtl8192cu +kmod-zd1211rw 
# Disabled, FIXME
##  DEPENDS+= +kmod-net-rtl8188eu

# APU
#  DEPENDS+= +kmod-e1000 +kmod-r8169 +kmod-via-rhine

# APU2
#  DEPENDS+= +kmod-i2c-core +kmod-igb +cjdns-v16-avx

  DEPENDS+= +kmod-fs-btrfs +kmod-fs-cifs +kmod-fs-cramfs +kmod-fs-ext4 +kmod-fs-hfs +kmod-fs-hfsplus +kmod-fs-isofs +kmod-fs-jfs +kmod-fs-msdos +kmod-fs-nfs +kmod-fs-ntfs +kmod-fs-reiserfs +kmod-fs-udf +kmod-fs-vfat +kmod-fs-xfs +kmod-fuse
  DEPENDS+= +kmod-nls-cp1250 +kmod-nls-cp1251 +kmod-nls-cp437 +kmod-nls-cp775 +kmod-nls-cp850 +kmod-nls-cp852 +kmod-nls-cp862 +kmod-nls-cp864 +kmod-nls-cp866 +kmod-nls-cp932 +kmod-nls-iso8859-1 +kmod-nls-iso8859-13 +kmod-nls-iso8859-15 +kmod-nls-iso8859-2 +kmod-nls-iso8859-6 +kmod-nls-iso8859-8 +kmod-nls-koi8r +kmod-nls-utf8
##  DEPENDS+= +hypesites +dokuwiki +owncloud +owncloud-documents +stikked
  DEPENDS+= +hypesites +dokuwiki +owncloud +stikked
##  DEPENDS+= +@LIBC_USE_UCLIBC #doesn't work, set it manually!
endef

ifneq ($(CONFIG_USE_UCLIBC),)
PKG_DO_VARS+= UCLIBC=1
endif

define Package/webinterface/description
 The Enigmabox administration web interface, used for configuring
 the settings of the Enigmabox. It does not depend on any OpenWrt
 interface, in fact, it replaces LuCI.

 It also serves as a metapackage. Select it, and everything else
 required for the Enigmabox will be selected.
endef

#PKG_BUILD_DEPENDS:=python-setuptools
#PYTHONPATH:=$(PYTHONPATH):$(PKG_BUILD_DIR)/thirdpart

#define Download/django
#   FILE=Django-1.6.tar.gz
#   URL=https://www.djangoproject.com/m/releases/1.6/
##   MD5SUM:=675fc736e2c29090f005e217ccf90b5b
#   MD5SUM:=675fc736e2c29090f005e217ccf90b5b
#endef

#define Download/gunicorn
#   FILE=gunicorn-0.16.1.tar.gz
#   URL=https://pypi.python.org/packages/source/g/gunicorn/
#   MD5SUM:=d53d5d04d941f2a3089e814e753a218f
#endef

#define Download/six
#   FILE=six-1.4.1.tar.gz
#   URL=https://pypi.python.org/packages/source/s/six/
#   MD5SUM:=bdbb9e12d3336c198695aa4cf3a61d62
#endef

define Build/Configure
endef

#define Build/Compile
#	# Download python dependencies
#	$(eval $(call Download,django))
#	$(eval $(call Download,gunicorn))
#	$(eval $(call Download,six))
#	# Install python dependencies
#	$(call HostPython,, \
#		$(STAGING_DIR_ROOT)/usr/bin/easy_install -d $(PKG_INSTALL_DIR) -Z -N \
#		$(DL_DIR)/Django-1.5.8.tar.gz)
#	$(call HostPython,, \
#		$(STAGING_DIR_ROOT)/usr/bin/easy_install -d $(PKG_INSTALL_DIR) -Z -N \
#		$(DL_DIR)/gunicorn-0.16.1.tar.gz)
#	$(call HostPython,, \
#		$(STAGING_DIR_ROOT)/usr/bin/easy_install -d $(PKG_INSTALL_DIR) -Z -N \
#		$(DL_DIR)/six-1.4.1.tar.gz)
#endef

define Build/Compile
endef

define Package/webinterface/install
	$(INSTALL_DIR) $(1)/box
	cp -rv ./files/root/* $(1)

	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/webinterface.init $(1)/etc/init.d/webinterface

	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) ./files/backup-stuff $(1)/usr/sbin/backup-stuff
	$(INSTALL_BIN) ./files/restore-stuff $(1)/usr/sbin/restore-stuff
	$(INSTALL_BIN) ./files/set-country $(1)/usr/sbin/set-country
	$(INSTALL_BIN) ./files/volumes-mounter $(1)/usr/sbin/volumes-mounter

	$(INSTALL_DIR) $(1)/etc/hotplug.d/usb
	$(INSTALL_BIN) ./files/trigger-volume-mounter $(1)/etc/hotplug.d/usb/trigger-volume-mounter

	$(INSTALL_DIR) $(1)/etc/lighttpd/sites.d
	$(INSTALL_DATA) ./files/lighttpd-site.conf $(1)/etc/lighttpd/sites.d/webinterface.conf

##FIXME BUGFIXES TWEAKS FROM AUTHENTICATION BROKING WEBINTERFACE
	$(INSTALL_DIR) $(1)/etc/lighttpd/auth
	$(INSTALL_BIN) ./files/auth/webinterface.conf $(1)/etc/lighttpd/auth/webinterface.conf
	$(INSTALL_BIN) ./files/auth/webinterface.htpasswd $(1)/etc/lighttpd/auth/webinterface.htpasswd
	
##SUBSCRIBERS SCRIPTS RECOVERED FROM ARCHIVED FIRMWARE (2015)
	$(INSTALL_BIN) ./files/request-internet $(1)/usr/sbin/request-internet
	$(INSTALL_BIN) ./files/request-serverjson $(1)/usr/sbin/request-serverjson
	$(INSTALL_BIN) ./files/addressbook $(1)/usr/sbin/addressbook
	$(INSTALL_BIN) ./files/subscriber-stuff $(1)/usr/sbin/subscriber-stuff
	$(INSTALL_BIN) ./files/updater $(1)/usr/sbin/updater
	$(INSTALL_BIN) ./files/updater-testing $(1)/usr/sbin/updater-testing
	$(INSTALL_BIN) ./files/upgrader $(1)/usr/sbin/upgrader
	$(INSTALL_BIN) ./files/upgrader-testing $(1)/usr/sbin/upgrader-testing
endef

$(eval $(call BuildPackage,webinterface))
