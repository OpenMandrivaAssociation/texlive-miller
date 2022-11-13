Name:		texlive-miller
Version:	18789
Release:	1
Summary:	Typeset miller indices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/miller
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset miller indices, e.g., <1-20>, that are used in material
science with an easy syntax. Minus signs are printed as bar
above the corresponding number.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/miller/miller.sty
%doc %{_texmfdistdir}/doc/latex/miller/ChangeLog
%doc %{_texmfdistdir}/doc/latex/miller/Makefile
%doc %{_texmfdistdir}/doc/latex/miller/README
%doc %{_texmfdistdir}/doc/latex/miller/miller-v.tex
%doc %{_texmfdistdir}/doc/latex/miller/miller.pdf
%doc %{_texmfdistdir}/doc/latex/miller/millertest.tex
#- source
%doc %{_texmfdistdir}/source/latex/miller/miller.dtx
%doc %{_texmfdistdir}/source/latex/miller/miller.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
