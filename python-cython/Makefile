#
# Copyright (C) 2009-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=python-cython
PKG_VERSION:=0.20.2
PKG_RELEASE:=2

PKG_SOURCE:=Cython-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.cython.org/release/
#PKG_BUILD_DIR:=$(BUILD_DIR)/Cython-$(PKG_VERSION)
PKG_MD5SUM:=7fc13e1c665bdf7cea19ad08906af91f

#PKG_BUILD_DEPENDS:=python python-cython/host
#HOST_BUILD_DEPENDS:=python

#HOST_BUILD_DIR:=$(BUILD_DIR_HOST)/Cython-$(PKG_VERSION)
#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-$(PKG_NAME)-$(PKG_VERSION)

#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-cython-$(PKG_VERSION)
#PKG_INSTALL:=1

#include $(INCLUDE_DIR)/host-build.mk
include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-cython
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=python-cython
  URL:=http://www.cython.org
  DEPENDS:=+python
  VARIANT:=python
endef

define Package/python-cython/description
  Cython is a language that should make writing C extensions for the Python language easier
endef

$(eval $(call PyPackage,python-cython))
$(eval $(call BuildPackage,python-cython))
