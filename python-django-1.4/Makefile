#
# Copyright (C) 2009-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=python-django-1.4
PKG_VERSION:=1.4.14
PKG_RELEASE:=1

PKG_SOURCE:=Django-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=https://media.djangoproject.com/releases/1.4/
PKG_MD5SUM:=80dc1b9866487afc2ab3f774e29181bc

include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

PYTHON_PKG_SETUP_ARGS:=

##PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)-python/Django-$(PKG_VERSION)
PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-python/Django-$(PKG_VERSION)

define Package/python-django-1.4
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=python-django-1.4
  URL:=https://www.djangoproject.com
  DEPENDS:=+python
  VARIANT:=python
endef

define Package/python-django-1.4/description
  python-django-1.4
endef

define Build/Configure
endef

define Build/Compile
	$(call Build/Compile/PyMod,., \
		install --prefix="/usr" --root="$(PKG_INSTALL_DIR)" \
	)
endef

define Package/python-django-1.4/install
	$(INSTALL_DIR) $(1)$(PYTHON_PKG_DIR)
	$(CP) \
		$(PKG_INSTALL_DIR)$(PYTHON_PKG_DIR)/* \
		$(1)$(PYTHON_PKG_DIR)/
endef

#$(eval $(call PyPackage,python-django-1.4))
$(eval $(call BuildPackage,python-django-1.4))
