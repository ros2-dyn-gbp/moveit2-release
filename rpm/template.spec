%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-moveit-ros-planning-interface
Version:        2.8.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_ros_planning_interface package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-devel
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-moveit-common
Requires:       ros-iron-moveit-core
Requires:       ros-iron-moveit-msgs
Requires:       ros-iron-moveit-ros-move-group
Requires:       ros-iron-moveit-ros-planning
Requires:       ros-iron-moveit-ros-warehouse
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rclcpp-action
Requires:       ros-iron-rclpy
Requires:       ros-iron-tf2
Requires:       ros-iron-tf2-eigen
Requires:       ros-iron-tf2-geometry-msgs
Requires:       ros-iron-tf2-ros
Requires:       ros-iron-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-eigen3-cmake-module
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-moveit-common
BuildRequires:  ros-iron-moveit-core
BuildRequires:  ros-iron-moveit-msgs
BuildRequires:  ros-iron-moveit-ros-move-group
BuildRequires:  ros-iron-moveit-ros-planning
BuildRequires:  ros-iron-moveit-ros-warehouse
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rclcpp-action
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-tf2
BuildRequires:  ros-iron-tf2-eigen
BuildRequires:  ros-iron-tf2-geometry-msgs
BuildRequires:  ros-iron-tf2-ros
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-moveit-configs-utils
BuildRequires:  ros-iron-moveit-planners-ompl
BuildRequires:  ros-iron-moveit-resources-fanuc-moveit-config
BuildRequires:  ros-iron-moveit-resources-panda-moveit-config
BuildRequires:  ros-iron-moveit-simple-controller-manager
BuildRequires:  ros-iron-ros-testing
BuildRequires:  ros-iron-rviz2
%endif

%description
Components of MoveIt that offer simpler remote (as from another ROS 2 node)
interfaces to planning and execution

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Sun Sep 10 2023 Henning Kayser <henningkayser@picknik.ai> - 2.8.0-1
- Autogenerated by Bloom

* Thu May 18 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.4-1
- Autogenerated by Bloom

* Mon Apr 24 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.3-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.2-2
- Autogenerated by Bloom

* Tue Apr 18 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.2-1
- Autogenerated by Bloom

* Thu Mar 23 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.1-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.0-2
- Autogenerated by Bloom

