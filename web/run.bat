docker run -it --rm --device /dev/snd --env PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native --volume ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --volume /run/user/$(id -u)/pulse:/run/user/$(id -u)/pulse --group-add $(getent group audio | cut -d: -f3) -v /dev/bus/usb:/dev/bus/usb robot