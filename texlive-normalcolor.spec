%global tl_name normalcolor
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	r11
Release:	%{tl_revision}.1
Summary:	Changing \normalcolor
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/normalcolor
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a command \setnormalcolor with the same syntax as
the command \color either of package color or of package xcolor.
However, \setnormalcolor will not change the current colour but the
normal / default color.

