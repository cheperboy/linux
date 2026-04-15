## Enable/disable gnome session (GDM)

https://wiki.debian.org/GDM

To set your system to always boot to a console rather than GDM:

```systemctl set-default multi-user.target```

To revert the previous command and have your system always boot straight into GDM:

```systemctl set-default graphical.target```

To check the current boot target:

```systemctl get-default```

To temporarily stop GDM:

```systemctl stop gdm```

To see the status of GDM:

```systemctl status gdm```

To start GDM manually:

```systemctl start gdm```

