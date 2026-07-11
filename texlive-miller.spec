%global tl_name miller
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Typeset miller indices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/miller
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset miller indices, e.g., <1-20>, that are used in material science
with an easy syntax. Minus signs are printed as bar above the
corresponding number.

