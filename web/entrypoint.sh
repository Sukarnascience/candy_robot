#!/bin/bash
# Start PulseAudio
pulseaudio --start
exec "$@"
