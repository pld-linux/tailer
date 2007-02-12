Summary:	Tailer - writing output to file and screen
Summary(pl.UTF-8):   Tailer - zapis wyjścia do pliku i na ekran
Name:		tailer
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	%{name}-%{version}.tgz
# Source0-md5:	a293e91618b8093a85219385b9b8e150
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tailer is a simple utility for writing output of executed
applications to file and screen at the same time.

%description -l pl.UTF-8
Tailer to proste narzędzie do zapisywanie wyjścia z wykonywanych
aplikacji do pliku i na ekran jednocześnie.

%prep
%setup -q

%build
%{__cc} -Wall %{rpmcflags} tailer.c -o tailer

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tailer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
