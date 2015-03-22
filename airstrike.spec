%define	pre	pre6a

Summary:	Incredibly addictive 2D dogfight game
Name:		airstrike
Version:	1.0
Release:	1.%{pre}.8
License:	GPL
Group:		Games/Arcade
URL:		http://icculus.org/airstrike/
Source0:	%{name}-%{pre}-src.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		airstrike-pre6a-config.patch
Patch1:		airstrike-pre6a-optflags.patch
Patch2:		airstrike-pre6a-linkage.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)

%description
Airstrike is a 0-2 players 2d dogfight game in the tradition of the 
Intellivision and Amiga games 'Biplanes' and 'BIP'. It features a robust 
physics engine and several other extensions of the original games, 
such as povray made graphics and incredible gameplay.

%prep
%setup -q -n %{name}-%{pre}-src
%patch0 -p1 -b .config
%patch1 -p1 -b .optflags
%patch2 -p1 -b .linkage

%build
%make OPTFLAGS="%{optflags}" airstrike-sound

%install
install -m755 airstrike -D %{buildroot}%{_gamesbindir}/airstrike.bin

# Launch script
cat <<EOF > %{buildroot}%{_gamesbindir}/airstrike
#!/bin/sh
if [ ! -e \$HOME/.airstrikerc ]; then
	cp %{_gamesdatadir}/%{name}/airstrikerc \$HOME/.airstrikerc
fi
cd %{_gamesdatadir}/%{name}
airstrike.bin \$@
EOF
chmod 755 %{buildroot}%{_gamesbindir}/airstrike

install -m644 airstrikerc -D %{buildroot}%{_gamesdatadir}/%{name}/airstrikerc
cp -r data  %{buildroot}%{_gamesdatadir}/%{name}

install -m644 doc/airstrike.6 -D %{buildroot}%{_mandir}/man6/airstrike.6 

#Menu items
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AirStrike
Comment=Incredibly addictive 2D dogfight game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc ChangeLog README doc
%{_gamesbindir}/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/airstrike.6*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


