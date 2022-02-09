
include $(TOPDIR)/rules.mk

PKG_NAME:=python-django-south
PKG_VERSION:=0.8.4
PKG_RELEASE:=2

PKG_SOURCE:=south-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.aeracode.org/releases/south/
PKG_MD5SUM:=ccd6ebadd3e2c8c6ef16d771632f7840

PKG_BUILD_DIR:=$(BUILD_DIR)/south-$(PKG_VERSION)/South-$(PKG_VERSION)
PKG_BUILD_DEPENDS:=python

#include $(INCLUDE_DIR)/package.mk
#$(call include_mk, python-package.mk)

PYTHON_PKG_SETUP_ARGS:=

#include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-django-south
  SECTION:=language-python
  CATEGORY:=Languages
  SUBMENU:=Python
  TITLE:=Django south 0.8.4
  URL:=http://south.aeracode.org/
  DEPENDS:=+python +python-setuptools
  VARIANT:=python
endef

define Package/python-django-south/description
 South is a tool to provide consistent, easy-to-use and
 database-agnostic migrations for Django applications.
endef

define Build/Compile
	$(call Build/Compile/PyMod,., \
		install --prefix="/usr" --root="$(PKG_INSTALL_DIR)" \
	)
endef

define Package/python-django-south/install
	$(INSTALL_DIR) $(1)$(PYTHON_PKG_DIR)
	$(CP) \
		$(PKG_INSTALL_DIR)$(PYTHON_PKG_DIR)/* \
		$(1)$(PYTHON_PKG_DIR)/
endef

#$(eval $(call PyPackage,python-django-south))
$(eval $(call BuildPackage,python-django-south))

