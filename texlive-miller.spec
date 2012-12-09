# revision 18789
# category Package
# catalog-ctan /macros/latex/contrib/miller
# catalog-date 2007-01-12 00:17:35 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-miller
Version:	1.2
Release:	2
Summary:	Typeset miller indices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/miller
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miller.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 754009
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719034
- texlive-miller
- texlive-miller
- texlive-miller
- texlive-miller

