#
# Copyright (C) 2013 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=python-greenlet
PKG_VERSION:=0.4.17
PKG_RELEASE:=2

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_URL:=https://github.com/python-greenlet/greenlet.git
PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_VERSION)
#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-$(PKG_NAME)-$(PKG_VERSION)
#PKG_BUILD_DEPENDS:=python

#PKG_BUILD_DIR:=$(BUILD_DIR)/$(BUILD_VARIANT)-greenlet-$(PKG_VERSION)
#PKG_INSTALL:=1

#include $(INCLUDE_DIR)/package.mk
#$(call include_mk, python-package.mk)

PYTHON_PKG_SETUP_ARGS:=

include $(TOPDIR)/feeds/packages/lang/python/pypi.mk
include $(INCLUDE_DIR)/package.mk
include $(TOPDIR)/feeds/packages/lang/python/python-package.mk

define Package/python-greenlet
  SUBMENU:=Python
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=greenlet
  URL:=https://github.com/python-greenlet/greenlet
  DEPENDS:=+python
  VARIANT:=python
endef

define Package/python-greenlet/description
  The greenlet package is a spin-off of Stackless, a version of CPython
  that supports micro-threads called "tasklets". Tasklets run
  pseudo-concurrently (typically in a single or a few OS-level threads)
  and are synchronized with data exchanges on "channels".

  A "greenlet", on the other hand, is a still more primitive notion of
  micro-thread with no implicit scheduling; coroutines, in other
  words. This is useful when you want to control exactly when your code
  runs. You can build custom scheduled micro-threads on top of greenlet;
  however, it seems that greenlets are useful on their own as a way to
  make advanced control flow structures. For example, we can recreate
  generators; the difference with Python's own generators is that our
  generators can call nested functions and the nested functions can
  yield values too. Additionally, you don't need a "yield" keyword. See
  the example in tests/test_generator.py.

  Greenlets are provided as a C extension module for the regular
  unmodified interpreter.

  Greenlets are lightweight coroutines for in-process concurrent
  programming.
endef

$(eval $(call PyPackage,python-greenlet))
$(eval $(call BuildPackage,python-greenlet))

