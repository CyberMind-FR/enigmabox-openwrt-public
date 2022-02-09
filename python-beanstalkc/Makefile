
include $(TOPDIR)/rules.mk

PKG_NAME:=python-beanstalkc
PKG_VERSION:=v0.4.0
PKG_RELEASE:=2

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_URL:=https://github.com/earl/beanstalkc.git
PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_VERSION)
#PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)

#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-beanstalkc-$(PKG_VERSION)
#PKG_UNPACK:=$(HOST_TAR) -C $(PKG_BUILD_DIR) --strip-components=1 -xzf $(DL_DIR)/$(PKG_SOURCE)

#$(call include_mk, pypi.mk)
#include $(INCLUDE_DIR)/package.mk
#$(call include_mk, python-package.mk)

include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-beanstalkc
  SECTION:=language-python
  CATEGORY:=Languages
  SUBMENU:=Python
  TITLE:=Python Beanstalkc
  DEPENDS:=+python
  VARIANT:=python
endef

define Package/python-beanstalkc/description
 A simple beanstalkd client library for Python.
endef

$(eval $(call PyPackage,python-beanstalkc))
$(eval $(call BuildPackage,python-beanstalkc))

