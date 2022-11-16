Name:		texlive-normalcolor
Version:	40125
Release:	1
Summary:	Changing \normalcolor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/normalcolor
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/normalcolor.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a command \setnormalcolor with the same
syntax as the command \color either of package color or of
package xcolor. However, \setnormalcolor will not change the
current colour but the normal / default color.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/normalcolor
%{_texmfdistdir}/tex/latex/normalcolor
%doc %{_texmfdistdir}/doc/latex/normalcolor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
