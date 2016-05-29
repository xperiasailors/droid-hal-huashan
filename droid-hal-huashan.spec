# These and other macros are documented in dhd/droid-hal-device.inc

%define device huashan
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia SP (C5303)

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-huashan.spec
%define android_config \
#define QCOM_BSP 1\
%{nil}

%define straggler_files\
/logo.rle\
%{nil}

%include rpm/dhd/droid-hal-device.inc
