
include $(TOPDIR)/rules.mk

PKG_NAME:=python-gunicorn
PKG_VERSION:=18.0
#PKG_VERSION:=19.2.0
PKG_RELEASE:=2

PKG_SOURCE:=gunicorn-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=https://pypi.python.org/packages/source/g/gunicorn/
#PKG_MD5SUM:=010e23e52324375ed9e2265d6e3be692
PKG_MD5SUM:=c7138b9ac7515a42066922d2b6120fbe

PKG_BUILD_DIR:=$(BUILD_DIR)/gunicorn-$(PKG_VERSION)
#PKG_BUILD_DEPENDS:=python python-setuptools

#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-gunicorn-$(PKG_VERSION)
#PKG_INSTALL:=1

#include $(INCLUDE_DIR)/package.mk
#$(call include_mk, python-package.mk)

include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-gunicorn
  SECTION:=language-python
  CATEGORY:=Languages
  SUBMENU:=Python
  TITLE:=Python Gunicorn
  URL:=https://pypi.python.org/pypi/gunicorn/
  DEPENDS:=+python +python-setuptools
  VARIANT:=python
endef

define Package/python-gunicorn/description
 Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.
 It's a pre-fork worker model ported from Ruby's Unicorn project.
 The Gunicorn server is broadly compatible with various web frameworks,
 simply implemented, light on server resources, and fairly speedy.
endef

$(eval $(call PyPackage,python-gunicorn))
$(eval $(call BuildPackage,python-gunicorn))

