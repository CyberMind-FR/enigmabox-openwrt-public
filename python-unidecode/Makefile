
include $(TOPDIR)/rules.mk

PKG_NAME:=python-unidecode
PKG_VERSION:=0.04.16
PKG_RELEASE:=2

PKG_SOURCE:=Unidecode-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=https://pypi.python.org/packages/source/U/Unidecode/
PKG_MD5SUM:=cd6e265fd61010a1cbfeb9dd42c6bcce

PKG_BUILD_DIR:=$(BUILD_DIR)/Unidecode-$(PKG_VERSION)
#PKG_BUILD_DEPENDS:=python

#include $(INCLUDE_DIR)/package.mk
#$(call include_mk, python-package.mk)

#PKG_INSTALL:=1

PYTHON_PKG_SETUP_ARGS:=

include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-unidecode
  SECTION:=language-python
  CATEGORY:=Languages
  SUBMENU:=Python
  TITLE:=Python Unidecode
  URL:=https://pypi.python.org/pypi/Unidecode
  DEPENDS:=+python +python-setuptools
  VARIANT:=python
endef

define Package/python-unidecode/description
 ASCII transliterations of Unicode text.
endef

$(eval $(call PyPackage,python-unidecode))
$(eval $(call BuildPackage,python-unidecode))
