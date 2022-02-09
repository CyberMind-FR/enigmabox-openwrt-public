include $(TOPDIR)/rules.mk

PKG_NAME:=owncloud
PKG_VERSION:=10.7.0
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=https://download.owncloud.org/community/
PKG_MD5SUM:=29a8d79acc9271b8bfde5ab35e2ab6a5
PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
CC="$(TARGET_CC)"

include $(INCLUDE_DIR)/package.mk

define Package/owncloud
  SECTION:=admin
  CATEGORY:=Enigmabox
  TITLE:=ownCloud - self hosted cloud
  DEPENDS:=hypesites
  SUBMENU:=Hypesite apps
endef

define Package/owncloud/description
 Access your data from all your devices, on an open platform you can extend and modify.
endef

define Build/Configure
endef

define Build/Compile
endef

define Package/owncloud/install
	$(INSTALL_DIR) $(1)/srv/www/owncloud
	$(CP) -rv $(BUILD_DIR)/owncloud/* $(1)/srv/www/owncloud/
endef

$(eval $(call BuildPackage,owncloud))
